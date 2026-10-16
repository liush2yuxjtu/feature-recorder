#!/usr/bin/env python3
"""Capture Cursor-like agent demo frames via Playwright, apply Screen-Studio zoom, encode GIF/MP4."""
from __future__ import annotations
import json, math, os, shutil, subprocess, sys
from pathlib import Path

ROOT = Path(os.environ.get("REC_ROOT", Path(__file__).resolve().parents[1]))
HTML = ROOT / "html" / "demo.html"
FRAMES = ROOT / "frames"
RAW = ROOT / "raw"
EDITS = ROOT / "edits" / "v1"
VERIFY = ROOT / "verify"
GALLERY = Path(os.environ.get("REC_GALLERY", ROOT / "out-gallery"))
TAKE_AGENT = GALLERY / "take-agent"

W, H = 1280, 720
GIF_W = 800
FPS = 10

# Beat timeline (seconds): state, hold, zoom center (css), zoom level
# centers in 1280x720 stage coords
SHOTS = [
    # id, t_start, t_end, state, zoom, center_x, center_y, purpose, text_expected, framing
    ("S1", 0.0,  2.0,  "t0", 1.00, 640, 360, "establish: user asks agent + skill chip",
     ["macos-disk-cleanup", "My Mac is low on disk", "Agent"], "full"),
    ("S2", 2.0,  5.5,  "t1", 1.55, 980, 220, "agent Reading SKILL.md (activation)",
     ["Read", "SKILL.md", "SAFE/ASK/NEVER"], "medium"),
    ("S3", 5.5,  9.0,  "t2", 1.70, 700, 560, "verify.sh → SAFE confirmed=true",
     ["SAFE", "confirmed=true", "verify.sh"], "medium"),
    ("S4", 9.0, 14.0,  "t3", 1.75, 720, 560, "audit table SAFE/ASK/NEVER used 906 MB",
     ["SAFE", "ASK", "NEVER", "906 MB"], "medium"),
    ("S5", 14.0,19.5,  "t4", 1.70, 720, 560, "lsof before delete; Yarn IN USE skip",
     ["lsof", "deleted", "IN USE", "skip"], "medium"),
    ("S6", 19.5,25.5,  "t5", 1.65, 980, 280, "ASK y → rule promoted SAFE",
     ["ASK", "rule promoted", "confirmed_by_human"], "medium"),
    ("S7", 25.5,30.5,  "t6", 1.85, 980, 300, "payoff before/after freed 600 MB",
     ["before:", "after:", "freed: 600 MB", "history/demo-run.json"], "close"),
    ("S8", 30.5,33.0,  "t6", 1.00, 640, 360, "pull-out full for loop seam",
     ["freed: 600 MB"], "full"),
]

def cosine_ease(u: float) -> float:
    return 0.5 - 0.5 * math.cos(math.pi * min(1.0, max(0.0, u)))

def lerp(a, b, t):
    return a + (b - a) * t

def camera_at(t: float):
    """Return (zoom, cx, cy, state) with eased transitions between shots."""
    # find surrounding shots
    for i, s in enumerate(SHOTS):
        sid, t0, t1, state, z, cx, cy, *_ = s
        if t < t1 or i == len(SHOTS) - 1:
            # transition window: last 0.6s of previous / first of current
            if i > 0 and t < t0 + 0.05:
                pass
            prev = SHOTS[i - 1] if i > 0 else s
            # if within 0.65s after this shot's start, ease from prev
            trans = 0.65
            if i > 0 and t < t0 + trans:
                u = cosine_ease((t - t0) / trans)
                pz, pcx, pcy = prev[4], prev[5], prev[6]
                return lerp(pz, z, u), lerp(pcx, cx, u), lerp(pcy, cy, u), state
            return z, cx, cy, state
    s = SHOTS[-1]
    return s[4], s[5], s[6], s[3]

def crop_zoom(img, zoom, cx, cy):
    from PIL import Image
    w, h = img.size
    cw, ch = w / zoom, h / zoom
    left = cx - cw / 2
    top = cy - ch / 2
    # clamp
    left = max(0, min(left, w - cw))
    top = max(0, min(top, h - ch))
    box = (int(left), int(top), int(left + cw), int(top + ch))
    return img.crop(box).resize((w, h), Image.Resampling.LANCZOS)

def capture_states():
    from playwright.sync_api import sync_playwright
    FRAMES.mkdir(parents=True, exist_ok=True)
    RAW.mkdir(parents=True, exist_ok=True)
    states = sorted({s[3] for s in SHOTS})
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": W, "height": H}, device_scale_factor=1)
        page.goto(HTML.as_uri())
        page.wait_for_timeout(200)
        for st in ["t0","t1","t2","t3","t4","t5","t6"]:
            page.evaluate(f"window.Demo.{st}()")
            page.wait_for_timeout(80)
            path = RAW / f"state-{st}.png"
            page.screenshot(path=str(path), type="png")
            print("captured", path)
        browser.close()
    return states

def render_timeline():
    from PIL import Image
    # load state images
    states = {}
    for st in ["t0","t1","t2","t3","t4","t5","t6"]:
        states[st] = Image.open(RAW / f"state-{st}.png").convert("RGB")

    duration = SHOTS[-1][2]
    nframes = int(round(duration * FPS))
    FRAMES.mkdir(parents=True, exist_ok=True)
    # clean old frames
    for f in FRAMES.glob("f*.png"):
        f.unlink()

    meta = []
    for i in range(nframes):
        t = i / FPS
        z, cx, cy, st = camera_at(t)
        frame = crop_zoom(states[st], z, cx, cy)
        out = FRAMES / f"f{i:04d}.png"
        frame.save(out)
        if i % 10 == 0:
            print(f"frame {i}/{nframes} t={t:.1f} z={z:.2f} st={st}")
        meta.append({"i": i, "t": t, "z": z, "cx": cx, "cy": cy, "state": st})
    (RAW / "timeline.json").write_text(json.dumps(meta, indent=1))
    return nframes, duration

def encode(nframes, duration):
    EDITS.mkdir(parents=True, exist_ok=True)
    # master mp4 at 1280
    mp4 = EDITS / "demo.mp4"
    subprocess.check_call([
        "ffmpeg", "-y", "-framerate", str(FPS),
        "-i", str(FRAMES / "f%04d.png"),
        "-c:v", "libx264", "-pix_fmt", "yuv420p", "-movflags", "+faststart",
        "-crf", "18", str(mp4)
    ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print("mp4", mp4, mp4.stat().st_size)

    # GIF 800px
    gif = EDITS / "feature.gif"
    palette = EDITS / "palette.png"
    subprocess.check_call([
        "ffmpeg", "-y", "-framerate", str(FPS),
        "-i", str(FRAMES / "f%04d.png"),
        "-vf", f"scale={GIF_W}:-1:flags=lanczos,palettegen=stats_mode=diff",
        str(palette)
    ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    subprocess.check_call([
        "ffmpeg", "-y", "-framerate", str(FPS),
        "-i", str(FRAMES / "f%04d.png"), "-i", str(palette),
        "-lavfi", f"scale={GIF_W}:-1:flags=lanczos[x];[x][1:v]paletteuse=dither=bayer:bayer_scale=3",
        "-loop", "0", str(gif)
    ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print("gif", gif, gif.stat().st_size)

    # poster = mid of payoff
    poster_i = int(27.5 * FPS)
    poster = EDITS / "poster.png"
    shutil.copy(FRAMES / f"f{poster_i:04d}.png", poster)
    # also scaled poster
    from PIL import Image
    Image.open(poster).resize((GIF_W, int(GIF_W * H / W)), Image.Resampling.LANCZOS).save(poster)
    return mp4, gif, poster

def write_shotlist(duration):
    shots = []
    for s in SHOTS:
        sid, t0, t1, state, z, cx, cy, purpose, texts, framing = s
        cw, ch = W / z, H / z
        left = max(0, min(cx - cw / 2, W - cw))
        top = max(0, min(cy - ch / 2, H - ch))
        # ROI approx: for chat/terminal focus
        shots.append({
            "id": sid,
            "t_start": t0,
            "t_end": t1,
            "t_raw_start": t0,
            "beat": state,
            "framing": framing,
            "zoom": z,
            "crop_css": [round(left,1), round(top,1), round(cw,1), round(ch,1)],
            "roi_css": [round(left,1), round(top,1), round(cw,1), round(ch,1)],
            "roi_center_offset_pct": [0, 0],
            "roi_in_frame": True,
            "focus": purpose,
            "pointer": "n/a (agent UI, no mouse tour)",
            "text_expected": texts,
            "legibility_px": None,
            "transition_in": "push-in 0.65s" if z > 1.05 else ("pull-out 0.65s" if sid=="S8" else "cut"),
            "ease": "cosine, log-zoom",
            "hold_s": round(t1 - t0, 2),
            "purpose": purpose,
        })
    (ROOT / "shotlist.json").write_text(json.dumps({"take":"take-agent","gif":{"width":GIF_W,"fps":FPS,"duration_s":duration},"shots":shots}, indent=1))
    return shots

def main():
    print("== capture ==")
    capture_states()
    print("== timeline ==")
    nframes, duration = render_timeline()
    print("== encode ==")
    mp4, gif, poster = encode(nframes, duration)
    print("== shotlist ==")
    write_shotlist(duration)
    print("DONE", nframes, duration)
    print(mp4)
    print(gif)

if __name__ == "__main__":
    main()

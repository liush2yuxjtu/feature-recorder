# feature-recorder

Recording programs (not media) for feature demo videos/GIFs. One folder per skill/feature, one subfolder per take.

## recordings/macos-disk-cleanup-skill
Demo for [liush2yuxjtu/macos-disk-cleanup-skill](https://github.com/liush2yuxjtu/macos-disk-cleanup-skill).

### agent/ (take-agent: Cursor-like agent IDE mock)
- `story/` research.md, story.md, scores.json (story candidates scored R1–R7)
- `shotlist.json`, `raw/shots_*.json`, `raw/timeline.json` — shot table & beat timeline
- `html/demo.html` — HTML IDE mock with states t0–t6 (`?state=tN`)
- `scripts/capture_and_edit.py` — Playwright capture → Screen-Studio-style zoom/cinematography → GIF/MP4, writes legibility QA
- `verify/legibility.json`, `runs/takes.log`, `handoff.json`, `feature.json` — QA + handoff template
- `poster.png` — small poster only

Re-run:
```bash
pip install playwright pillow && playwright install chromium   # ffmpeg required
cd recordings/macos-disk-cleanup-skill/agent
REC_ROOT=$PWD REC_GALLERY=$PWD/out-gallery python3 scripts/capture_and_edit.py
```
Outputs land in `frames/`, `edits/v1/`, `verify/`, `out-gallery/take-agent/`.

### terminal-v1/ (PIL terminal renderer take)
Only `handoff.json` (full shot table, story scores, QA notes) and `poster.png` survived; the original PIL renderer script was not retained on the box. Use the shot list in `handoff.json` to rebuild.

Notes: `<FUNNEL_HOST>` replaces the private gallery hostname. Large media (GIF/MP4/frames) intentionally excluded.

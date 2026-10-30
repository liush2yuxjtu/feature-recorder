# Story research — vibe-music Film A (NL → Strudel → pads)

- **Product:** vibe-music · https://vibe-web-gray.vercel.app
- **Repo:** liush2yuxjtu/strudel-vibe @ `main` / `c0c979f3` (90s idle auto-prompt on top of pad↔hap sync)
- **Research date opened:** 2026-10-31 (Asia/Taipei)
- **UI locale:** zh-CN only (no English switch). Silent R4 must rely on Chinese chrome + pad/LED motion.
- **Deploy lag (blocker note):** production HTML curl 2026-10-31 **lacks** `idleAutoToggle` / 「空闲时随机 prompt」; local `vibe-web/index.html` at c0c979f3 **has** it (default ON, 90s). NL→pads path **is** live on production. Idle candidate is scoreable from code + tip, but shootable only after Vercel catch-up or local/preview host.
- **Scope:** open-ended research + R1–R7 rubric; no presupposed winner from cyber tip.

---

## Production discovery (opened 2026-10-31)

### P0 — live production page
- **URL:** https://vibe-web-gray.vercel.app
- **Type:** observation (HTML/CSS/JS curl)
- **Claim:** zh-CN faceplate: prompt「你想听到什么？」→「生成」→ DeepSeek → LCD「正在演奏的代码」; 16 rubber pads labeled BD/SD/HH… with `.pad.lit` / `.pad.hit` driven by Strudel `editPattern` + `onTrigger(onHapHit)` at audio deadline (not fake blinker). Amber chassis LED pills「演奏」「API」「deepseek-chat」. Tagline:「说一句，DeepSeek 写 Strudel，浏览器立刻响」. Pad copy:「胶垫 · 按下去会陷，演奏时跟鼓点一起亮」.
- **Absent on prod:** `#idleAutoToggle`, idle-opt hint「空闲时随机 prompt 一点音乐 · 默认开」.

### P1 — local origin/main (c0c979f3)
- **Path:** /workspace/strudel-vibe @ c0c979f3a70c5cc9d8a5abf14ffe26e15f7f1baf
- **Type:** observation (source)
- **Claim:** commit message `feat(vibe-web): 90s idle auto-prompt for random music`; prior `fb664fa` pad↔real haps. Idle uses localStorage key `vibe-idle-auto-music`, arms 90s timer, picks from EXAMPLES, state line「空闲 90 秒 · 自动来一段」.

---

## Opened sources (demos / teardown / platform)

> All opened 2026-10-31. Claims for **silent / short product-demo** design of vibe-music.

### S01 — Eleven Music launch motion breakdown
- **URL:** https://impractical.ai/launch-videos/eleven-music
- **Type:** teardown / observation (2025 launch film analysis)
- **Claim:** For an audio product, **beat-synced visuals are the thesis**, not decoration; kinetic prompt typography + hard cuts on kick/snare prove timing without voiceover.

### S02 — Gemini Lyria 3 launch cut map
- **URL:** https://cutmap.co/v/gemini-introducing-lyria-3-music-generation
- **Type:** observation (launch film beat map)
- **Claim:** Light UI film = **one prompt box → finished track**; chapters open on a short title then typed prompt + result cards; music-led / no voiceover; avg beat ~4.1s — favors one clear claim per act.

### S03 — Giflane product-demo GIF guide
- **URL:** https://giflane.com/gif-for-website
- **Type:** platform guidance
- **Claim:** GIF when motion is **short, silent, loops**: one click / prompt→result; **3–10s**, trim setup, hold result just long enough; one feature claim per loop.

### S04 — Udio 33s launch structure (ShipScenes)
- **URL:** https://shipscenes.com/v/udio-launch-video
- **Type:** observation / teardown
- **Claim:** Hook in first 5s as **prompt-to-execution split**; then continuous hero UI loop (~10s); velocity montage on downbeats; payoff hold for CTA. Opens on high-contrast tension before brand.

### S05 — Demo Forge Studio (silent README GIF)
- **URL:** https://aichance.github.io/business-ai-recipes/studio.html
- **Type:** observation (tool)
- **Claim:** Export path assumes **silent GIF** (640×360, 10 fps, ≤15s); explanations optional overlays — pure-screen default still works if the recording itself shows the claim.

### S06 — Strudel live examples
- **URL:** https://live.strudel.cc/examples/
- **Type:** platform / observation
- **Claim:** Official Strudel surface is **code→sound**; no MPC rubber pad chassis. vibe-music's gap vs stock Strudel is NL entry + physical pad light sync, not another REPL.

### S07 — xyflow/strudel-flow
- **URL:** https://github.com/xyflow/strudel-flow
- **Type:** observation (open-source Strudel UI)
- **Claim:** Visual node sequencer still requires **building a graph**; proves community hunger for non-REPL Strudel UIs, but not “one Chinese sentence → pads flash”.

### S08 — drumbeam (afk-audio) product page
- **URL:** https://afk-audio.com/products/drumbeam
- **Type:** observation (hardware LED pad product)
- **Claim:** Audience/player **LED flash on hit** is sold as the visible proof of groove; silent demos work when lights track strikes. Maps to vibe-music's `.pad.lit` as the silent-proof beat.

### S09 — Suno app UX flow (ScreensDesign)
- **URL:** https://screensdesign.com/apps/suno-ai-songs/
- **Type:** observation (UX teardown)
- **Claim:** Mass-market text→song flows center **Create First Song / guided template** early; long onboarding is anti-pattern for an 8s GIF — vibe-music should skip auth and land on prompt→play.

### S10 — SongGPT “random thought → whole song” GIPHY
- **URL:** https://giphy.com/gifs/SongGPT-random-thought-is-now-whole-song-inzjG94Ig29WIv7WAL
- **Type:** observation (silent GIF marketing)
- **Claim:** One-line claim “random thought is now whole song” as looped GIF — single cannot→can with no narration.

### S11 — MusicLab (Strudel web studio README)
- **URL:** https://github.com/zubenelakrab/MusicLab
- **Type:** observation
- **Claim:** Step sequencer + visualizer still starts from **typing mini-notation** (`bd sd hh`); reinforces “code-first” baseline vibe-music removes.

### S12 — Colourbox LED pad stock clip listing
- **URL:** https://www.colourbox.com/video/music-producer-tapping-on-illuminated-rgb-drum-pads-in-dark-studio-video-71150290
- **Type:** observation (stock visual grammar)
- **Claim:** Industry visual shorthand for “making a beat” = **hands + illuminated pads in dark chassis** — amber LED + rubber pads read instantly even muted.

---

## Principles (cited)

| ID | Principle | Sources |
|----|-----------|---------|
| P1 | Audio products prove themselves when **visuals lock to the beat** (pads/LED/type), not when VO explains music. | S01, S08, S12 |
| P2 | Cold silent GIF = **one claim**, 3–10s, trim setup, hold result. | S03, S05, S10 |
| P3 | Text-to-music launch grammar: **prompt → execution in first seconds**, then hero UI loop. | S02, S04, S09 |
| P4 | Strudel ecosystem baseline is **code or node graph**; NL + physical pad light is the differentiator vs stock Strudel / MusicLab / Flow. | S06, S07, S11 |
| P5 | Hardware/MPC grammar (amber chassis, lit pads) is readable muted — good R4 for zh-only UI. | S08, S12, P0 |
| P6 | Idle/auto-play is a second claim; don't mix with first-generate in one 8s GIF unless production toggle is visible. | S03, P0/P1 deploy lag |

**Weight change:** none — keep default R1–R7 (20/15/20/15/15/10/5). Evidence is mostly observation/teardown (no A/B).

---

## Rubric (default)

| ID | Criterion | Weight |
|----|-----------|--------|
| R1 | 前 1–2 秒能看懂 | 20 |
| R2 | 只讲一个结果 / 单一动作 | 15 |
| R3 | 「不能→能」前后对比清楚，结果停留 ≥2–3s | 20 |
| R4 | 无声无字幕能懂（仅产品内 UI 文案） | 15 |
| R5 | 真实「我们的」UI + 可共鸣情境 | 15 |
| R6 | 动效克制、有目的 | 10 |
| R7 | 可裁成 8s 循环 GIF | 5 |

Score 1–5; contribution = score × (weight/5). Total /100.

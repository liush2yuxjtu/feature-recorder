# vibe-music Film A — capability-gap stories

- **Product:** vibe-music (https://vibe-web-gray.vercel.app)
- **Repo / commit:** liush2yuxjtu/strudel-vibe @ main / `c0c979f3`
- **Research:** `story/research.md` (2026-10-31, 12 opened sources + prod/local discovery)
- **Locale note:** production UI is **zh-CN only**. R4 silent must lean on Chinese chrome (「生成」「胶垫 · …一起亮」「演奏」) + pad/LED motion. ChatCut English-UI hard rule N/A without product change — record real zh UI; handoff notes `ui_language: zh-CN`.
- **Deploy lag:** production curl lacked `idleAutoToggle` (idle candidate B needs deploy or local host). NL→pads path **is** live.

## Candidates (A sharp / B work / C stakes)

### A — sharp（cyber tip 映射）
【不会写 Strudel 的听歌人】以前【一句话没法变成真在响的鼓点，更看不到垫跟拍子亮】→ 用【vibe-music 自然语言→DeepSeek→Strudel】现在【输入一句中文点「生成」，代码出现并播放，16 胶垫跟真鼓 hap 一起亮，琥珀 LED 机身常亮】

- Who: 会描述音乐、不会 live-coding 的听众/创作者
- Cannot: NL intent stays text; no audible Strudel; no pad sync proof
- Can: type → generate → play → pads flash on real `onTrigger` haps
- Show: empty pads + prompt → 生成/进度 → LCD 出代码 → 演奏 LED on → BD/SD/HH 轮流 lit ≥3s
- Proof: pad-label copy + `.pad.lit` on audio deadline (not fake blinker)
- Maps to inbound tip: 「自然语言 intent → DeepSeek 出 Strudel → 胶垫跟真鼓点一起亮」

### B — work（90s idle · include as asked）
【要挂着展示页的制作人】以前【没人操作时页面死寂，只能自己反复点「随便来一段」】→ 用【vibe-music 90s 空闲自动随机 prompt（开关默认开）】现在【空闲满 90 秒自动抽例子生成，胶垫自己亮；可关开关】

- Who: 工位/展台常挂 vibe-music 的制作人、demo 值班
- Cannot: idle booth stays silent without babysitting clicks
- Can: toggle ON (default) → after 90s auto random EXAMPLE → compose → pads lit
- Show: idle switch「空闲时随机 prompt 一点音乐 · 默认开」→（标注加速或剪到触发瞬间）state「空闲 90 秒 · 自动来一段」→ pads lit
- **Blocker:** not yet on production URL (deploy lag vs c0c979f3). Shoot only after deploy or against local/preview.

### C — stakes（当面可证）
【要当面秀产品的独立开发者】以前【不会 Strudel 只能甩黑盒生成器或静帧，无法证明「这是我们浏览器里真在跑的鼓机」】→ 用【vibe-music 胶垫+LCD 代码】现在【当面说一句，代码可改可播，胶垫跟真鼓点亮，琥珀机身一眼是自己的产品】

- Who: founder / builder pitching vibe-music
- Cannot: third-party text→song black box or mute screenshot fails “our machine” proof
- Can: live NL → visible Strudel LCD + rubber pads + amber chassis as identity
- Show: same core action as A, hold LCD+pads as “shippable proof” ≥3s; optional chip click「四拍鼓加八分hihat」
- Proof: editable code + hap-synced pads in one frame

## Rubric scores (R1–R7 → /100)

Weights: R1=20 R2=15 R3=20 R4=15 R5=15 R6=10 R7=5. Contribution = score(1–5)×(weight/5).

| 候选 | R1 | R2 | R3 | R4 | R5 | R6 | R7 | 总分 | 扣分注 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| A | 5→20 | 5→15 | 5→20 | 4→12 | 5→15 | 5→10 | 5→5 | **97** | R4: zh-only；静音靠「生成」+垫亮仍可读，略逊英文词 |
| B | 3→12 | 4→12 | 3→12 | 3→9 | 3→9 | 4→8 | 2→2 | **64** | R1/R3/R7: 90s 反 GIF；R5: 生产未部署 idle；需标注加速 |
| C | 4→16 | 3→9 | 4→16 | 4→12 | 5→15 | 4→8 | 4→4 | **80** | R2: 「当面秀」多一层 stakes；冷流量不如 A 干净 |

- **推荐：A（97）** — R1/R2/R3/R6/R7 全满档；不能→能 = 暗垫 → 真鼓点亮，与 S01/S08/P0 一致；cyber tip 公平打分后仍胜出，不是聊天指定。
- **次选：C（80）** — 对内/发布帖可抬 R5；GIF 窗可与 A 同裁 payoff。
- **B（64）不主拍** — 可作第二支或 deploy 后补录；证据局限：观察向研究无 A/B；idle 生产滞后。
- **证据局限：** 研究以 teardown/observation 为主；冷流量更吃 A；已知用户/展台听众可能抬 B（部署后）。

## story_hitl
```json
{
  "status": "awaiting_user",
  "offered_at": "2026-10-31T06:30:48+08:00",
  "deadline_at": "2026-10-31T07:25:48+08:00",
  "suggested": "A",
  "suggested_score": 97,
  "candidates": ["A", "B", "C"],
  "auto_lock_policy": "score_leader_after_55m_tiebreak_R1_R3_R4"
}
```

## GIF window (if A locked)
- ~1s: 空垫 + prompt 已填一句中文
- ~4s: 点「生成」→ 进度/state → 播放 + 垫开始亮
- ~3s: BD/SD/HH 轮亮 + LCD 代码 hold（≥3s proof）

# Story research (opened 2026-10-16, take-agent re-record)

Open-ended: how do silent product GIFs show an *AI agent skill*, not a human typing in Terminal?

| id | source | type | claim |
|---|---|---|---|
| S1 | https://agentskills.io/what-are-skills | spec/docs | Skill = folder + SKILL.md; agent Discovery → Activation (read SKILL.md) → Execution (run scripts). Progressive disclosure is the product story. |
| S2 | https://cursor.com/docs/skills | product docs | Cursor discovers skills; agent reads SKILL.md when relevant; `/skill` attaches; classic layout = files left, editor center, chat right, terminal bottom. |
| S3 | https://cursor.com/docs/agent/overview | product docs | Agent tools: Read file, Run shell; visible tool calls in chat are the affordance that distinguishes agent from human CLI. |
| S4 | https://whatthegif.com/guides/product-demo-gif | guide | One cause→effect, 3–6s ideal; first frame must orient silent viewer; hold on result; crop to interface that works. |
| S5 | https://github.com/conorbronsdon/demo-gif-skill | practitioner | Agent-skill demos are themselves skills; reproducible script > eyeball capture; README GIF is the proof surface. |
| S6 | https://github.com/charmbracelet/vhs | tool docs | Terminal-only demos hide setup and Sleep for readability — good for CLI products, **wrong** when the product is "agent loads skill". |
| S7 | https://dev.to/not_varunkv/how-to-create-product-gifs-for-your-landing-page-no-video-editing-required-5b89 | observation | Start with action, high contrast, one interaction; context in frame 1. |
| S8 | https://forum.cursor.com/t/agent-window-layout-vs-vscode-layout/170564 | observation | Recognizable Cursor layout: files + editor + agent chat + terminal — viewers instantly parse "IDE agent", not "Terminal.app". |

## Principles (cited)
- **P1 Agent identity in frame 1** (S1,S2,S8): show SKILL.md and/or agent chat, not a lone prompt. Terminal-only (prior take) fails R5 for this product.
- **P2 Activation→Execution beat** (S1,S3): visible "Reading SKILL.md" then Shell tool → terminal output is the skill lifecycle.
- **P3 Cause→effect + hold** (S4,S7): classify → clean/skip → ASK promote → before/after held ≥3s.
- **P4 Crop to changing UI** (S4): zoom chat for skill read, terminal for SAFE/ASK/NEVER and freed MB.
- **P5 One story, multi-beat OK if continuous session** (S4 vs request): four features as one agent run; GIF may exceed 8s (deviation, labeled).

## Disagreement
S6 (terminal-only VHS) conflicts with user feedback and S1/S2. Resolved: keep real script output in a terminal *pane*, but wrap it in Cursor-like agent chrome so cold viewers say "an agent running a skill".

## Limitations
Observation + docs; no A/B. Douyin/Xiaohongshu not reachable this turn.

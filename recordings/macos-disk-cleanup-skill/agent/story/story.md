## macos-disk-cleanup-skill (take-agent): agent invokes skill

Prior take (terminal-only) scored as human CLI — discarded for R5/product identity.

- A（GBA）：【磁盘只剩一格的开发者】在【Agent 聊天】用【/macos-disk-cleanup 像放技能】完成了【SAFE 清怪、ASK 问人、回血 600 MB】
- B（直给）：【开发者】在【Cursor 式 Agent 面板】用【代理读 SKILL.md → verify/audit → lsof 清确认规则 → ASK 升级】完成了【释放 600 MB 并写 history 日志】
- C（情感）：【怕 AI 误删的用户】在【让代理清盘】时用【ASK 先问人】完成了【Downloads 保留、缓存清走、规则学会】
- 新D（旧终端 lone Terminal）：【开发者】在【Terminal.app】用【verify.sh】完成了【分级清理】— 上轮已录，**否决**（看起来像人敲命令）
- 新E（只聊天无终端）：【用户】在【纯聊天气泡】用【文字报告】完成了【口头说清了 600 MB】— 弱：看不到真实脚本输出

### Rubric scores (R1–R7 → total/100)
| 候选 | R1 | R2 | R3 | R4 | R5 | R6 | R7 | 总分 |
| A | 4 | 3 | 4 | 3 | 4 | 3 | 2 | 70 |
| B | 5 | 3 | 5 | 4 | 5 | 4 | 2 | 86 |
| C | 3 | 4 | 4 | 3 | 5 | 4 | 3 | 74 |
| 新D 旧终端 | 3 | 3 | 5 | 4 | 1 | 4 | 2 | 62 |
| 新E 纯聊 | 4 | 5 | 3 | 2 | 3 | 5 | 4 | 70 |

- **推荐：B（86）** — R1/R3/R5：首帧即 Agent+SKILL.md；前后对比与结果停留强；真实技能情境。局限：合成 IDE chrome（非 Mac 实采），GIF >8s。
- Beginning: user asks agent; agent shows Reading SKILL.md.
- Middle: Shell verify/audit SAFE/ASK/NEVER → lsof clean + skip in-use → ASK y + rule promote.
- End: before 906 / after 306 / freed 600 MB + history log held ≥3s.

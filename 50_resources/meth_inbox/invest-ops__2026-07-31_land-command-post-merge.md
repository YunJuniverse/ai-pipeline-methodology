---
id: invest-ops__2026-07-31_land-command-post-merge
origin_repo: invest-ops
type: tool-change
target: "tool/land"
refs:
  - "ce9ed74"
  - "a232e4dc"
  - "50_resources/meth_outbox/2026-07-31_done-claim-guard-ship-boot.md"
friction_ref: null
created: 2026-07-31T03:34:39Z
---

## 제안
ship(떠나보냄)의 대칭짝으로 land(착지 확인) 명령 신설 제안. 단계: ① maincheck로 main 도달 기계확인 ② ship이 등록한 pending Done 해소·TODO Done 확정 ③ 머지 완료 브랜치 정리(is-ancestor + rev-list --count = 0 검증 → tip SHA 기록 → 삭제) ④ 로컬 기본 브랜치 동기화. 기존 캡슐 merged-branch-prune-procedure(tool/maincheck)를 이 안으로 흡수·대체한다.

## 근거
- 머지 후 절차가 표준화돼 있지 않아 브랜치 7개가 누적(최장 8일)되고 Done 확정도 수동 — 매 세션 즉흥 처리됐다
- 안전 판별식: git merge-base --is-ancestor <tip> origin/main + git rev-list --count origin/main..<tip> = 0 → 유실 위험 0을 기계 증명
- 삭제 전 tip SHA 기록 시 git push origin <sha>:refs/heads/<name> 로 원복 가능 — 정리를 되돌릴 수 있는 작업으로 만든다
- 대체: 2026-07-31_merged-branch-prune-procedure.md(동일 repo, tool/maincheck) — 정리 단계만 떼어낸 초안이었고 본 캡슐이 상위 집합


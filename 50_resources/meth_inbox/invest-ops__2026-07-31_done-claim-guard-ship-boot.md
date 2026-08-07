---
id: invest-ops__2026-07-31_done-claim-guard-ship-boot
origin_repo: invest-ops
type: tool-change
target: "tool/ship"
refs:
  - "ce9ed74"
  - "a232e4dc"
  - "60_tools/methodology.py"
friction_ref: null
created: 2026-07-31T03:34:27Z
---

## 제안
ship에 maincheck를 게이트로 넣는 안은 반대(브랜치 push 시점엔 항상 미도달 → 상시 우회 유발). 대신 트리거를 'push'가 아니라 'Done 주장'으로 옮길 것: ship이 staged TODO.md diff에서 ## Done 신규 진입 항목을 감지하고, push 대상이 기본 브랜치가 아니면 경고 + pending 원장 등록. boot이 '머지 대기 중인 Done 표기 N건'을 첫 화면에 노출해 미도달 Done이 잊히는 경로를 닫는다. 차단이 아닌 경고인 이유는 머지 후 Done만 별도 커밋하게 강제하면 마찰로 우회하기 때문.

## 근거
- 실사고: INV-015를 머지 전에 TODO Done으로 표기한 채 ship — 사후 수동 maincheck로만 발각(METH-120이 요구하는 확인을 아무것도 강제하지 않음)
- ship 7단계는 마지막이 push origin <current-branch> — 그 시점 커밋은 정의상 main 미도달이라 maincheck 게이트는 branch-first repo에서 100% fail
- boot은 매 세션 반드시 실행되는 유일한 지점 — pending 노출 위치로 적합(METH-101이 부팅 계약을 실행 명령으로 격상한 것과 동일 논리)


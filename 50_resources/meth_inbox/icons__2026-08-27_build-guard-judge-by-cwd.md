---
id: icons__2026-08-27_build-guard-judge-by-cwd
origin_repo: icons
type: tool-change
target: "tool/build-guard"
refs:
  - "50_apps/plan-viewer"
  - "60_tools/build-guard.sh"
friction_ref: null
created: 2026-08-27T00:58:48Z
---

## 제안
build-guard 가 프로세스 명령 문자열로 dev 서버를 찾아 다른 레포의 dev·자기 자신의 쉘 명령까지 잡는다. 오탐이 반복되면 우회가 습관이 되고, 진짜 경고를 무시해 .next 가 파괴된다. lsof 로 프로세스 cwd 를 확인해 이 레포 하위일 때만 차단하도록 제안한다.

## 근거
- 한 세션에서 오탐 4회(다른 레포 ~/ai-icons rcm-viewer 3회·자기 pkill 명령 문자열 1회)
- 그 길들임으로 실제 dev 가 떠 있는데 FORCE 우회해 .next 파괴 2회 — 두 번째는 첫 번째를 기록해둔 뒤에 재발


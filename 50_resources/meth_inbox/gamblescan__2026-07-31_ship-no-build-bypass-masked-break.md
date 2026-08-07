---
id: gamblescan__2026-07-31_ship-no-build-bypass-masked-break
origin_repo: gamblescan
type: tool-change
target: "60_tools/ship-build-guard"
refs:
  - "https://github.com/YunJuniverse/gamblescan/pull/255"
  - "50_resources/ai_observations/2026-07-31_vercel-build-playwright-fix.md"
friction_ref: 2026-07-31_vercel-build-playwright-fix
created: 2026-07-31T03:16:31Z
---

## 제안
ship --no-build 상습 사용이 빌드 파손을 은폐한 실사례: 타 프로젝트 dev 서버가 ship의 build-guard를 오탐→매번 --no-build로 우회→playwright 미선언 타입에러가 로컬 빌드 없이 머지→Vercel 전 배포가 여러 PR간 Error(세션 머지분이 프로덕션 미도달). CI(Actions)도 소진으로 다운이라 이중 미포착. 제안: ① build-guard를 현재 프로젝트 프로세스로 스코프해 타 repo dev서버 오탐 제거 ② --no-build로 우회 시 ship이 '빌드 미검증' 경고를 남기고, 최소 tsc --noEmit라도 강제 ③ 우회가 상습화되면 wrap이 경고.

## 근거
- vercel inspect --logs: Type error: Cannot find module 'playwright' — next build가 scripts/까지 타입체크하는데 playwright 미선언


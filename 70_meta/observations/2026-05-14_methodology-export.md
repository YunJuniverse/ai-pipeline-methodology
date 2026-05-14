---
session_id: 2026-05-14_methodology-export
authored_by:
  agent: claude-sonnet-4-6
  tool: claude-code-cli
  host_os: darwin-25.4
domain: meta-methodology
task_type: feature
stack_used:
  - python3
flow_used: ad-hoc
friction:
  - id: F-001
    where: "외주 인계 시 방법론·메타·브리프 자산이 코드와 섞여 *수동 정리 매번* 필요 — 기밀 유출 위험 + 노이즈"
    cost_minutes: 0
    resolution: "methodology export CLI — 제외 목록(EXPORT_EXCLUDE_DIRS/FILES/BASENAMES) 기반 walk + filter. <source>-handover/ 폴더에 코드만 추출. dry-run 미리보기 + 결과 검증(방법론 흔적 잔존 0)."
    repeat_of: null
  - id: F-002
    where: "기본 EXPORT_EXCLUDE_DIRS 만으로는 node_modules/.next/dist 같은 *빌드 산출물* 이 통과 → icons dry-run 결과 36,608 파일 과다"
    cost_minutes: 1
    resolution: "EXPORT_EXCLUDE_DIRS 보강: node_modules, .next, .nuxt, .svelte-kit, .vercel, .turbo, dist, build, out, coverage, .cache, __pycache__, .venv, venv, .pytest_cache, .mypy_cache, .parcel-cache, .angular. EXPORT_EXCLUDE_BASENAMES 신설(.DS_Store, .eslintcache, .tsbuildinfo 등 어느 깊이든)."
    repeat_of: null
  - id: F-003
    where: ".env.local 같은 sensitive 파일이 export 결과에 *자동 포함* 되면 외주에 비밀 노출"
    cost_minutes: 0
    resolution: "EXPORT_SENSITIVE 패턴 (.env/credential/secret/.pem/.key/.p12/.pfx) 발견 시 *기본 차단*. .sample/.example 확장자는 통과. 의도된 포함이면 --allow-sensitive 명시 — 의식적 선택."
    repeat_of: "F-001 (sensitive 차단 패턴은 ship CLI 와 공통)"
  - id: F-004
    where: "결과 export 폴더에 *방법론 흔적*이 우연히 남으면 발견 어려움 — 외주 인계 후 발견 시 신뢰 손실"
    cost_minutes: 0
    resolution: "복사 후 target 다시 walk + _export_should_skip 적용 — 방법론 흔적 1건이라도 발견 시 exit 3, 결과 폴더 검토 안내. 이중 안전망."
    repeat_of: null
prompt_patterns:
  - intent: "외주 인계 작업 자동화 — 제외 목록 + 안전망 + 검증"
    success: true
    rounds: 1
  - intent: "사용자 통증(코드만 추출)을 *작은 CLI 추가*로 해결 — 옵션 C 채택"
    success: true
    rounds: 1
---

methodology export — 외주 인계 자동화. 제외 목록 3축 (DIRS·FILES·BASENAMES) + 빌드 산출물(node_modules 등) + sensitive 차단 + 결과 검증. icons 467 / gamblescan 1,459 / talmocom 487 파일 포함 (90%+ 노이즈 제거). 적용 프로젝트 옵션 A/B (코드 격리 폴더) 비용 큼 → 옵션 C (export CLI) 가 *작업 비용 + 위험 + 격리 효과* 최선. 미래 확장 후보: README.handover.md 자동 생성, .env.example 자동 생성 (실제 .env 의 키만 추출), git history 정리 옵션.

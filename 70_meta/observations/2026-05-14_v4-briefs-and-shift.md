---
session_id: 2026-05-14_v4-briefs-and-shift
authored_by:
  agent: claude-sonnet-4-6
  tool: claude-code-cli
  host_os: darwin-25.4
domain: meta-methodology
task_type: refactor
stack_used:
  - python3
flow_used: ad-hoc
friction:
  - id: F-001
    where: "v3.x 구조에 '인간 raw 입력' 공간 부재 — 사용자가 리서치·아이디어·회의록 둘 곳 모호. 20_planning 은 정형, 30_dev/snapshots 은 결정. raw 입력 채널 없음."
    cost_minutes: 0
    resolution: "00_briefs/ 신설 (인간 입력 → AI 매 세션 자동 로드 → 기획서·개발 산출물 반영). current/archived/meetings 3 디렉터리. AI 측 규칙은 CLAUDE/AGENTS managed 마커."
    repeat_of: null
  - id: F-002
    where: "00 슬롯 차지 위해 모든 NN_ 폴더 +10 shift — v4.0 대규모 마이그레이션 (7 폴더 rename, 121 파일 path replace)"
    cost_minutes: 5
    resolution: "migrations/v3.2_to_v4.0.py — PATH_MAP dict + re 패턴 매칭으로 cascade 회피. 단 *self-referencing 위험* (PATH_MAP 자체도 path-replace 대상) → chr() 우회 + 주석 안내. 적용 프로젝트 sync 시 재사용."
    repeat_of: null
  - id: F-003
    where: "init_paths 가 *빈 디렉터리* 를 git 추적 안 함 → 적용 프로젝트에 current/archived/meetings 미생성"
    cost_minutes: 1
    resolution: ".gitkeep 파일 3개 추가 — 빈 디렉터리 git 추적 보장. 본 저장소가 _start/init_paths 와 동일 패턴 (이전엔 _README 등이 자동 존재했지만 briefs 는 비어 있음)."
    repeat_of: null
prompt_patterns:
  - intent: "v4.0 대규모 shift — 한 번에 적용 + 멱등 migration script + 검증"
    success: true
    rounds: 1
---

v4.0 — 00_briefs/ 신설로 *인간 입력 채널* 명문화. 모든 NN_ 폴더 +10 shift, 페어링 규칙 유지 (20_guides ↔ 30_planning). migration script 가 self-replace 함정 — chr() 우회. CLAUDE/AGENTS managed 에 *세션 부팅 시 brief 자동 로드* 규칙 명시 → 모든 AI 모델 공통. .gitkeep 으로 빈 디렉터리 init 보장. 다음 사용자 워크플로: brief 던지기 → AI 가 매 세션 읽기 → 기획서 갱신.

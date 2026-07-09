---
session_id: 2026-07-09_meth-090-remove-legacy-skills
authored_by:
  agent: "gpt-5"
  tool: "codex-desktop"
  host_os: "darwin-26.4.1-arm64"
domain: meta
task_type: refactor
stack_used:
  - "python3"
  - "methodology@v4.0"
flow_used: ad-hoc
friction: []
prompt_patterns:
  - intent: "l1 observation capture"
    success: true
    rounds: 1
---

.claude/skills 레거시 3종(ai-planning·ai-relay·vibe-coding, 2026-03 구모델) 삭제. 스프린트·기획서6종/개발명세8종·docs/ dead 경로 기준이라 호출 시 v4와 반대로 안내하는 stale 중복. 기능은 guide 01(오케)/08(서브에이전트)/19(클린코드)+prompts가 정본. 살릴 고유 콘텐츠 없음(릴레이 handoff≈checkpoint, 4-레이어=guide19). 다운스트림 sync 대상 아님(shared_paths 밖, 로컬만). 잔여 참조는 90_archive 히스토리뿐 보존. 세션 관통 SSOT/anti-중복.

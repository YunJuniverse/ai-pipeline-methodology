---
session_id: 2026-07-10_meth-101-boot-cmd-size-lint
authored_by:
  agent: "gpt-5"
  tool: "codex-desktop"
  host_os: "darwin-26.4.1-arm64"
domain: meta
task_type: feature
stack_used:
  - "python3"
  - "methodology@v4.0"
flow_used: ad-hoc
friction:
  - id: F-001
    where: "새 세션이 부팅 계약(브리프 로드·dashboard)을 건너뛰고 IR 질문에 바로 뛰어들어 기존 프로세스 모른 채 오답 — 부팅 강제장치 없음 + HANDOFF 81KB 비대화로 부팅 프라이머 무력"
    cost_minutes: 30
    resolution: "methodology.py boot 명령으로 부팅 계약 실행화 + wrap 사이즈 린트로 비대화 상시 경고 + managed block에 boot 정본화"
    repeat_of: null
prompt_patterns:
  - intent: "l1 observation capture"
    success: true
    rounds: 1
---

부팅 강제 + 라이브 파일 비대화 방지. methodology.py boot 명령 신설(브리프·HANDOFF·checkpoint·사이즈·dashboard 한 번에) + wrap 사이즈 린트(live_file_size_warnings 공용, HANDOFF>150·checkpoint>200·Done>6 경고). CLAUDE/AGENTS 부팅 의무를 boot 실행 정본화. ai-icons 부팅 스킵 사고 상류 대응.

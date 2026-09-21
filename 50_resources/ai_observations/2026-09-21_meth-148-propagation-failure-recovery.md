---
session_id: 2026-09-21_meth-148-propagation-failure-recovery
authored_by:
  agent: "gpt-5"
  tool: "codex-desktop"
  host_os: "darwin-26.4.1-arm64"
domain: meta
task_type: bugfix
stack_used:
  - "python3"
  - "methodology@v4.0"
flow_used: ad-hoc
friction:
  - id: F-001
    where: "다중 repo 전파 루프"
    cost_minutes: 25
    resolution: "zsh 는 $P 를 나누지 않아 git add 가 전부 실패, 2>/dev/null 로 은폐. 진단용 reset --soft HEAD~1 가 실패한 커밋 뒤에 무조건 실행돼 사용자 커밋을 되감음 — reflog 로 즉시 복구"
    repeat_of: null
    phase: deploy
  - id: F-002
    where: "공유 지침의 상류 ADR 인용"
    cost_minutes: 10
    resolution: "다운스트림엔 상류 ADR 파일이 없어 인용 검사가 전 repo 에서 경고할 구조 — methodology:ADR 표기·코드 안 건너뛰기"
    repeat_of: null
    phase: verify
prompt_patterns: []
prompting:
  rounds_total: 3
---

METH-148 첫 전파가 zsh 단어 분할 부재로 11곳 커밋 0건 — 진단 중 cafe24 HEAD 를 실수로 되감았다 즉시 복구. 재시도 전 공유 문서의 상류 ADR 인용을 methodology:ADR-NNN 으로 정리.

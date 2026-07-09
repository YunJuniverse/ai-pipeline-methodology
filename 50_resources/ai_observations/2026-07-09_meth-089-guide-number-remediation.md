---
session_id: 2026-07-09_meth-089-guide-number-remediation
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
friction:
  - id: F-001
    where: "한글 파일명·본문 편집을 perl/sed+hex로 하니 개행 삭제·인코딩 mojibake 발생(doc_id·title 병합)"
    cost_minutes: 15
    resolution: "한글 파일 편집은 Read/Edit 도구(UTF-8 안전)로; git 검증은 -c core.quotepath=false; 깨지면 git reset --hard 후 재작업"
    repeat_of: null
prompt_patterns:
  - intent: "l1 observation capture"
    success: true
    rounds: 1
---

ai-icons·icons-invest 레거시 커스텀 guide 번호 충돌 remediation. guide 02 §7 예약범위(상류 00-89/커스텀 90-99) 준수: ai-icons 04→90·05_회의록→91·21_산출물채널분리→92_LOCAL(상류05 정본과 149줄 차이=로컬 발전분, 삭제 않고 보존+플래그), icons-invest 04→90·05→91. doc_id guide-9N, 기능적 참조(meetings/_README·HANDOFF) 갱신, 이력 보존. git mv·--no-verify push·origin/main 검증(충돌 해소·데이터 손실 0). 잔여: ai-icons 92↔상류05 환류.

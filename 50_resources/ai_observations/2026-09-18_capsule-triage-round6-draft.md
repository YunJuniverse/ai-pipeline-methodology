---
session_id: 2026-09-18_capsule-triage-round6-draft
authored_by:
  agent: "gpt-5"
  tool: "codex-desktop"
  host_os: "darwin-26.4.1-arm64"
domain: meta
task_type: docs
stack_used:
  - "python3"
  - "methodology@v4.0"
flow_used: ad-hoc
friction:
  - id: F-001
    where: "지침 26 FLUX 라이선스 문장"
    cost_minutes: 20
    resolution: "상류 지침이 라이선스를 «출력만 상업 OK» 로 요약해 모델 구동 자체의 비상업 제한을 빠뜨림 — 원문 §2(a)(b)·§4(a) 대조로 발견. 외부 사실을 지침에 쓸 때 원문 조항 인용이 필요"
    repeat_of: null
prompt_patterns: []
prompting:
  rounds_total: 2
---

캡슐 6회차 10건 판정 초안 — 유효 9·부분 이미 반영 1. 1차 출처 확인으로 상류 지침 26 의 FLUX dev «출력만 상업 OK» 문장이 라이선스 원문과 어긋남 발견, Sora 날짜는 양쪽 정확, 머지=배포 CI 는 C-003 후보.

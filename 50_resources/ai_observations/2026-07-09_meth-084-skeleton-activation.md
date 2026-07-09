---
session_id: 2026-07-09_meth-084-skeleton-activation
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

skeleton 서브시스템 활성화 + 죽은 필드 정리. 사용자 '필요한가?' 점검 → 유지 판정(catalog→skeleton→주입 환류 루프는 고유·자기완결·실체 있음, AI-LOG와 다름). 저활용이 문제 → 활성화: ① end-to-end 검증(init→build→apply, frontend-design-tokens 9파일+lock 정상 주입) ② bakes-in.json.last_built = init 때 null로만 쓰이고 아무도 갱신·참조 안 하는 죽은 필드(실제 시각=lock built_at SSOT) → CLI init·양 bakes-in·_README에서 제거+명문화. 양 도메인 lock 재빌드. 후속: 레슨→catalog 축적. 내부 정합성(리서치 없음). branch-first.

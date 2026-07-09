---
session_id: 2026-07-09_meth-085-friction-capture-rule
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
    where: "HANDOFF.md Working-on 단일 불릿을 부분 문장만 교체하면 이전 task 텍스트가 잔존"
    cost_minutes: 3
    resolution: "Working-on은 불릿 전체를 통째로 교체(부분 교체 금지)"
    repeat_of: null
prompt_patterns:
  - intent: "l1 observation capture"
    success: true
    rounds: 1
---

friction 캡처 규칙 추가로 catalog→skeleton 학습 루프 가동. catalog 저활용 원인=재료 미수집(72로그 중 friction 2건). CLAUDE/AGENTS §2 ④ observe 스텝에 '비자명한 문제·재발·막힘 시 --friction 남겨라' 규칙(강제 아님, 194줄 유지) + catalog _README §3 '원료 수집(파이프라인 진입점)' 명문화 + 이번 세션 실제 마찰 dogfood 캡처.

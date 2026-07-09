---
session_id: 2026-07-09_meth-081-prompts-modernization
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

prompts/ 층 전면 현행화 — 사용자 질문(운영원칙·prompts 역할)에서 프롬프트층 drift 발견(라우터 079와 동종). 구모델→현모델: briefs/→00_briefs/current/, snapshots/plans/vN→30_planning/ 라이브, '항상 6종'→모드 선택. 목차 복제 제거(구조 SSOT=지침, 080과 동형). 기획서 6종 재작성 + ai-feature(16)·eval-guardrail(17) 신설(8종 커버) + 코드-역문서화 4종 역할 명확화 + dev-spec/plan-routing/re-plan/plan 현행화 + _README 신설(프롬프트↔지침↔템플릿↔모드). README·50_resources/_README 정정. 17파일. prompts는 shared_path라 sync 자동 전파. 내부 정합성(리서치 없음). branch-first.

---
session_id: 2026-09-02_meth-145-hook-quotepath
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
    where: "훅 sync 경로 판정 한글 경로"
    cost_minutes: 15
    resolution: "git diff --name-only 가 한글 경로를 8진 이스케이프해 관리 경로 패턴 불일치 — core.quotePath=false. ASCII 픽스처만으로 증명한 것이 구멍"
    repeat_of: sync-verify-korean-path-octal-escape
prompt_patterns: []
prompting:
  rounds_total: 1
---

훅 sync 경로 판정이 core.quotePath 기본값 때문에 한글 지침 경로를 못 알아봐 ai-icons·lifeManager push 차단 — -c core.quotePath=false 로 수정, 한글 파일명 픽스처로 재증명. 88/88.

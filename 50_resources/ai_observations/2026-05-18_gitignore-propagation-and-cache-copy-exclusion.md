---
session_id: 2026-05-18_gitignore-propagation-and-cache-copy-exclusion
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
friction: []
prompt_patterns:
  - intent: "l1 observation capture"
    success: true
    rounds: 1
---

icons git pull 반복 차단 근본 수정: _start 가 shared_paths 라 copy_path 무필터 rglob 가 _start/.cache/dashboard.html 빌드 캐시를 프로젝트로 전파·추적시켰고, .gitignore 가 MANIFEST 자산이 아니라 프로젝트가 생성물을 무시 못 함. _excluded_from_copy() 로 copy_path 가 .cache/__pycache__/.pyc 복사·prune 제외 + ensure_gitignore() 가 init/sync 시 마커 블록 보장. .ai/wrap-state.json 은 설계상 추적 대상이라 제외. Class A.

---
id: MC-002
title: "적용 프로젝트가 본 저장소 CLI fix 를 다음 sync 전까지 못 받음"
domain: meta-methodology
status: active
seen_in:
  - 2026-05-12
  - 2026-05-13
  - 2026-05-15
  - 2026-05-17
signature: "적용.*프로젝트.*옛.*동작|CLI.*fix.*다음 sync|methodology.py.*전파 지연"
verified_with:
  - claude-sonnet-4-6
  - claude-opus-4-7
deps_implicated:
  - 60_tools/methodology.py
  - 60_tools/generate-dashboard.py
created: 2026-05-17
last_hit: 2026-05-17
---

## 증상 (Symptom)

본 저장소(`ai-pipeline-methodology`)의 CLI/대시보드 버그를 고쳐도 적용
프로젝트(icons/talmocom/gamblescan/tshome)는 *다음 `sync` 전까지* 옛
동작을 유지. 반복 목격:

- 2026-05-12 METH-015 전파 (F-001, F-003)
- 2026-05-13 dashboard 포트 충돌 fix — 3 프로젝트 옛 코드 (F-003)
- 2026-05-13 multi-dashboard (F-005)
- 2026-05-15~17 정합성 QA 4건 — 4 프로젝트 sync 전까지 미반영, pre-push
  hook 도 옛 버전(50_tools 하드코딩)이라 우연히 skip

N≥7 — 패턴 확정.

## 근본 원인 (Root Cause)

적용 프로젝트는 sync 시점의 `60_tools/methodology.py` *스냅샷* 을 보유.
본 저장소의 후속 fix 는 push 만으로 전파되지 않는다 (git 의존성이 아니라
파일 복사 모델). 게다가 `.git/hooks/` 는 git 추적 대상이 아니라
`hooks install` 을 재실행하지 않으면 옛 hook 이 그대로 남는다.

## 솔루션 (Solution)

1. **시급한 fix 는 본 저장소 절대경로 CLI 직접 호출** (sync 안 기다림):
   ```sh
   python3 /path/to/methodology/60_tools/methodology.py <cmd> --path <project>
   ```
2. **정기 전파**: fix 누적 후 `methodology sync --apply --include-worktrees`
   (PR #19 가드로 stale worktree 자동 skip)
3. **hook 재설치 의무화**: sync 후 적용 프로젝트에서 1회
   `methodology hooks install --force` (옛 하드코딩 hook 교체)

## 안티패턴 (Anti-Pattern)

- fix push 후 적용 프로젝트가 자동으로 받을 거라 가정
- sync 없이 적용 프로젝트의 옛 CLI 로 디버깅 (재현 안 됨 → 시간 낭비)
- 옛 hook 의 *우연한* skip 에 의존 (3-tier fallback 전까지 50_tools
  하드코딩 hook 이 v4.0 프로젝트에서 검증 전체 skip — 안전망 무력화)

## 솔루션 후보 (장기)

- `methodology <cmd> --use-upstream` — 적용 프로젝트에서도 본 저장소 CLI
  강제 사용 (스냅샷 무시)
- 또는 적용 프로젝트가 `60_tools/methodology.py` 를 symlink (단일 출처)
- sync 흐름에 `hooks install --force` 자동 포함

(METH-020 acceptance — N≥4 확인 완료, 솔루션 후보 명문화)

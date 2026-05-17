# ADR-002: 메타-방법론(`70_meta/`) 격리 — 적용 프로젝트 비주입 원칙

## Status

accepted

## Date

2026-05-17

## Context

본 저장소(`ai-pipeline-methodology`)는 두 종류의 자산을 동시에 보유한다:

1. **방법론 자산** — 적용 프로젝트에 *주입되어야* 하는 것
   (`20_guides/`, `50_resources/templates|prompts`, `60_tools/methodology.py`,
   `_start/`, managed `CLAUDE.md`/`AGENTS.md` 등)
2. **메타-방법론 자산** — 방법론 *자체의 운영·개선* 기록.
   적용 프로젝트에 절대 새어나가면 안 되는 것
   (`70_meta/observations`, `70_meta/catalog` MC-NNN, `70_meta/rfc`,
   `70_meta/retrospectives`, `70_meta/experiments`)

메타 자산이 적용 프로젝트로 새면: (a) 외주 인계 시 방법론 내부 사정 유출,
(b) 적용 프로젝트 AI 가 메타 카탈로그를 자기 도메인 카탈로그로 오인,
(c) `methodology export` 의 "방법론 흔적 0" 보증 붕괴.

RFC-001 은 본래 이 격리 결정을 위해 작성됐으나 `status` upstream-commit
검출 개선 용도로 *재사용*됐다(2026-05-12 accepted). 격리 결정 자체는
문서화되지 않은 채 코드/MANIFEST 에 암묵적으로만 존재했다. 격리가 여러
번 깨질 뻔한 사건(PR #14 applied-ci 가 source 에서 70_meta 검사 fail,
QA-1 에서 70_meta 누수 점검) 을 거치며 *명시적 구조 결정* 의 필요가
확인됐다.

## Decision

`70_meta/` 는 **이중 안전망** 으로 적용 프로젝트 비주입을 강제한다:

1. **MANIFEST `excluded_paths`** — `methodology.py` 의 sync/init 이
   `70_meta` 를 절대 복사 대상에 넣지 않음. `assert_excluded_paths_safe()`
   가 주입 목록에 격리 경로가 섞였는지 매 실행 검증.
2. **`manifest-check` CLI** — 적용 프로젝트에 `70_meta`(또는 v3.2
   `60_meta`)가 존재하면 즉시 실패. pre-push hook·source-ci·applied-ci
   가 호출.

부수 규칙:

- `methodology-applied-ci.yml` 은 source 저장소(`github.repository ==
  YunJuniverse/ai-pipeline-methodology`)에서 **job-level skip** — source 는
  70_meta 를 *의도적으로* 보유하므로 격리 검사가 항상 fail (PR #14).
  source 자체 검증은 `methodology-source-ci.yml` 가 담당.
- `methodology export` 는 NN_ 방법론 폴더 전체 + `_start`/`.ai` 제외 후
  복사하고, 결과 재-walk 로 "방법론 흔적 잔존 0" 을 이중 검증.
- 메타 카탈로그 ID 는 `MC-NNN` (도메인 카탈로그 `C-NNN` 와 구분),
  `domain: meta-methodology` 고정.

## Impact Scope

- `60_tools/methodology.py` — `MANIFEST["excluded_paths"]`,
  `assert_excluded_paths_safe()`, `cmd_manifest_check`
- `.github/workflows/methodology-{source,applied}-ci.yml`
- `methodology export` 제외 목록·이중 검증
- `70_meta/_README.md` §2 (이중 안전망 서술) — 본 ADR 이 근거
- 향후 신규 메타 하위폴더 추가 시 자동으로 격리 대상

## Rollback Plan

격리 자체는 비활성화하지 않는다(보안·정합성 핵심). 만약 특정 메타
하위폴더를 *의도적으로* 적용 프로젝트에 노출해야 한다면, 해당 경로만
`excluded_paths` 에서 제외하고 MANIFEST `shared_paths` 로 명시 이동 +
본 ADR 에 supersede 기록. `excluded_paths` 전체 제거나
`manifest-check` 무력화는 금지 — `methodology export` 보증과 직결.

## Notes

- RFC-001 은 status 용도로 소진됨 → 본 ADR 이 격리 결정의 단일 출처.
- 관련 마찰 기록: `70_meta/observations/2026-05-15_applied-ci-source-repo-skip.md`,
  QA 리포트(2026-05-17 정합성 점검 18 카테고리).

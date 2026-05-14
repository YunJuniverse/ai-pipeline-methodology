# 70_meta/observations/ — 메타-운영 관찰 (L1, 본 저장소 한정)

> 본 저장소 운영 중 AI가 자동 기록하는 *방법론 자체에 대한* 관찰.
> 외부 프로젝트 도메인 작업 관찰은 `50_resources/ai_observations/` 에.

## 차이점 (가장 흔한 혼동)

| 디렉터리 | 대상 |
|---|---|
| `50_resources/ai_observations/` | 외부 프로젝트 도메인 작업 (예: webapp-next 기능 구현 중 마찰) |
| **`70_meta/observations/`** (본 폴더) | **본 저장소의 방법론 운영 작업** (예: RFC 작성 중 마찰, 백서 부록 검색 비효율) |

판정 기준: **"이 마찰이 외부 프로젝트에서도 발생할 수 있는가?"** Yes → 도메인 / No (본 저장소만 발생) → 메타.

## 파일명·스키마

[`20_guides/03_AI_관찰_로그_작성_규칙.md`](../../20_guides/03_AI_관찰_로그_작성_규칙.md) 와 **동일**. 단:
- `domain` 필드는 `meta-methodology` 고정
- `task_type` 에 `rfc` / `retrospective` / `experiment` 추가 가능

## 운영 규칙

도메인 관찰 규칙과 동일:
- AI가 자동 기록, 사용자 수정 금지
- 절대 삭제 금지
- 칭찬·서술·요약 금지 — 사실과 시간 비용만

# 데이터 모델 (Data Model) — 템플릿

> 용도: 엔티티·필드·관계·무결성·마이그레이션 명세. 기획 산출물 하류의 개발명세. 지침 `20_guides/18_개발_마스터_플랜_작성_지침.md` §18.5 참조.
> **Class B 직결**: DB migration/schema 변경은 CLAUDE.md §3 Class B — impact scope·rollback을 이 문서가 선제 충족.

| 항목 | 내용 |
|------|------|
| 버전 / 작성일 / Status | |
| 기반 문서 (상류) | |
| 범위 (Phase/Sprint) | |

## 1. Entity List

| Entity | 목적 | Owner(도메인) |
|---|---|---|
| | | |

## 2. Fields (엔티티별)

### <Entity 명>

| Field | Type | Required(Y/N) | Description (default값 인라인) |
|---|---|---|---|
| | | | |

## 3. Relationships

| From | To | Type (1:1 / N:1 / N:M) | Notes |
|---|---|---|---|
| | | | |

## 4. Integrity Rules
- (이력 보존: 변경은 *시점부터* 적용, 과거 기록은 당시 값 스냅샷 — 지침 11 §19.3)
-

## 5. Privacy / Security
- (개인정보 필드·암호화·접근 제한)
-

## 6. Migration Impact
- 초기 테이블 / 추가 테이블 / 확장 필드:
- Pending Migrations (직접 실행 필요):
- Backfill needs (시드 데이터 N개):

## Change Log

| Version | Date | Changed Because |
|---|---|---|
| | | |

**원칙**: 정의(스키마)와 적용(migration/backfill)을 한 문서에서 분리하되 연결. 차기 Phase 확장 필드는 default값과 함께 미리 박아둔다.

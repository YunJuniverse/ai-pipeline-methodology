# 기능 명세 (Functional Spec) — 템플릿

> 용도: 요구사항(`requirements-spec.md`) 하류의 *구현 단위* 기능 명세 — 기능 ID 추적 + 비즈니스 규칙·권한·예외 분리. 지침 `20_guides/11_서비스기획서_작성_지침.md` §19.2(⑦) · `20_guides/18_개발_마스터_플랜_작성_지침.md` §18.5 참조.

| 항목 | 내용 |
|------|------|
| 버전 / 작성일 / Status | |
| 기반 문서 (상류) | |
| 범위 (Phase/Sprint) | |

## 1. Functions (영역별 그룹)

| FS-ID | 기능명 | 설명 | Input | Output | 우선순위 |
|---|---|---|---|---|---|
| FS-01 | | | | | |

## 2. Business Rules

| Rule ID | 규칙 | Applies To (FS-ID 역참조) |
|---|---|---|
| BR-01 | | |

## 3. Permissions

| Actor | Allowed | Restricted |
|---|---|---|
| | | |

## 4. Exception Handling
- **레이어별 에러 처리 규약**: application 레이어=throw / page=catch & 사용자 메시지 / component=props로 상태 수신 (production console.log 금지, 경계 에러 정규화 — CLAUDE.md §7).
- 상황별 동작:

| 상황 | 사용자에게 보이는 동작 |
|---|---|
| | |

## 5. Out of Scope (차기 Phase 예고)
- (지금 안 만드는 것 + 진입 조건)

## Change Log

| Version | Date | Changed Because |
|---|---|---|
| | | |

**원칙**: 기능표(FS-ID)와 별개로 Business Rules(역참조)·Permissions 매트릭스·Exception을 *분리*. 안정 ID로 상류 요구(requirements-spec)와 하류 코드를 양방향 추적.

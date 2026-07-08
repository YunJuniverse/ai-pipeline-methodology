# API·인터페이스 계약 (API Contract) — 템플릿

> 용도: **시스템 인터페이스 계약** — 개발리드가 개발자(특히 프론트/백엔드 병렬 작업)에게 던지는 핵심 조율물. `functional-spec.md`(기능 *단위* 입출력)의 상위 *시스템 레벨* 계약이며, 엔드포인트·요청/응답·에러·버전·인증을 못 박아 병렬 개발의 단일 진실로 삼는다.
> 기계판독 우선: 지침 `20_guides/00_AI_기획_프로젝트_운영_원칙.md` §2.5~2.8(자연어 + OpenAPI 등 기계판독). 사람 개발자 인계 시 매체 규칙은 지침 `20_guides/09_기획_핸드오프_재포맷_규칙.md`. 작성 위치·읽는 순서는 지침 `20_guides/21_개발명세_작성_지침.md`.
> 상태: 이 문서가 코드/OpenAPI와 어긋나면 **기계판독 스펙(OpenAPI)을 진실로 따른다** — 본 마크다운은 사람용 요약·근거.

| 항목 | 내용 |
|------|------|
| 버전 / 작성일 / Status | (예: v1.0 / YYYY-MM-DD / Draft) |
| 기반 문서 (상류) | `requirements-spec` · `functional-spec` · `data-model` |
| 기계판독 스펙 (정본) | (예: `docs/openapi.yaml` — 있으면 본 문서보다 우선) |
| Base URL / 환경 | (예: `https://api.example.com/v1` · dev/stg/prod) |
| 인증 방식 | (예: Bearer JWT · API Key · OAuth2 — 헤더·만료·갱신) |

---

## 1. 리소스·엔드포인트 목록

> 한눈에 보는 계약 표. 상세는 §2. **담당(프론트 소비/백엔드 제공)**을 명시해 병렬 작업 소유를 못 박는다.

| ID | Method | Path | 용도 | Auth | 상류 FS-ID | 제공(BE) | 소비(FE) | Status |
|----|--------|------|------|:----:|-----------|----------|----------|--------|
| API-001 | POST | `/auth/login` | 로그인 | ✗ | FS-012 | | | Draft |
| API-002 | GET | `/orders?status=` | 주문 목록 | ✓ | FS-031 | | | Draft |

---

## 2. 엔드포인트 상세

> 엔드포인트 1개당 블록 1개. 요청/응답은 **예시 + 스키마**를 함께. 스키마 타입은 §4 공유 스키마를 참조(정의 중복 금지).

### API-002 · GET `/orders`
- **용도 / 상류**: 주문 목록 조회 / FS-031
- **인증·권한**: Bearer JWT · 정회원 이상 (본인 주문만)
- **요청**
  - Query: `status` (enum: `pending|paid|shipped`, optional), `page` (int, default 1), `size` (int, default 20, max 100)
- **응답 200**
  ```json
  { "items": [ /* Order[] — §4 참조 */ ], "page": 1, "size": 20, "total": 137 }
  ```
- **에러**: 401(미인증) · 403(타인 주문) · 422(잘못된 status enum) — 포맷은 §3.1
- **비고**: 정렬 기본 `created_at desc`. rate limit §3.3.

---

## 3. 공통 규약 (전 엔드포인트)

### 3.1 에러 포맷 (단일 형태)
```json
{ "error": { "code": "INVALID_STATUS", "message": "status must be one of ...", "field": "status" } }
```
> `code`는 기계 분기용(안정적 enum), `message`는 사람용. 클라이언트는 **`code`로만 분기**한다(문구 변경에 깨지지 않게).

### 3.2 상태 코드 규약
| 코드 | 의미 | 사용 규칙 |
|------|------|-----------|
| 200 / 201 | 성공 / 생성됨 | 201은 리소스 생성 시 `Location` 헤더 포함 |
| 400 / 422 | 잘못된 요청 / 검증 실패 | 파싱 실패=400, 값 규칙 위반=422 |
| 401 / 403 | 미인증 / 권한없음 | 토큰 부재/만료=401, 권한 부족=403 |
| 404 / 409 | 없음 / 충돌 | 멱등 충돌·중복 생성=409 |
| 429 / 5xx | rate limit / 서버오류 | 429는 `Retry-After` 포함 |

### 3.3 공통 정책
- **페이지네이션**: `page`/`size` (또는 cursor) — 프로젝트 하나로 통일.
- **정렬·필터**: `sort=field,-field` 규칙.
- **Rate limit**: (예: 인증 60 req/min, 공개 20 req/min) — 초과 시 429 + `Retry-After`.
- **Idempotency**: 결제·생성 등은 `Idempotency-Key` 헤더 (§ data/auth 리스크 — PR에 명시).

### 3.4 버전·호환 정책
- URL 버전(`/v1`) — **breaking change는 새 버전**, 하위호환 변경만 in-place.
- Deprecation: 헤더 `Deprecation`/`Sunset` + 마이그레이션 노트 링크. (지침 05 예외군 = 버전드 API 문서)

---

## 4. 공유 스키마 (타입 단일 정의)

> `data-model.md` 엔티티와 **1:1로 링크**하고 여기서 정의를 반복하지 않는다 — 전송 형태(직렬화·숨김 필드·파생 필드)만 명시.

| 스키마 | data-model 엔티티 | 전송 시 차이 (숨김/파생/직렬화) |
|--------|-------------------|----------------------------------|
| `Order` | Order | `internal_memo` 숨김 · `total_krw` 파생 · 금액=정수(원) |
| `User` | User | `password_hash` 숨김 · `role` enum 노출 |

---

## 5. 미해결 계약 질문 (Open)

> 사람 개발자 인계 시 **빈틈을 0으로 닫지 말고 여기 남긴다**(지침 09 — 소통 계약·생산적 마찰). BE/FE가 계약 확정 전 합의할 항목.

| ID | 질문 | 관련 API | 결정 필요 시점 | 상태 |
|----|------|----------|----------------|------|
| Q-1 | 목록 페이지네이션 cursor vs offset | API-002 | FE 착수 전 | Open |

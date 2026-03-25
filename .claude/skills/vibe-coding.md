---
name: vibe-coding
description: Stage 4 구현 워크플로우 — 4-레이어 아키텍처, TDG 루프, 멱등성 체크리스트, 린터 설정. "구현", "코딩", "개발", "기능 만들어", "API", "컴포넌트" 등 개발 키워드 시 활성화.
---

# 바이브코딩 구현 가이드 (Stage 4)

## 전제 조건

- `docs/spec.md` (Product Spec)가 존재해야 한다
- spec.md가 PRD 역할을 겸한다 — 별도 CPS/PRD 작성 불필요
- spec.md가 없으면 Stage 2부터 시작하도록 안내한다

---

## 구현 순서 (TDG 루프)

매 기능 구현 시 아래 순서를 반복한다:

```
1. spec.md에서 해당 기능 요구사항 확인
2. 도메인 타입/인터페이스 정의 (/domain)
3. 유스케이스 테스트 작성 (/application)
4. 유스케이스 구현 (/application)
5. 인프라 구현 (/infrastructure)
6. 인터페이스 구현 (/interface)
7. 통합 테스트
8. 린터 통과 확인
9. 커밋 (컨벤션 형식)
```

> 테스트 → 구현 → 린터 → 커밋. 이 순서를 깨지 않는다.

---

## 4-레이어 아키텍처

```
/src
  /domain          # 순수 비즈니스 로직 — 외부 의존 없음
  /application     # 유스케이스, 서비스 조합
  /infrastructure  # DB, 외부 API, 파일 I/O
  /interface       # HTTP 핸들러, CLI, 웹소켓
  /shared          # 공통 타입, 유틸, 상수
```

### 레이어 의존성

```
interface ──→ application ──→ domain
                    ↑
             infrastructure
```

| 레이어 | 가능한 import | 금지된 import |
|--------|-------------|-------------|
| `domain` | `shared`만 | 나머지 모두 |
| `application` | `domain`, `shared` | `infrastructure`, `interface` |
| `infrastructure` | `domain`, `application/ports`, `shared` | `interface` |
| `interface` | `application`, `shared` | `domain`, `infrastructure` |

> 역방향 import 절대 금지

---

## 파일 네이밍

| 종류 | 패턴 | 예시 |
|------|------|------|
| 도메인 엔티티 | `[name].ts` | `user.ts` |
| 유스케이스 | `[name].usecase.ts` | `create-user.usecase.ts` |
| 레포지토리 | `[name].repository.ts` | `user.repository.ts` |
| 라우터 | `[name].router.ts` | `users.router.ts` |
| 핸들러 | `[name].handler.ts` | `users.handler.ts` |
| 테스트 | `[name].test.ts` | `create-user.usecase.test.ts` |
| 포트 | `[name].port.ts` | `user-repo.port.ts` |
| 인덱스 | `index.ts` | barrel export |

**금지 패턴**: `userList.ts`, `userDetail.ts`, `userManager.ts`, `userHelper.ts`

---

## 멱등성 체크리스트 (매 구현 전 확인)

```
[ ] 이 파일이 이미 존재하는가 (덮어쓰기 전 확인)
[ ] 이 함수가 이미 비슷한 곳에 있는가 (중복 생성 방지)
[ ] DB 삽입은 upsert인가 (insert 단독 금지)
[ ] 환경변수 처리가 되어 있는가
[ ] 에러 핸들링이 포함되어 있는가
```

---

## 린터 핵심 규칙

| 규칙 | 설정 | 목적 |
|------|------|------|
| `@typescript-eslint/no-explicit-any` | error | any 타입 금지 |
| `@typescript-eslint/naming-convention` | error | 네이밍 컨벤션 강제 |
| `import/order` | error | import 순서 고정 |
| `import/no-cycle` | error | 순환 참조 금지 |
| `max-depth` | error (3) | 중첩 깊이 제한 |
| `no-console` | warn | console.log 경고 |
| `import/no-restricted-paths` | error | 레이어 경계 강제 |

---

## Git 훅 3단계

- **pre-commit**: 린터 → 타입체크 → console.log 검사
- **commit-msg**: `feat/fix/refactor/docs/test/chore` 형식 검사
- **pre-push**: 테스트 전체 실행

> 커밋 시 린터 실패 → "린터 에러 고쳐줘" → 재커밋. 이 루프가 Normal Form 수렴의 핵심.

---

## 프로젝트 유형별 변형

### 웹 앱 / 대시보드
```
interface/ → http/ + views/
```

### 자동화 / 백엔드 API
```
interface/ → http/ + jobs/
```

### AI 에이전트 / 챗봇
```
domain/ → conversation/ + tools/
infrastructure/ → llm/ + memory/
interface/ → bot/
```

### 풀스택 서비스 (모노레포)
```
apps/ → web/ + api/
packages/ → shared/
```

---

## 주기적 유지보수

- 기능 세션과 리팩토링 세션 **분리** (같은 날 섞지 않기)
- 리팩토링 전 "분석만 해줘, 수정 금지" 프롬프트 사용
- 주요 결정은 CLAUDE.md ADR 로그에 기록
- CLAUDE.md "현재 상태" 섹션 업데이트

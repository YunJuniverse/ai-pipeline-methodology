# ARCHITECTURE.md

---

## 전체 구조

```
[PROJECT_ROOT]/
│
├── CLAUDE.md                    # ← AI 컨텍스트 앵커 (필수)
├── .eslintrc.json               # ← 하네스 린터 규칙
├── .gitignore
├── package.json
├── tsconfig.json
│
├── docs/
│   ├── CPS_TEMPLATE.md
│   ├── PRD_TEMPLATE.md
│   └── adr/
│       ├── ADR_TEMPLATE.md
│       └── 001-[결정명].md
│
├── scripts/
│   └── setup-hooks.js
│
└── src/
    ├── domain/          # 순수 비즈니스 로직
    │   ├── [entity]/
    │   │   ├── [entity].ts
    │   │   ├── [entity].test.ts
    │   │   └── index.ts
    │   └── shared/
    │       ├── errors.ts
    │       └── value-objects.ts
    │
    ├── application/     # 유스케이스
    │   ├── [feature]/
    │   │   ├── [feature].usecase.ts
    │   │   ├── [feature].usecase.test.ts
    │   │   └── index.ts
    │   └── ports/
    │       └── [repo].port.ts
    │
    ├── infrastructure/  # 외부 시스템 구현
    │   ├── db/
    │   ├── external/
    │   └── config/
    │       └── env.ts
    │
    ├── interface/       # 진입점
    │   ├── http/
    │   ├── cli/
    │   └── websocket/
    │
    └── shared/          # 공통 유틸
        ├── types/
        ├── utils/
        └── constants/
```

---

## 레이어 의존성 규칙

```
interface ──→ application ──→ domain
                    ↑
             infrastructure
```

| 레이어 | 가능한 import | 금지된 import |
| --- | --- | --- |
| `domain` | `shared`만 | 나머지 모두 |
| `application` | `domain`, `shared` | `infrastructure`, `interface` |
| `infrastructure` | `domain`, `application/ports`, `shared` | `interface` |
| `interface` | `application`, `shared` | `domain`, `infrastructure` |

---

## 파일 네이밍 규칙

| 파일 종류 | 패턴 | 예시 |
| --- | --- | --- |
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

## 프로젝트 유형별 변형

### 웹 앱 / 대시보드

```
interface/
  └── http/         # REST API
  └── views/        # SSR 템플릿
```

### 자동화 / 백엔드 API

```
interface/
  └── http/         # REST/GraphQL
  └── jobs/         # 크론잡, 큐 워커
```

### AI 에이전트 / 챗봇

```
domain/
  └── conversation/ # 대화 상태, 메시지 타입
  └── tools/        # 에이전트 툴 정의

infrastructure/
  └── llm/          # LLM 클라이언트
  └── memory/       # 벡터 DB, 메모리 스토어

interface/
  └── bot/          # Telegram, Slack, Discord 핸들러
```

### 풀스택 서비스

```
apps/
  ├── web/          # 프론트엔드
  └── api/          # 백엔드 API
packages/
  └── shared/       # 공통 타입 (모노레포)
```
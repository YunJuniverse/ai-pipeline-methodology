# ⬡ Harness Engineering 템플릿

AI 바이브코딩 시 멱등성과 일관성을 유지하기 위한 하네스 엔지니어링 방법론 문서 모음입니다.

> **규칙**: 이 프로젝트의 모든 문서는 `.md` 기준으로 작성합니다. (ADR-001)
> 

---

## 📁 파일 목록

| 파일 | 역할 | 사용 시점 |
| --- | --- | --- |
| HARNESS_TEMPLATE | 전체 방법론 가이드 | 처음 읽기 |
| [CLAUDE.md](http://CLAUDE.md) | AI 컨텍스트 앵커 | 프로젝트 루트에 복사 |
| CPS_TEMPLATE | 기능 기획 문서 | 기능 개발 시작 전 |
| PRD_TEMPLATE | 기술 요구사항 문서 | CPS 확정 후 |
| ARCHITECTURE | 폴더 구조 레퍼런스 | 아키텍처 합의 시 |
| ADR_TEMPLATE | 아키텍처 결정 기록 | 주요 결정 시 |

---

## 🚀 새 프로젝트 시작 체크리스트

- [ ]  `CLAUDE.md` → 프로젝트 루트에 복사 후 `[PROJECT_NAME]` 채우기
- [ ]  `.eslintrc.json` → 프로젝트 루트에 복사
- [ ]  `scripts/setup-hooks.js` 실행하여 Git 훅 설치
- [ ]  `docs/` 폴더 생성 후 첫 번째 CPS 문서 작성
- [ ]  `src/` 4-레이어 폴더 구조 생성

---

## 🔄 기능 개발 루프 (매번)

```
[CPS 문서 작성]
     ↓
[PRD 구체화]
     ↓
[세션 시작 프롬프트로 Claude 로딩]
     ↓
[테스트 케이스 먼저 작성 요청]
     ↓
[구현 요청 — 레이어 명시]
     ↓
[린터 통과 확인]
     ↓
[Git Commit — 컨벤션 형식]
```

---

## 📌 핵심 원칙

> AI는 빠른 손, 하네스는 그 손이 항상 같은 글씨를 쓰게 만드는 틀
> 

[HARNESS_[TEMPLATE.md](http://TEMPLATE.md)](%E2%AC%A1%20Harness%20Engineering%20%ED%85%9C%ED%94%8C%EB%A6%BF/HARNESS_TEMPLATE%20md%2032e1a2ebe06a81c7ab61d6551edc6a20.md)

[[CLAUDE.md](http://CLAUDE.md)](%E2%AC%A1%20Harness%20Engineering%20%ED%85%9C%ED%94%8C%EB%A6%BF/CLAUDE%20md%2032e1a2ebe06a81388dd2c06a8ce7fc82.md)

[CPS_[TEMPLATE.md](http://TEMPLATE.md)](%E2%AC%A1%20Harness%20Engineering%20%ED%85%9C%ED%94%8C%EB%A6%BF/CPS_TEMPLATE%20md%2032e1a2ebe06a81298da7dd40538f75f3.md)

[PRD_[TEMPLATE.md](http://TEMPLATE.md)](%E2%AC%A1%20Harness%20Engineering%20%ED%85%9C%ED%94%8C%EB%A6%BF/PRD_TEMPLATE%20md%2032e1a2ebe06a816c8d61d22e00da47c2.md)

[[ARCHITECTURE.md](http://ARCHITECTURE.md)](%E2%AC%A1%20Harness%20Engineering%20%ED%85%9C%ED%94%8C%EB%A6%BF/ARCHITECTURE%20md%2032e1a2ebe06a8118bacbdadb1626d526.md)

[ADR_[TEMPLATE.md](http://TEMPLATE.md)](%E2%AC%A1%20Harness%20Engineering%20%ED%85%9C%ED%94%8C%EB%A6%BF/ADR_TEMPLATE%20md%2032e1a2ebe06a819b8355cd5109d9ec61.md)
# AI Relay Workflow Guide

## 개요

여러 AI 앱(Claude, ChatGPT, GenSpark 등)을 **md 파일 기반으로 릴레이**하여, 각 AI의 강점을 결합하는 워크플로우 시스템.

- **API 코딩 없음** — 데스크탑/웹 AI 앱만 사용
- **md 파일이 공유 메모리** — 산출물과 맥락을 md로 저장하고 다음 AI에 전달
- **프로젝트 시작은 항상 Claude**

---

## 핵심 설계 원칙

### 1. 컨텍스트 유실 방지: 압축 핸드오프 전략

매 릴레이 단계에서 두 종류의 md 파일을 생성한다:

| 파일 종류 | 역할 | 예시 |
|-----------|------|------|
| **산출물 파일** | 실제 결과물 (기획서, 리뷰, 코드 등) | `01_claude_draft_v1.md` |
| **핸드오프 파일** | 맥락 요약 + 다음 AI 지시서 | `01_handoff_v1.md` |

> **다음 AI에게는 핸드오프 파일 + 최신 산출물만 전달한다.**  
> 이전 라운드의 산출물은 넘기지 않는다. 핸드오프 파일이 누적 맥락을 압축 보관한다.

### 2. 마찰 최소화

- **프롬프트 표준화**: 거의 모든 단계에서 동일한 표준 프롬프트 사용
- **공유 폴더 구조**: 프로젝트별 통일된 폴더에서 파일 관리

### 3. AI별 역할 배분

- **빌더와 리뷰어는 반드시 다른 AI** (자기 편향 방지)
- **고정 역할** (초안 작성, 수정 빌드) + **유동 슬롯** (리뷰, 리서치, 시각화)
- 역할 배분은 프로젝트마다 릴레이 설계서에서 정의

### 4. OPEN ISSUES 관리

- AI가 매 단계 끝에 이슈 상태를 업데이트하고 추천 (CLOSE/이월/신규)
- 사용자가 릴레이 사이에 30초 검수 후 최종 결정

---

## 폴더 구조

```
~/ai-relay/
├── _templates/              # 재사용 템플릿
│   ├── handoff_template.md
│   ├── relay_plan_template.md
│   └── standard_prompt.md
│
└── {project-name}/          # 프로젝트별 폴더
    ├── 00_relay_plan.md     # 릴레이 설계서
    ├── 01_claude_draft_v1.md
    ├── 01_handoff_v1.md
    ├── 02_gpt_review_v1.md
    ├── 02_handoff_v2.md
    ├── 03_claude_draft_v2.md
    ├── 03_handoff_v3.md
    └── ...
```

### 파일 네이밍 규칙

```
{순번}_{AI이름}_{역할}_{버전}.md
```

- 순번: 릴레이 순서 (01, 02, 03...)
- AI이름: claude, gpt, genspark 등
- 역할: draft, review, research, ppt 등
- 버전: v1, v2, v3...

---

## 릴레이 실행 흐름

```
1. 릴레이 설계서 작성 (Claude)
2. Claude 작업 → 산출물 md + 핸드오프 md 저장
3. OPEN ISSUES 검수 (30초, 사용자)
4. 다음 AI에 핸드오프 + 산출물 첨부 + 표준 프롬프트
5. 다음 AI 작업 → 산출물 md + 핸드오프 md 저장
6. 반복...
```

---

## 확장 시나리오

이 시스템은 산출물 파일 타입과 릴레이 설계서만 바꾸면 다양한 시나리오에 적용 가능:

| 시나리오 | 릴레이 흐름 | 산출물 타입 |
|----------|------------|------------|
| 기획서 | Claude→ChatGPT→Claude→GenSpark | md, pptx |
| 블로그/리뷰 | Claude→ChatGPT→Claude | md |
| 투자 리서치 | Claude→GenSpark→Claude→ChatGPT→Claude | md |
| 바이브 코딩 | Claude→ChatGPT→Claude | md, 코드 파일 |
| 프레젠테이션 | Claude→ChatGPT→GenSpark→Claude | md, pptx |

> **모든 시나리오에서 프로젝트 시작은 항상 Claude.**

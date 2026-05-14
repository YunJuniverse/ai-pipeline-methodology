---
doc_id: briefs-readme
title: 00_briefs/ — 인간 입력 (브리프·리서치·아이디어·회의록)
version: v1.0.0
status: active
last_updated: 2026-05-14
ai_relevance: rule
---

# 00_briefs/ — 인간 입력 공간

> **사용자가 raw 메모·기획·리서치를 던지면, AI 가 매 세션·필요 시 다시 읽고 반영한다.**
> 위상: 모든 작업의 *출발점*. 백서 §3-G1 단일 진입점.

---

## 1. 무엇을 넣는가

| 종류 | 예시 |
|---|---|
| **아이디어 노트** | "사용자 onboarding 단순화 해보면 어떨까" |
| **리서치 결과** | 시장 분석·경쟁사 조사·기술 문서 요약 |
| **회의록** | 사용자 인터뷰·내부 회의 내용 |
| **참고 자료 링크** | URL·PDF 경로 (raw 인용 OK) |
| **방향성 선언** | "이번 분기는 X 에 집중" |

→ *정형 산출물* 은 아님. **raw·자유 형식 OK**. AI 가 읽고 *기획서·개발 산출물* 로 변환.

## 2. 어디에 넣는가

```
00_briefs/
├── _README.md              ← 본 문서
├── current/                ← 활성 브리프 (AI 가 매 세션 읽음)
│   ├── YYYY-MM-DD_<topic>.md
│   └── ...
├── archived/               ← 옛 브리프 (참고용 보관)
└── meetings/               ← 회의록 (선택)
    └── YYYY-MM-DD_<topic>.md
```

**파일명 컨벤션**: `YYYY-MM-DD_<topic-slug>.md` — 시간 순 자동 정렬.

## 3. AI 가 언제 읽는가

| 시점 | 동작 |
|---|---|
| **매 세션 시작** | `.ai/context.json` `must_read_optional` 에 `00_briefs/current/*.md` 자동 포함 |
| **사용자 요청 시** | "브리프 다시 봐줘" → AI 가 `current/` 전체 재로드 |
| **자동 트리거 (향후)** | brief 파일 mtime 변경 감지 → 다음 세션에 highlight |

## 4. 갱신 패턴

- 인간이 *수시로* `current/` 에 새 파일 추가 또는 기존 파일 수정
- 일정 기간 후 (인간 판단) `archived/` 로 이동
- *삭제 금지* — 옛 맥락도 학습 데이터

## 5. AI 측 규칙 (CLAUDE.md / AGENTS.md 반영)

- **세션 부팅 시** must_read 로 `current/*.md` 일별 정렬 후 *전부 읽음*
- 작업 진행 중 *그 브리프 내용을 어떻게 반영했는지* 명시 (예: "TALMOCOM-042 는 2026-05-14_onboarding.md 의 §3 반영")
- *옛 브리프와 충돌* 발생 시 사용자에게 확인 — 자동 결정 금지

## 6. 안티패턴

- ❌ 정형 산출물을 brief 에 넣음 — `30_planning/` 또는 `40_dev/` 로
- ❌ 비밀번호·API 키 — `.env` 또는 secret manager 사용
- ❌ 너무 길게 — 1 파일 200줄 이내 권장 (긴 리서치는 `40_dev/snapshots/` 또는 외부 링크)
- ❌ archived 삭제 — 학습 데이터 손실

## 7. 첫 시드

신규 프로젝트면 `current/` 비어있음. 사용자가 첫 브리프 1장 던지면 AI 가 그걸 baseline 으로 작업 시작.

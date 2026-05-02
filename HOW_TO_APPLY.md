# How To Apply

> 이 방법론을 새 프로젝트에 붙이는 실무 절차.

---

## 0. 전체 흐름 한눈에

```
briefs/ (자료 준비)
    │
    ▼ Phase 0: 초기화
    │
    ▼ Phase 1: 6종 기획서 작성 (사업·서비스·운영·마케팅·브랜드·PM)
    │            ↕ 재기획 시 briefs/updates/ 에 파일 추가 → re-plan
    ▼ 🔒 Gate 1: 사람 6종 검토 + 승인
    │
    ▼ Phase 2: 개발명세서 작성
    ▼ 🔒 Gate 2: 사람 검토 + 승인
    │
    ▼ Phase 3: TODO.md 분해 → 개발 루프
               Class A → PR
               Class B → 근거 포함 PR
               Class C → ADR/issue 승인 후 PR
               각 PR → 🔒 Gate 3+: merge
```

---

## 1. Mode 선택

| Mode | 언제 | 코드 폴더 |
|------|------|-----------|
| `fullstack` | 구현까지 진행 | `src/`, `tests/` 생성 |
| `planning-only` | 기획 산출물만 필요 | 없음 |

---

## 2. 프로젝트 초기화

```bash
METHODOLOGY="/Users/hayden/Library/Mobile Documents/iCloud~md~obsidian/Documents/methodology"
cd ~/Projects
bash "$METHODOLOGY/init-project.sh" my-project --type fullstack
```

생성 결과:

```
my-project/
├── CLAUDE.md
├── AGENTS.md
├── HANDOFF.md
├── TODO.md
├── generate-dashboard.py
├── briefs/                        ← 초기 기획 자료
│   └── updates/                   ← 개발 중 추가 아이디어
├── .github/PULL_REQUEST_TEMPLATE.md
├── docs/
│   ├── guides/planning/           ← 6종 기획서 작성 지침 (참조용)
│   ├── adr/
│   └── snapshots/
│       ├── plans/
│       │   ├── business/          ← 사업기획서 v1, v2, ...
│       │   ├── service/
│       │   ├── ops/
│       │   ├── marketing/
│       │   ├── brand/
│       │   └── pm/
│       └── dev-specs/             ← 개발명세서 v1, v2, ...
├── src/        # fullstack만
└── tests/      # fullstack만
```

---

## 3. Briefs 준비

`briefs/` 에 기획 자료를 넣는다.

- 아이디어 노트 (`.md`, `.txt`)
- 초안 기획서, 사업계획서 초안 (`.pdf`, `.md`)
- 사용자 리서치, 경쟁사 분석 메모 등

AI는 이 파일을 **읽기만 하고 수정하지 않는다.**
개발 중 새 아이디어가 생기면 `briefs/updates/YYYY-MM-DD-제목.md` 로 추가한다.

---

## 4. Project Settings 채우기

첫 세션에서 아래 값을 채운다.

- project name
- objective
- mode
- stack
- primary approver
- release policy

`CLAUDE.md`와 `AGENTS.md` 상단에 들어간다.

---

## 5. 세션 리듬

### Phase 0: 초기화

[KICKOFF_PROMPT.md](KICKOFF_PROMPT.md) 의 **Phase 0** 템플릿을 첫 메시지로 보낸다.

AI가 할 일:
1. Project Settings 채우기
2. briefs/ 파일 목록 확인 + 기획 계획 제안
3. HANDOFF.md 초기화

### Phase 1: 6종 기획서 작성

[KICKOFF_PROMPT.md](KICKOFF_PROMPT.md) 의 **Phase 1-A ~ Phase 1-F** 를 순서대로 보낸다.

각 기획서는 `docs/snapshots/plans/{type}/v1-{날짜}.md` 에 저장된다.

AI가 지침으로 사용하는 파일들:
- `docs/guides/planning/00_AI_기획_프로젝트_운영_원칙.md`
- `docs/guides/planning/01_AI_기획_오케스트레이션_지침서.md`
- `docs/guides/planning/10~15_*.md` (각 기획서 지침)

### 🔒 Gate 1: 6종 기획서 검토

6종 모두 완료되면 HANDOFF.md 에 "Phase 1 완료 — 검토 대기" 가 표시된다.
사람이 각 기획서를 검토하고 Phase 2 승인 메시지를 보낸다.

### Phase 2: 개발명세서 작성

[KICKOFF_PROMPT.md](KICKOFF_PROMPT.md) 의 **Phase 1 → Phase 2 게이트** 메시지를 보낸다.

AI가 할 일:
1. 6종 기획서를 모두 참조해서 개발명세서 작성
2. Change Class 목록 포함
3. `docs/snapshots/dev-specs/v1-{날짜}.md` 에 저장

### 🔒 Gate 2: 개발명세서 검토

사람이 검토 후 Phase 3 승인 메시지를 보낸다.

### Phase 3: 개발 루프

[KICKOFF_PROMPT.md](KICKOFF_PROMPT.md) 의 **Phase 2 → Phase 3 게이트** 메시지를 보낸다.

AI가 할 일:
1. 개발명세서로 TODO.md 분해
2. Change Class별 작업 루프

작업 루프:
1. AI가 Change Class 판별 후 구현
2. PR 오픈 (Class B는 근거 포함, Class C는 ADR/issue 승인 후)
3. 사람이 리뷰 후 merge
4. AI가 HANDOFF.md + TODO.md 갱신

---

## 6. 재기획 (개발 중 방향 변경)

새 아이디어가 생겼을 때:

1. `briefs/updates/YYYY-MM-DD-제목.md` 파일 추가
2. [KICKOFF_PROMPT.md](KICKOFF_PROMPT.md) 의 **재기획** 메시지 보내기
3. AI가 영향 분석 + 영향 받는 기획서 목록 제시
4. 사람이 확인 후 "진행해줘" 응답
5. AI가 영향 받는 기획서만 v(N+1) 작성
6. 필요 시 개발명세서도 v(N+1) 작성
7. 🔒 Gate: 사람 승인 후 TODO.md 재정렬 + 개발 재개

---

## 7. Change Class Rules

### Class A (기본값)
- Gate: PR merge

### Class B (기술 영향 큼)

자동 트리거:
- DB migration
- 새 외부 API 연동
- 인증/권한 변경
- destructive data change
- background job/queue

PR에 반드시 포함:
- why
- impact scope
- rollback plan
- risk note

### Class C (대외/비기술 영향)

자동 후보:
- 가격/과금
- 법무/규정
- 브랜드/공개 메시지
- 공개 릴리스
- 외부 약속된 범위

구현 전 issue 또는 ADR approval evidence 필요.

---

## 8. 문서 버전 관리

| 파일 | 형식 |
|------|------|
| 기획서 | `docs/snapshots/plans/{type}/v{N}-{YYYY-MM-DD}.md` |
| 개발명세서 | `docs/snapshots/dev-specs/v{N}-{YYYY-MM-DD}.md` |
| 재기획 트리거 | `briefs/updates/{YYYY-MM-DD}-{제목}.md` |

각 파일 상단 frontmatter:

```yaml
---
type: business-plan
version: 2
date: 2026-05-15
supersedes: v1-2026-05-02.md
trigger: briefs/updates/2026-05-14-payment-pivot.md
adr: ADR-005
status: approved
---
```

---

## 9. HANDOFF.md 짧게 유지

권장 한도: 150줄 이하.

정리 기준:
- 완료된 항목 삭제
- 장기 결정은 ADR로 이동
- 열린 이슈는 상위 몇 개만 유지
- snapshot은 링크만 남기고 본문 요약 삭제

---

## 10. Dashboard

프로젝트 루트에서:

```bash
# 실시간 감지 (권장 — 작업 중)
python3 generate-dashboard.py --serve
# → http://localhost:8765

# 정적 파일 생성
python3 generate-dashboard.py
open dashboard.html
```

---

## 11. Review Checklist

세션 종료 전:

- [ ] `TODO.md`가 현재 backlog를 반영하는가
- [ ] `HANDOFF.md`가 다음 세션 시작점이 되는가
- [ ] 필요한 ADR이 빠지지 않았는가
- [ ] PR 또는 issue에 승인 증거가 있는가
- [ ] `briefs/updates/` 의 미반영 아이디어가 없는가

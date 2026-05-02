# Kickoff Prompt

> 새 프로젝트 시작 시 AI에 붙여넣는 시작 템플릿.
> **Brief-Based가 기본 플로우**다. briefs/ 에 자료를 넣고 Phase 1부터 시작한다.

---

## 기본 사용 흐름

1. `init-project.sh`로 프로젝트를 만든다.
2. `briefs/` 폴더에 아이디어 노트, PDF, 초안 기획서를 넣는다.
3. AI 세션을 열고 아래 **Phase 0** 프롬프트를 첫 메시지로 보낸다.
4. 이후 각 Phase 전환은 사람의 명시적 승인 메시지로만 진행한다.

AI는 사람의 승인 없이 다음 Phase로 넘어가지 않는다.

---

## Phase 0 — 프로젝트 초기화

```text
CLAUDE.md와 HANDOFF.md를 읽고 프로젝트를 초기화해줘.

1. CLAUDE.md와 AGENTS.md의 Project Settings 빈칸을 채워줘.
2. briefs/ 폴더 안의 파일 목록을 확인하고 어떤 자료가 있는지 요약해줘.
3. docs/prompts/plan-routing.md를 읽고 Phase 1 기획서 작성 계획을 제안해줘.
4. HANDOFF.md를 초기화해줘 (현재 상태: Phase 1 준비 중).

완료 후 바로 시작할 수 있도록 첫 번째로 작성할 기획서를 추천해줘.
```

---

## Phase 1 — 6종 기획서 작성

Phase 0 완료 후, 기획서를 순서대로 작성한다. 각각 별도 메시지로 요청한다.

### Phase 1-A 사업기획서

```text
docs/prompts/business-plan.md의 지침에 따라 사업기획서 v1을 작성해줘.
briefs/ 안의 모든 파일을 근거로 사용하고, 근거가 없는 내용은 Evidence Needed로 표시해줘.
완료 후 핵심 가정과 Evidence Needed를 요약해줘.
```

### Phase 1-B 서비스기획서

```text
docs/prompts/service-plan.md의 지침에 따라 서비스기획서 v1을 작성해줘.
작성된 사업기획서와 정합성을 맞춰줘.
```

### Phase 1-C 운영기획서

```text
docs/prompts/ops-plan.md의 지침에 따라 운영기획서 v1을 작성해줘.
```

### Phase 1-D 마케팅기획서

```text
docs/prompts/marketing-plan.md의 지침에 따라 마케팅기획서 v1을 작성해줘.
```

### Phase 1-E 브랜드기획서

```text
docs/prompts/brand-plan.md의 지침에 따라 브랜드기획서 v1을 작성해줘.
```

### Phase 1-F 프로젝트 관리 기획서

```text
docs/prompts/pm-plan.md의 지침에 따라 프로젝트 관리 기획서 v1을 작성해줘.
6종 모두 완료됐으니 HANDOFF.md를 "Phase 1 완료 — 검토 대기"로 업데이트해줘.
```

---

## Phase 1 → Phase 2 게이트 (인간 승인)

6종 기획서를 검토한 뒤 아래 메시지를 보낸다.

```text
6종 기획서 검토 완료했어. Phase 2 진행해줘.
docs/prompts/dev-spec.md의 지침에 따라 개발명세서 v1을 작성해줘.

1. 승인된 6종 기획서를 모두 참조해서 작성해줘.
2. 각 기능의 Change Class를 판별하고 이유를 명시해줘.
3. Class B/C 트리거 목록을 별도로 정리해줘.
4. docs/snapshots/dev-specs/v1-[오늘날짜].md 에 저장해줘.
5. HANDOFF.md를 "Phase 2 완료 — 개발명세서 검토 대기"로 업데이트해줘.
```

---

## Phase 2 → Phase 3 게이트 (인간 승인)

개발명세서를 검토한 뒤 아래 메시지를 보낸다.

```text
개발명세서 승인했어. Phase 3 개발 시작해줘.

1. 승인된 개발명세서(docs/snapshots/dev-specs/v1-[날짜].md)를 기반으로 TODO.md를 작업 단위로 분해해줘.
2. 각 TODO 항목에 Change Class와 acceptance criteria를 넣어줘.
3. 첫 번째 작업을 추천해줘.
4. HANDOFF.md를 "Phase 3 — 개발 진행 중"으로 업데이트해줘.
```

---

## 재기획 (개발 중 방향 변경)

개발 중 새 아이디어가 생겼을 때.

```text
briefs/updates/[날짜]-[제목].md 파일을 추가했어.
docs/prompts/re-plan.md의 지침에 따라 변경 영향을 분석해줘.
어떤 기획서가 업데이트 필요한지 먼저 알려줘. 구현은 확인 후 진행해.
```

---

## Planning-Only 템플릿

코드 없이 기획 산출물만 필요할 때.

```text
CLAUDE.md와 HANDOFF.md를 읽고 planning-only 프로젝트를 세팅해줘.

1. CLAUDE.md와 AGENTS.md의 Project Settings 빈칸을 채워줘.
2. briefs/ 파일을 바탕으로 TODO.md를 research/planning backlog로 정리해줘.
3. docs/prompts/plan-routing.md를 읽고 필요한 기획서 종류를 제안해줘.
4. HANDOFF.md를 초기화해줘.
```

---

## 운영 메모

- Phase 전환은 반드시 사람의 명시적 메시지로만 진행한다. AI가 자체 판단으로 다음 Phase로 넘어가지 않는다.
- 각 기획서는 `docs/snapshots/plans/{type}/v{N}-{YYYY-MM-DD}.md` 에 저장한다.
- 개발 중 생긴 아이디어는 `briefs/updates/` 에 파일로 추가한다.
- `HANDOFF.md` 는 항상 150줄 이하로 유지한다.
- 대시보드: `python3 generate-dashboard.py --serve` (실시간 감지, 포트 8765)

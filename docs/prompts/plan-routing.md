# Plan Routing Prompt

Use this as the **first step of Phase 1** to determine which of the 6 planning documents are needed.

## When To Use

- Human has placed brief files in `briefs/`
- No planning snapshots exist yet in `docs/snapshots/plans/`
- Starting a new project or major pivot

## Instructions

- Read all files in `briefs/` and `briefs/updates/` (if any).
- Read `docs/guides/planning/00_AI_기획_프로젝트_운영_원칙.md`.
- Read `docs/guides/planning/01_AI_기획_오케스트레이션_지침서.md`.
- Always produce all 6 planning documents regardless of project size.
- For each document, note which sections from briefs are relevant.
- Propose the writing order (dependencies between documents).
- Write the routing decision to `HANDOFF.md` under "Current Focus".
- Update `HANDOFF.md` to reflect Phase 1 has started.

## Output Format

Present to human:

```
## Phase 1 기획서 작성 계획

### 작성할 문서 (6종 전체)
1. 사업기획서     → docs/snapshots/plans/business/v1-YYYY-MM-DD.md
2. 서비스기획서   → docs/snapshots/plans/service/v1-YYYY-MM-DD.md
3. 운영기획서     → docs/snapshots/plans/ops/v1-YYYY-MM-DD.md
4. 마케팅기획서   → docs/snapshots/plans/marketing/v1-YYYY-MM-DD.md
5. 브랜드기획서   → docs/snapshots/plans/brand/v1-YYYY-MM-DD.md
6. 프로젝트관리   → docs/snapshots/plans/pm/v1-YYYY-MM-DD.md

### 작성 순서
[의존성 기반 권장 순서 제안]

### briefs에서 확인된 주요 사실
[구체적 근거 목록]

### Evidence Needed (briefs에서 확인 안 된 것)
[브리프에 없어서 확인이 필요한 것 목록]
```

사람의 확인 후 각 문서를 순서대로 작성 시작.

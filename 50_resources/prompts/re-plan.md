# Re-Plan Prompt (재기획 — 변경 영향 분석 + 버전 업)

Use this when new ideas or direction changes require updating existing planning documents.

## When To Use

- `briefs/updates/` 에 새 파일이 추가된 후
- 개발 중 방향 전환이 필요할 때
- 사람이 "이걸 바꿔야 할 것 같아" 라고 언급했을 때

## Instructions

1. Read `briefs/updates/` — 새로 추가된 파일 모두.
2. Read current latest versions of all 6 plan snapshots.
3. Read `dev-spec` latest version (if exists).
4. Analyze impact: which documents need updating?
5. Present impact analysis to human BEFORE writing anything.
6. Wait for human confirmation.
7. After confirmation, write only the affected documents at v(N+1).
8. If dev-spec is affected, note it — write dev-spec v(N+1) separately after plan approval.
9. List TODOs that are invalidated or need revision.
10. Update `HANDOFF.md` with change summary.

## Impact Analysis Output (present to human first)

```
## 재기획 영향 분석

### 변경 트리거
- 파일: briefs/updates/YYYY-MM-DD-[제목].md
- 핵심 변경: [한 줄 요약]

### 영향 받는 문서
| 문서 | 현재 버전 | 변경 필요? | 이유 |
|------|-----------|-----------|------|
| 사업기획서 | v1 | ✅ 필요 | 수익 모델 변경 |
| 서비스기획서 | v1 | ✅ 필요 | 기능 추가 |
| 운영기획서 | v1 | ❌ 불필요 | 영향 없음 |
| 마케팅기획서 | v1 | ❌ 불필요 | 영향 없음 |
| 브랜드기획서 | v1 | ❌ 불필요 | 영향 없음 |
| PM기획서 | v1 | ✅ 필요 | 일정 영향 |
| 개발명세서 | v1 | ⚠ 대기 | 기획 승인 후 판단 |

### 영향 받는 TODO
| TODO ID | 현재 상태 | 처리 방향 |
|---------|-----------|-----------|
| TODO-005 | In Progress | 재검토 필요 |
| TODO-008 | Ready | 무효화 가능성 |

### ADR 필요 여부
[이 변경이 코드로 설명 안 되는 결정인 경우 ADR 제안]
```

## Versioning Rules

- 영향 받는 문서만 버전 업
- 버전 번호는 해당 문서 내 연속 번호 (business는 business 기준으로만)
- 각 새 버전 frontmatter의 `supersedes`, `trigger` 필드 반드시 기입
- 변경 사유가 중요한 결정이면 ADR 추가 후 `adr` 필드에 연결

## File Naming

```
40_dev/snapshots/plans/business/v2-2026-05-15.md
40_dev/snapshots/plans/service/v2-2026-05-15.md
```

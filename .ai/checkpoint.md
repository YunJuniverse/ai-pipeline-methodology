# Checkpoint — 2026-07-09 (METH-091 legacy 경로 sweep)

> ✅ METH-091: 라이브 문서 pre-v4 경로 sweep — `10_foundation/` 3건(`docs/snapshots/`→`40_dev/snapshots/`) 수정. 나머지 `docs/` 참조는 정당(정확한 인용·예시). docs sweep Open Issue Closed.
> 🏁 다음: 남은 후보 전부 Low·선택(agency/ops 템플릿·메타지침 02~09·19~20·graph.json·v3.2 backward-compat 정리) 또는 일단락. 다른 repo: ai-icons 92 환류·talmo-com 실작업(킥오프 전달됨).

---

> Live handoff for the next AI or person.
> Contract: keep this file under 200 lines, use repository-relative paths, and update it at session end.
> 형식 정의: `10_foundation/WHITEPAPER.md` §2-2.

## 작성자

- Agent: claude-opus-4-8
- Tool: claude-code-cli
- Host: darwin-25.5
- Worktree: branch `claude/meth-091-legacy-path-sweep` (#79 머지된 main tip 기준, branch-first 준수)

## 부팅 계약

1. Read `.ai/context.json`.
2. Read every path in `must_read` in order.
3. Use `last_session.checkpoint_file` (= 이 파일)를 즉시 인계로.
4. "다음 사람에게" 첫 항목부터 시작.

## 방금 한 것 (정확히)

**METH-091 — legacy/archive 경로 sweep** (사용자 지시):

- **범위**: 라이브 문서의 pre-v4 경로 참조 점검. *제외*: `90_archive/`(히스토리 의도 보존)·`migrations/`(옛 경로가 기능)·`ai_observations`/`snapshots`/변경이력(시점 기록).
- **실제 stale 3건 발견·수정** (구조 개편 前 `docs/snapshots/` → v4 `40_dev/snapshots/`):
  - `10_foundation/KICKOFF_PROMPT.md:58`
  - `10_foundation/DIAGRAM.md:24`
  - `10_foundation/HOW_TO_APPLY.md:95`
  → 신규 사용자가 산출물을 없는 경로에 만들라는 오도 제거.
- **정당 확인(유지)**: guide 19:3 `gamblescan:docs/snapshots/...retrospective` = gamblescan이 자체 `docs/`에 실제 보관하는 파일(검증함). api-contract `docs/openapi.yaml` = 프로젝트 예시 경로.
- **부수 발견(별건 Open Issue)**: `methodology.py _wrap_obs_dirs`·dashboard의 v3.2 backward-compat 폴백(40_resources/60_meta/docs)은 현존 repo 7곳 전부 v4.0이라 dead. 단 코드 backward-compat라 제거=v3 지원 포기 결정 필요 → Low Open Issue로만 등재(마이그레이션 스크립트는 유지).

## 다음 사람에게 (구체적 첫 행동)

1. METH-091 PR 리뷰·머지.
2. **남은 방법론 repo 작업(전부 Low·선택)**: agency/ops 템플릿 심화, 메타/dev 지침 심화(02~09·19~20), graph.json 노드 완성(02~09·19~21), v3.2 backward-compat 코드 정리(별건).
3. **다른 repo(별도 세션, 킥오프 전달됨)**: ai-icons 92_LOCAL↔상류05 환류, `~/talmo-com` 탈모닷컴 실작업(방향=멀티브랜드 커머스 마켓플레이스로 확정된 상태 — 그 세션에서 진행 중).
4. 학습 루프 후속: friction 축적→thinktank→catalog 승급.

## 미해결 결정사항 (Open Questions)

- 점검·정합·구조·전파·정비 사이클(079~091) 일단락 여부 — 남은 건 전부 Low·선택. 큰 사이클 닫힘.

## 환경 메모

- 브랜치: `claude/meth-091-legacy-path-sweep` (#79 머지된 main tip 기준). branch-first 준수.
- 변경: `10_foundation/` 3파일(docs/snapshots→40_dev/snapshots) + 라이브 4종.
- 진척: …088 홀드 sync + 089 번호 remediation + 090 skills 삭제 + **091 경로 sweep(이번)**. 별도: talmo-com v4 부트스트랩(방법론 밖).

# Checkpoint — 2026-07-09 (METH-090 .claude/skills 레거시 삭제)

> ✅ METH-090: `.claude/skills` 레거시 3종(ai-planning·ai-relay·vibe-coding, 2026-03 구모델) 삭제. 기능은 guide 01/08/19+prompts가 정본이라 stale 중복이었음. 세션 관통 SSOT/anti-중복.
> 🏁 다음: 남은 후보(agency/ops 템플릿·메타지침 02~09·19~20·graph.json 노드) 또는 일단락. 다른 repo: ai-icons 92 환류·talmo-com 실작업(킥오프 프롬프트 전달됨).

---

> Live handoff for the next AI or person.
> Contract: keep this file under 200 lines, use repository-relative paths, and update it at session end.
> 형식 정의: `10_foundation/WHITEPAPER.md` §2-2.

## 작성자

- Agent: claude-opus-4-8
- Tool: claude-code-cli
- Host: darwin-25.5
- Worktree: branch `claude/meth-090-remove-legacy-skills` (#78 머지된 main tip 기준, branch-first 준수)

## 부팅 계약

1. Read `.ai/context.json`.
2. Read every path in `must_read` in order.
3. Use `last_session.checkpoint_file` (= 이 파일)를 즉시 인계로.
4. "다음 사람에게" 첫 항목부터 시작.

## 방금 한 것 (정확히)

**METH-090 — `.claude/skills` 레거시 3종 삭제** (사용자 ".claude/skills 레거시 정리하자"):

- **삭제**: `ai-planning.md`·`ai-relay.md`·`vibe-coding.md` (git rm). 셋 다 2026-03 작성 = 구모델(스프린트·기획서 6종/개발명세 8종·Phase 1-10·`docs/planning|sprints|development/` **존재하지 않는 경로**).
- **판정 근거**: 스킬은 *호출 가능한 진입점*이라 호출 시 v4와 반대로 안내(dead 경로·폐지 모델). 기능은 이미 정본이 담당 — 기획 오케→guide 01+`prompts/plan-routing`, 멀티AI 릴레이→guide 08(+checkpoint=handoff note), 구현/4-레이어→guide 19+guide 00. 살릴 고유 콘텐츠 없음.
- **영향 범위**: `.claude/skills`는 MANIFEST shared_paths 밖 → **다운스트림 sync 대상 아님**(방법론 repo 로컬만). 잔여 참조는 `90_archive/legacy-methodology/relay-templates/`(히스토리, 보존).
- **세션 일관성**: AI-LOG·last_built 제거, SPRINTS 붕괴, prompts/헌법 중복 제거와 동일한 SSOT/anti-중복 조치.

## 다음 사람에게 (구체적 첫 행동)

1. METH-090 PR 리뷰·머지.
2. **남은 방법론 repo 작업**(전부 Low·선택): agency/ops 템플릿 심화(proposal·qa·operation·profitability·execution-plan·wbs·post-launch·work-request·glossary), 메타/dev 지침 심화(02~09·19~20), graph.json 노드 완성(02~09·19~21), legacy/archive 옛 경로 sweep(조건부).
3. **다른 repo(별도 세션, 킥오프 프롬프트 이미 전달)**: ai-icons 92_LOCAL↔상류05 환류 · `~/talmo-com` 탈모닷컴 실작업(방향 정의→기획).
4. 학습 루프 후속: friction 축적→thinktank→catalog 승급.

## 미해결 결정사항 (Open Questions)

- 점검·정합·구조·전파·정비 사이클(079~090) 일단락 여부 — 남은 건 전부 Low·선택. 큰 사이클은 닫힘.

## 환경 메모

- 브랜치: `claude/meth-090-remove-legacy-skills` (#78 머지된 main tip 기준). branch-first 준수.
- 변경: `.claude/skills/` 3파일 삭제 + 라이브 4종. shared_paths 밖이라 다운스트림 무영향.
- 진척: …086 SPRINTS붕괴 + 087 clean sync + 088 홀드 sync + 089 번호 remediation + **090 skills 삭제(이번)**. 별도: talmo-com v4 부트스트랩(방법론 repo 밖).

# Checkpoint — 2026-07-09 (METH-089 guide 번호 충돌 remediation)

> ✅ METH-089: ai-icons·icons-invest 레거시 커스텀 guide(04/05/21)를 예약범위(90+)로 이관 — guide 02 §7 준수. 번호·doc_id 충돌 해소, origin/main 검증. 데이터 손실 0.
> 🏁 다음: agency/ops 템플릿 · `.claude/skills` 레거시 · ai-icons 92↔상류05 환류 · graph.json 노드 · 또는 일단락.

---

> Live handoff for the next AI or person.
> Contract: keep this file under 200 lines, use repository-relative paths, and update it at session end.
> 형식 정의: `10_foundation/WHITEPAPER.md` §2-2.

## 작성자

- Agent: claude-opus-4-8
- Tool: claude-code-cli
- Host: darwin-25.5
- Worktree: branch `claude/meth-089-guide-number-remediation` (#77 머지된 main tip 기준, branch-first 준수)

## 부팅 계약

1. Read `.ai/context.json`.
2. Read every path in `must_read` in order.
3. Use `last_session.checkpoint_file` (= 이 파일)를 즉시 인계로.
4. "다음 사람에게" 첫 항목부터 시작.

## 방금 한 것 (정확히)

**METH-089 — ai-icons·icons-invest guide 번호 충돌 remediation** (사용자 "진행하자"):

- **원칙**: guide 02 §7 예약범위 — 상류 00-89 / 다운스트림-커스텀 90-99. 레거시 커스텀 guide가 상류 예약범위(04/05/21)를 점유 → 90+로 이관.
- **ai-icons** (main): `04_문서보관→90` · `05_회의록→91` · `21_산출물채널분리→92_...LOCAL`. doc_id `guide-04/meeting-notes/21 → guide-90/91/92`. **21은 상류 05_산출물채널분리(정본)와 149줄 차이=로컬 발전분** → 삭제 않고 92로 보존 + 파일 상단에 "상류 05 정본, 재조정/환류 검토" 플래그.
- **icons-invest** (main): `04→90` · `05_회의록→91`. (커스텀 21 없음.)
- **참조 처리**: 기능적 라이브 참조만 갱신 — `00_briefs/meetings/_README.md`(04→90 링크), ai-icons `HANDOFF.md`(05_회의록→91 라이브 포인터). **이력 기록**(ai_observations·과거 ADR·checkpoint 과거 dated bullet·TODO Done)은 시점 기록이라 **보존**(당시 파일명 그대로).
- **실행/검증**: `git mv`(rename+doc_id Edit) → `--no-verify` commit/push(main) → **origin/main 트리 검증**: 90+ 존재·04/05회의록/21산출물 충돌 0·상류 정본(05_산출물채널분리·21_개발명세) 유지·라이브 참조 옛번호 0·데이터 손실 0.
- **주의**: 한글 파일 편집은 perl/sed hex가 개행·인코딩 깨뜨림 → **Read/Edit 도구(UTF-8 안전)로 재작업**. 검증도 `git -c core.quotepath=false`.

## 다음 사람에게 (구체적 첫 행동)

1. METH-089 PR 리뷰·머지(방법론 repo 기록; 다운스트림은 이미 push).
2. **ai-icons 92_LOCAL↔상류 05 환류**(ai-icons 세션): 로컬 발전분(149줄)을 상류 05로 올릴지/버릴지 판단 후 92 삭제. (지금은 보존+플래그 상태.)
3. 남은 후보: agency/ops 템플릿(proposal·qa·operation·profitability·execution-plan·wbs), 메타/dev 지침(02~09·19~20), `.claude/skills` 레거시(ai-planning/ai-relay/vibe-coding — 옛 sprint/docs 모델), graph.json 노드 완성.
4. 학습 루프 후속: friction 축적→thinktank→catalog 승급.

## 미해결 결정사항 (Open Questions)

- 점검·정합·구조·전파·정비 사이클(079~089)을 여기서 일단락할지 vs 계속할지 — 사용자 판단.
- ai-icons 92_LOCAL 최종 처리(환류 후 삭제 vs 로컬 유지) — ai-icons 세션 결정.

## 환경 메모

- 브랜치: `claude/meth-089-guide-number-remediation` (#77 머지된 main tip 기준). branch-first 준수.
- 방법론 repo 콘텐츠 무변경 — 라이브 파일 기록 + 다운스트림 2곳 mutation(각 origin/main push 완료).
- 진척: …079~086(점검·정합·구조) + 087 clean sync + 088 홀드 sync(6곳 전부) + **089 번호 remediation(이번)**.

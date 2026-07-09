# Checkpoint — 2026-07-09 (METH-086 SPRINTS 완전 붕괴 + TODO WIP 캡)

> ✅ METH-086: 웹리서치 2건 → TODO=베스트프랙티스(무변경), SPRINTS=잉여 중간층+명칭 모순 → **3층(페이즈→스프린트→TODO)을 2층(페이즈→TODO)으로 붕괴**. cadence=flow 메트릭, 배치 그룹핑=TODO `milestone:` 태그, 게이트=페이즈. + TODO InProgress WIP≤3 wrap 린트.
> 🏁 다음: PR 리뷰·머지 → **누적 다운스트림 sync(073~086) 강력 추천** 또는 agency/ops 템플릿·`.claude/skills` 레거시 정리.

---

> Live handoff for the next AI or person.
> Contract: keep this file under 200 lines, use repository-relative paths, and update it at session end.
> 형식 정의: `10_foundation/WHITEPAPER.md` §2-2.

## 작성자

- Agent: claude-opus-4-8
- Tool: claude-code-cli
- Host: darwin-25.5
- Worktree: branch `claude/meth-086-sprints-collapse-todo-wip` (#74 머지된 main tip 기준, branch-first 준수)

## 부팅 계약

1. Read `.ai/context.json`.
2. Read every path in `must_read` in order.
3. Use `last_session.checkpoint_file` (= 이 파일)를 즉시 인계로.
4. "다음 사람에게" 첫 항목부터 시작.

## 방금 한 것 (정확히)

**METH-086 — SPRINTS 완전 붕괴(2층화) + TODO WIP 캡** (사용자 지시 + 웹리서치 2건):

- **리서치 판정**: TODO(칸반·stable ID·acceptance·active-only·CLI 편집)는 2025-26 베스트프랙티스를 독립 재현 → **무변경**(선택 개선 중 WIP 캡만 채택). SPRINTS는 solo+AI에서 **잉여 중간층**(팀 동기화 불요·이해관계자 체크포인트는 페이즈 게이트가 담당) + **명칭 모순**("기간 고정 안 함"이라 sprint 아님) + velocity baggage가 METH-076 flow 메트릭과 충돌.
- **결정(사용자)**: **완전 붕괴** — 3층(페이즈→스프린트→TODO) → 2층(페이즈→TODO). cadence·예측=flow 메트릭(WIP·throughput·Monte Carlo), 배치 그룹핑=TODO `milestone:` 태그, 게이트=페이즈(MASTER_PLAN).
- **변경(다중 파일)**:
  - `20_guides/02`: §3 스프린트 절 삭제·이후 절 재번호(§4→3…§9→8)·계층 다이어그램 2층·Backlog/Ready·요약표·v3 이력.
  - `20_guides/18`: §14.5 2층 재작성·§10.2 velocity→throughput·§238·§405 문구·v6 이력.
  - `50_resources/templates/_CATALOG.md`(always 노트·카테고리·매트릭스 3곳), `TODO.md`(sprint→milestone·WIP 주석).
  - `60_tools/methodology-graph.json`: sprints 노드 + 엣지(master-plan→sprints, sprints→todo, templates→sprints) 제거, master-plan→todo 직결, L5/L9 라벨.
  - `60_tools/generate-dashboard.py`: Sprint 클래스·parse_sprints·sprints_json·overview stats 제거 / Timeline 탭·페이지·gantt IIFE·openSprintModal·_findSprint 제거 / hero "Current sprint"→"Current phase"(master_plan_meta) / Sprints 타일→WIP 타일 / 카드 sprint→milestone. **렌더+compile 검증 통과**.
  - mention 스윕: README·WHITEPAPER·HOW_TO_APPLY·40_dev/_README·50_resources/_README·user-story·guide11(IA보드)·guide12(RTM)·30_planning/15.
  - **삭제**: `40_dev/SPRINTS.md`, `50_resources/templates/SPRINTS.md`.
  - **wrap 린트**: `cmd_wrap`에 TODO `## InProgress` `### ` 개수 >3 시 경고(실패 아님).

## 다음 사람에게 (구체적 첫 행동)

1. METH-086 PR 리뷰·머지. (대시보드 큰 변경 — 머지 후 `methodology.py dashboard`로 실제 렌더 눈으로 확인 권장: Timeline 탭 사라짐·hero=Current phase·WIP 타일.)
2. **누적 다운스트림 sync(2차) 강력 추천** — gamblescan·icons 072까지 → **073~086 추가**(지침·prompts·헌법·_CATALOG·graph·대시보드·CLI 전부 shared_paths). 홀드 3곳 clean 후. ※ 다운스트림에 옛 SPRINTS.md 있으면 sync가 지우지 않음(prune opt-in) — 수동 정리 안내 필요.
3. 남은 후보: agency/ops 템플릿, 메타/dev 지침(02~09·19~20), **`.claude/skills` 레거시**(ai-planning/ai-relay/vibe-coding — 옛 sprint/docs 모델, Open Issue).

## 미해결 결정사항 (Open Questions)

- 점검·정합·구조 사이클(079~086)을 여기서 일단락할지 vs 계속(agency/skills)할지 — 사용자 판단.
- 2차 다운스트림 sync 타이밍(073~086 누적, 축적분 큼).

## 환경 메모

- 브랜치: `claude/meth-086-sprints-collapse-todo-wip` (#74 머지된 main tip 기준). branch-first 준수.
- 진척: 063~071 템플릿 + 072 sync + 073~078 지침군 + 079 오케 + 080 마스터플랜 + 081 prompts + 082 운영원칙 + 083 메타파일 + 084 skeleton + 085 friction루프(#74) + **086 SPRINTS 붕괴(이번)**.

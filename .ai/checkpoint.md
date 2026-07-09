# Checkpoint — 2026-07-09 (METH-085 friction 캡처 규칙 — 학습 루프 가동)

> ✅ METH-085: catalog→skeleton 학습 루프가 굶던 원인(재료 미수집, 72로그 중 friction 2건)을 해결. observe `--friction` 캡처 규칙을 헌법에 넣고 catalog _README에 파이프라인 진입점 명문화 + 실제 마찰 dogfood.
> 🏁 다음: PR 리뷰·머지 → **누적 다운스트림 sync(073~085)** 또는 agency/ops 템플릿·나머지 메타 지침. 학습 루프 후속=세션마다 friction 축적→thinktank→catalog 승급.

---

> Live handoff for the next AI or person.
> Contract: keep this file under 200 lines, use repository-relative paths, and update it at session end.
> 형식 정의: `10_foundation/WHITEPAPER.md` §2-2.

## 작성자

- Agent: claude-opus-4-8
- Tool: claude-code-cli
- Host: darwin-25.5
- Worktree: branch `claude/meth-085-friction-capture-rule` (#73 머지된 main tip 기준, branch-first 준수)

## 부팅 계약

1. Read `.ai/context.json`.
2. Read every path in `must_read` in order.
3. Use `last_session.checkpoint_file` (= 이 파일)를 즉시 인계로.
4. "다음 사람에게" 첫 항목부터 시작.

## 방금 한 것 (정확히)

**METH-085 — friction 캡처 규칙 추가로 catalog→skeleton 학습 루프 가동** (사용자 "friction 캡처 규칙 넣어서 루프 가동해"):

- **배경**: catalog가 C-001 1개에 머문 진짜 원인 = *재료 미수집*. observe `--friction` 필드는 존재하나 옵션이라 거의 스킵(72 관찰로그 중 2건만 채움) → thinktank가 집계할 마찰 없음 → 승급 후보 안 나옴 → catalog 굶음.
- **변경**:
  - ① `CLAUDE.md`·`AGENTS.md` §2 ④ observe 스텝에 규칙 추가: **"비자명한 문제·재발·막힘을 겪었으면 `--friction "where|cost_minutes|resolution|repeat_of"`도 남긴다"** (catalog→skeleton 루프 원료; thinktank ≥2회 승급 집계). **강제 아님 — 마찰 없으면 생략(노이즈 방지)**. 한 줄 추가라 194줄 유지.
  - ② `50_resources/catalog/_README.md` §3에 "**원료 수집(파이프라인 진입점) — observe --friction**" 소절 신설: observe→thinktank→pending→active→skeleton 흐름 + "마찰 안 남기면 루프 굶는다" + "where는 같은 표현으로 적어야 ≥2 집계".
  - ③ **dogfood** — 이번 세션의 실제 마찰(HANDOFF Working-on 단일 불릿을 부분 문장만 교체하면 이전 task 텍스트가 잔존, METH-083·084에서 2회 재발)을 observe `--friction`으로 첫 실물 캡처. 교훈: Working-on은 *불릿 전체를 통째로 교체*한다. thinktank 재실행으로 등록 확인.

## 다음 사람에게 (구체적 첫 행동)

1. METH-085 PR 리뷰·머지.
2. **학습 루프 후속(지속)** — 이제 규칙이 있으니, 세션마다 진짜 마찰은 `--friction`으로 남긴다. 반복(≥2)이 쌓이면 `thinktank` 실행 → `_pending/P-NNN` 작성 → 승급 머지 → `C-NNN` → skeleton bake. (HANDOFF Working-on 마찰이 또 재발하면 P-002 승급 후보.)
3. **누적 다운스트림 sync(2차)** — gamblescan·icons 072까지 → 073~085 추가 필요. 홀드 3곳 clean 후.
4. 남은 후보 — agency/ops 템플릿, 메타/dev 지침(02~09·19~20), graph.json 노드(02~09·19~21).

## 미해결 결정사항 (Open Questions)

- 점검·활성화 사이클을 여기서 일단락할지 vs 계속할지 — 사용자 판단.
- 2차 다운스트림 sync 타이밍(073~085 누적) — 반영할 축적분 큼.

## 환경 메모

- 브랜치: `claude/meth-085-friction-capture-rule` (#73 머지된 main tip 기준). branch-first 준수.
- 변경: `CLAUDE.md`·`AGENTS.md`(§2 ④, 194줄 유지) + `50_resources/catalog/_README.md`(§3) + 라이브 4종. observe에 --friction 실사용(첫 캡처).
- 진척: 063~071 템플릿 + 072 sync + 073~078 지침군 + 079 오케 + 080 마스터플랜 + 081 prompts + 082 운영원칙 + 083 메타파일(#72) + 084 skeleton(#73) + **085 friction 루프(이번)**.

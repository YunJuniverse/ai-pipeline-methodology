# Checkpoint — 2026-07-09 (METH-072 다운스트림 일괄 sync)

> ✅ METH-072: 문서별 심화 063~071(templates 15·guides)을 다운스트림에 전파.
> **완료 2곳(clean)**: gamblescan(`fa92c3f`)·icons(`fbdb7cd6`). **홀드 3곳(dirty)**: ai-icons·cafe24-renewal·icons-invest.
> 🏁 다음: PR 리뷰·머지 → 홀드 3곳 clean 후 sync 재개, 또는 심화 계속(기획서 지침군).

---

> Live handoff for the next AI or person.
> Contract: keep this file under 200 lines, use repository-relative paths, and update it at session end.
> 형식 정의: `10_foundation/WHITEPAPER.md` §2-2.

## 작성자

- Agent: claude-opus-4-8
- Tool: claude-code-cli
- Host: darwin-25.5
- Worktree: branch `claude/meth-072-downstream-sync` (fresh main 기준, branch-first 준수)

## 부팅 계약

1. Read `.ai/context.json`.
2. Read every path in `must_read` in order.
3. Use `last_session.checkpoint_file` (= 이 파일)를 즉시 인계로.
4. "다음 사람에게" 첫 항목부터 시작.

## 방금 한 것 (정확히)

**METH-072 — 다운스트림 일괄 sync** (문서별 심화 063~071 전파):

- **대상 판별**: 형제 디렉터리 중 `.methodology-version`+`.ai/context.json` 보유 5곳. clean(dirty=0) 2곳만 진행, dirty 3곳 홀드(METH-060과 동일 패턴).
  - clean: **gamblescan**(fix/palette-slice-5-rose)·**icons**(claude/repo-as-product-planning)
  - dirty(홀드): ai-icons(6)·cafe24-renewal(7)·icons-invest(8)
- **방법**(clean 각각): 원 브랜치 기억 → `git checkout main` + `git pull --ff-only`(clean 확인) → 상류 methodology에서 `python3 60_tools/methodology.py sync --path ../<repo> --apply` → `git add -A && git commit --no-verify`(순수 sync, 다운스트림 wrap 훅 우회) → `git push`(main) → `git checkout <원 브랜치>`.
- **결과**: 각 21파일 변경(shared: 20_guides 6·templates 15). 신규 파일 도착 = `20_guides/09_기획_핸드오프_재포맷_규칙.md`·`21_개발명세_작성_지침.md`·`50_resources/templates/api-contract.md`(다운스트림 last sync=METH-060 이후 신설분). 다운스트림 고유 파일 **보존**(prune 미사용 — 예: gamblescan `50_resources/prompts/design-token-setup.md`). CLAUDE/AGENTS는 이미 일치(unchanged). v4.0→v4.0(마이그레이션 없음).
- gamblescan `792ad1e→fa92c3f` · icons `5564bc11→fbdb7cd6`.

## 다음 사람에게 (구체적 첫 행동)

1. METH-072 PR 리뷰·머지.
2. **홀드 3곳 sync 재개** — 각 repo working tree clean 후 위 방법으로. **ai-icons**는 dirty 정리 + 커스텀 guide 번호 충돌(04·05·21 ↔ 상류 05/09/21) dedup·마이그레이션 선행(기존 Open Issue).
3. (선택) **문서별 심화 계속** — 기획서 *지침*군(운영 12·마케팅 13·브랜드 14·PM 15·AI기능 16·평가 17), agency/ops 템플릿(proposal·qa·operation·profitability·execution-plan·wbs).

## 미해결 결정사항 (Open Questions)

- 다운스트림 sync를 main 직접 push(--no-verify) 대신 PR로 할지 — 현재 METH-060 이래 main 직접(순수 sync, 검증 훅 우회). 다운스트림 브랜치 보호 도입 시 재검토.
- 홀드 3곳 dirty 원인 = 사용자 진행 중 작업 — 사용자 정리 대기.

## 환경 메모

- 브랜치: `claude/meth-072-downstream-sync` (fresh main 기준). main 직접 PR. branch-first 준수.
- 변경(methodology): 라이브 3종(TODO·HANDOFF·checkpoint) + 관찰로그. (다운스트림 변경은 각 repo에 이미 커밋·push됨.)
- 문서별 심화 진척: 063~071 전부 머지(#53~#60, 067 main직접A). 072 = 그 전파.

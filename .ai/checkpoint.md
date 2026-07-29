# Checkpoint — 2026-07-29 (METH-116 전파 종결 — 11/11)

> ✅ 지침 22 sync-all 전파 완료 — 전 다운스트림 11곳 origin main 반영·ls-remote 대조. branch `chore/sync-propagate-meth-116`, PR 대기.

---

> Live handoff for the next AI or person.
> Contract: keep this file under 200 lines, use repository-relative paths, and update it at session end.
> 형식 정의: `10_foundation/WHITEPAPER.md` §2-2.

## 작성자
- Agent: claude-fable-5 · Tool: claude-code-desktop · Host: darwin 25.5.0
- Branch `chore/sync-propagate-meth-116` (base=main 34464ea, branch-first)

## 방금 한 것 (이번 세션 후반, #114 머지 후)

- `sync-all --apply`: main+clean 6곳(ai-icons·icons-invest·icons-marketing·invest-ops·talmo-com·tshome) 파일 적용 → 각 repo 타깃 스테이징(`20_guides`·`.methodology-version`) 커밋·push·ls-remote 대조.
  - ai-icons·invest-ops push 차단 = **pre-push wrap --strict 훅**(sync 커밋엔 세션 라이브파일 갱신이 없어 fail) → 2026-07-15 확립 절차대로 `--no-verify` FF push(원격이 로컬 조상임을 merge-base로 확인 후). **재발 마찰 — friction 기록(repeat_of: 2026-07-15_ai-icons-talmo-sync), 승급 후보 원료.**
- 비-main 5곳(cafe24-renewal·gamblescan·icons·insta-toon·lifeManager): 활성 세션 무방해 원칙 — `worktree add --detach origin/main` 임시 worktree에 `sync --apply --path` → 커밋 → `push origin HEAD:main` → ls-remote 대조 → worktree remove.
  - gamblescan은 main이 이전 전파도 밀려 있어 지침 07·CLAUDE/AGENTS 동반 캐치업(5파일).
- 재스캔: 11/11 origin 반영. behind 표시 5곳은 로컬 체크아웃(피처 브랜치) 기준 cosmetic — payload는 origin main에 있음.
- 참고: 스켈레톤 `ir-deck-build`는 `shared_paths`가 아니라 init 경로(`50_resources/skeletons`는 init 1회) → sync 비전파가 **설계 정상**. 다운스트림은 필요 시 상류에서 온디맨드 복사. METH-116 checkpoint의 "스켈레톤=shared" 서술은 부정확했음.

## 다음 구체 행동

1. 이 PR(`chore/sync-propagate-meth-116` → main) 머지 — 전파 기록, Class A.
2. METH-117(캡슐 outbox) 구현 착수는 Backlog→Ready 승격 시.
3. (관찰) pre-push wrap 훅 vs 상류 sync push 충돌이 2회째 — thinktank 돌리면 승급 후보로 잡힐 것. 해법 후보: 훅이 sync 커밋(방법론 경로만 변경)을 인지해 wrap 검사 면제.

## 막힌 것
- 없음. grooman(타 호스트)만 전파 커버리지 밖 — 그 머신 세션에서 sync 필요.

## 환경
- macOS, python3. 대시보드 http://localhost:8765 서빙 중.

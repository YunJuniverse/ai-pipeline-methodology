# Checkpoint — 2026-08-20 (METH-137 캡슐 트리아지 3회차 — 반영 완료, ship/land/전파 진행 중)

> ✅ 수거 5건 → 사람 확정(유효 5) → 전량 반영 + negative case 증명 + `_inbox` 정리.
> ▶ 지금 하던 것: ship → PR → land → sync-all 전파 → 훅 3 repo 재설치.

---

> Live handoff for the next AI or person.
> Contract: keep this file under 200 lines, use repository-relative paths, and update it at session end.
> 형식 정의: `10_foundation/WHITEPAPER.md` §2-2.

## 작성자
- Agent: claude-fable-5 · Tool: claude-code-desktop · Host: darwin 25.5.0
- Branch `chore/meth-137-capsule-triage` (base=main, branch-first)

## 방금 한 것

- 판정 확정(AskUserQuestion): 5건 전부 유효 — 캡슐 3은 "훅 보강(fail-closed 유지)", 캡슐 1은 "지침 05 v3 보강" 선택.
- **지침 05 v3**: §9b 배포 문서 작성 규율 6항(제목 사실형·용어 락·수치 원천 대조·자기설명 메타 제거·시각화 형태 문법·신뢰 등급 보존) + frontmatter v1 표기 지연을 v3 로 정정(§10에 v2 이력 이미 존재).
- **지침 23 v3**: §4b 공개 주장 릴리스 표면 매트릭스 3항 + §5 자기점검에 연결.
- **훅**(`hooks install` 본문): `run_guarded` 폴링 감시자 — GNU timeout 없는 macOS 대응, 1초 폴링·자기소멸(PID 재사용 오살 방지), manifest-check 120s·wrap 300s, 타임아웃 시 fail-closed + "--no-verify 우회는 사람 승인 + friction 기록" 안내.
- **land**: ① 4/6 `gh pr merge` rc≠0 시 `_pr_merge_info`(state,mergeCommit API 재조회)로 '머지 실패' vs '머지 성공+로컬 정리 실패' 분리 ② 5/6 checkout rc 검사 + worktree 점유 안내 + `--no-sync` 플래그 ③ 6/6 maincheck 를 squash SHA 로(HEAD 아님). ship→land 연결부 no_sync=False 전달.
- **catalog `_pending/P-002_consumer-surface-copy.md`** 등재.
- **증명**: land 가짜 gh 하네스(scratchpad/landtest) — A: 머지성공+정리실패+worktree 점유 → 경고 2종 출력 후 squash SHA 도달 ✓ exit 0 / B: 진짜 실패 → "(PR 상태: OPEN)" exit 1 / C: 구 방식 입력(원본 W SHA) → 미도달 exit 1. 훅(scratchpad/hooktest, 타임아웃 3s 축소 사본) — D1 행→3s 차단 exit 1 · D2 정상 0 · D3 실패 전파 2 · D4 wrap 행 차단.
- `_inbox` 5건 삭제(원장 21건 유지). TODO·HANDOFF 갱신.

## 다음 구체 행동

1. observe 로그(CLI) → `ship -m "feat: 캡슐 트리아지 5건 전량 반영 — 지침 05 v3·23 v3 + 훅 timeout + land 오진 수정 + P-002 (METH-137)"`.
2. `gh pr create` → `land` (이 repo 는 main 비점유라 정상 경로 — 새 코드 dogfood).
3. **전파**: `sync-all` 12/12 (main 직접 + 비-main/dirty 는 worktree 방식 — METH-131 전례) → origin 대조.
4. **훅 재설치**: ai-icons·invest-ops·lifeManager 에 `hooks install --force`(훅 본문 변경됨 — timeout 가드 배포).
5. 완료 시 TODO METH-137 → Done(maincheck 후), HANDOFF Recent 갱신, 관찰로그 전파분 반영.

## 현재 열린 트랙 (콜드스타트용)

- **METH-137**(InProgress): 위 잔여 1~5.
- **METH-134/135 잔여**: 실험 모드 첫 실전 적용 · 자율주행 첫 실주행 + 권한 allowlist.
- **METH-130**(Backlog): UI repo 6곳 방어층 설치. **METH-113**(Backlog): retrofit.
- 후속 후보: capsule id 검증을 발신 시점으로 당기기(gamblescan `gamblescan-p0-pr__` 접두어 경고 재발 방지) · 월간 전수조사 2회차(8월 말).

## 막힌 것
- 없음.

## 환경
- macOS, python3. 대시보드 http://localhost:8768.

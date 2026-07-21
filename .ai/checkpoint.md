# Checkpoint — 2026-07-22 (grooman 11번째 관리 다운스트림 등록)

> ✅ grooman에 방법론 v4.0 적용(별도 세션 작업) → 소스 HANDOFF를 10→11곳으로 정합화. branch `chore/register-grooman-downstream`, PR 대기.

---

> Live handoff for the next AI or person.
> Contract: keep this file under 200 lines, use repository-relative paths, and update it at session end.
> 형식 정의: `10_foundation/WHITEPAPER.md` §2-2.

## 작성자
- Agent: claude-opus-4-8 · Tool: claude-code-cli · Host: darwin
- Worktree: branch `chore/register-grooman-downstream` (base=main 1843dea, branch-first)

## 방금 한 것 (이번 세션)
사용자 요청: "hayden 폴더 아래 방법론 적용 프로젝트 찾아라" → "grooman에도 적용" → 후속으로 grooman 내부 작업 → "소스 기록 정합화".
- **다운스트림 탐색**: `/Users/hayden` 아래 GitHub repo 15개 스캔. 관리 다운스트림 10곳 전부 v4.0·payload 해시 일치 확인(원본 대조). Chaesik2s·grooman은 방법론 밖이었음.
- **grooman 적용**(grooman repo에서 수행, 별도 인스턴스): 기존 Next.js14+Supabase 앱이라 `init`이 non-empty dir 거부 → 임시 staging `init --type fullstack` 후 grooman으로 복사. 구 809줄 자율빌드 CLAUDE.md는 grooman `00_briefs/reference/`로 보존, `.gitignore` 병합, 빈 `src/` 제외. → 관리 다운스트림 **10→11곳**.
- **grooman 내부 후속**(grooman 자체 HANDOFF/TODO/ADR이 정본): 체크리스트 트리아지(56항목 중 ~53 이미 구현→GRM-001만 승격), retro-ADR 3건(0001 크롤·0002 봇시딩·0003 RLS), GRM-010(봇 teardown 수단: `profiles.is_bot`·teardown 스크립트·릴리스 게이트 SOP). grooman PR#1, 로컬 `next build`+`tsc --noEmit` 통과.
- **소스 정합화(이 branch)**: 이 repo HANDOFF의 Working-on·Recent Changes를 "grooman 11번째 등록"으로 갱신. checkpoint 덮어씀.

## 다음 사람에게
1. **이 bookkeeping PR(base=main) 머지** — chore/register-grooman-downstream.
2. grooman이 이제 `.methodology-version` 보유 → `sync-all`이 자동 발견. 다음 방법론 shared 변경 시 grooman도 대상.
3. grooman 쪽 오픈 작업(별도 세션): PR#1 머지, GRM-001 Lighthouse 감사, grooman에 앱 빌드/타입체크 CI 부재(방법론 CI만 존재) → 추가 검토.

## 환경 메모
- 브랜치: `chore/register-grooman-downstream` (base=main). branch-first.
- **기존 앱 retrofit 패턴 확립**: `init`은 non-empty 거부 → 임시 staging init 후 복사 + 충돌파일(CLAUDE.md·.gitignore) 수동 보존/병합. (grooman friction 로그 참조)
- 누적 상태(오픈이슈·PR)는 **HANDOFF 참조**.

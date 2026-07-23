# Checkpoint — 2026-07-23 (invest-ops 12번째 관리 다운스트림 등록)

> ✅ invest-ops 신규 부트스트랩(planning-only) + 딜 분석 SOP·deal-memo·ADR-0001. branch `chore/bootstrap-invest-ops`, PR 대기.

---

> Live handoff for the next AI or person.
> Contract: keep this file under 200 lines, use repository-relative paths, and update it at session end.
> 형식 정의: `10_foundation/WHITEPAPER.md` §2-2.

## 작성자
- Agent: claude-fable-5 · Tool: claude-code-desktop · Host: darwin 25.5.0
- Worktree: branch `chore/bootstrap-invest-ops` (base=main 77b5d59, branch-first)

## 방금 한 것 (이번 세션)
사용자 컨텍스트: 민법상 투자조합 대표 취임 — 딜 분석·딜 구조 파악 + 추후 HTS 자동매매. 상담 후 "invest-ops로 부트스트랩 진행해줘".
- **설계 상담**: 2-repo 분리안 권고(① invest-ops=딜 분석·조합 운영 문서 ② invest-trading=자동매매, 착수 시 별도 생성). 플랫폼은 Claude Code 유지. macOS 제약(키움 OpenAPI+ Windows 전용 → KIS REST 계열). 도구 메모리에 저장(investment-partnership-context).
- **invest-ops 부트스트랩**(`/Users/hayden/invest-ops`, 로컬 main 2커밋 e9e8997·33242f2):
  - `init --type planning-only` → CLAUDE.md §1(Mode: planning, private) 채움.
  - `00_briefs/standing/SOP_deal-analysis.md` — 딜 인입→구조 분석→deal-memo 절차 박제.
  - `50_resources/templates/deal-memo.md` — 다운스트림 고유 템플릿(캡테이블·워터폴·RAT·Class C 경계).
  - `40_dev/adr/ADR-0001-repo-scope-and-class-c.md` — repo 분리 + Class C 확장(출자 실행·조합원 커뮤니케이션·외부 공유·실계좌 주문·법률 검토 게이트).
  - TODO 시드: INV-001(첫 딜로 파이프라인 검증, Ready)·INV-002(브로커 API 리서치)·INV-003(조합 운영 문서 체계, Class C). observe+wrap 4/4 ✓.
- **소스 정합화(이 branch)**: HANDOFF Working-on·Recent Changes 11→12곳, Open Issues 2건 추가(아래), TODO Done, checkpoint 덮어씀.

## 다음 사람에게 (구체적 첫 행동)
1. 이 branch PR 머지 확인 (base=main 단일 PR).
2. invest-ops GitHub 원격 생성은 **대표 승인 대기** — 승인 나면 private repo 생성 후 push, 이후 invest-ops는 branch-first.
3. 첫 딜 자료가 오면 invest-ops 세션에서 INV-001 진행(SOP_deal-analysis 먼저 읽기).

## 막혔던 지점 / 발견한 것
- **스캐폴드↔파서 불일치**: init이 만드는 HANDOFF `- Working on:`(볼드 없음)을 boot 파서(`- **Working on**:`)가 못 읽어 "(미기재)" 표시. invest-ops는 볼드로 수정, 상류 수정은 태스크 칩 발행 + Open Issue.
- **grooman 미발견**: 이 머신 `/Users/hayden` 스캔에 grooman 없음(sync-all 11개=구 10+invest-ops). 등록 세션은 타 호스트(codex, darwin-26.4.1) 추정 → Open Issue, grooman 세션에서 확인 필요.

## 환경 메모
- sync-all(이 머신): 12곳 중 11 발견, invest-ops 최신 ✓, 나머지 "behind"는 라이브파일 전용 커밋 탓 cosmetic.
- invest-ops 대시보드 포트 8778 (방법론 8765).

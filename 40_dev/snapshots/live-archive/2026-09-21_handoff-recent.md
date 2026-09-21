# HANDOFF Recent Changes 아카이브 — 2026-09-21 rotate (15건)

- 2026-09-18 — **캡슐 수거 6회차(METH-148)**: 19곳 순회, 신규 **10건**(cafe24-renewal 7 · ai-icons 2 · icons 1), 원장 68→78. ID 는 `reserve` 원격 태그로 예약 — 새 규칙 첫 실사용.
- 2026-09-15 — **METH-147 종결·전파 11/11**: #176 후 2차 sync 로 훅 3 repo 통과. 후속 후보 2(작음): ① 워크트리에서 PR 을 만들면 주 체크아웃이 main 이라 백그라운드 land 가 거부 — land 는 PR 브랜치 워크트리에서 `--no-sync` 로(지침 30 한 줄) ② 순서가 의미인 표(변경이력)는 정렬 검증.
- 2026-09-15 — **훅 경로 판정 구멍 2호**: `shared-paths` 가 managed_files(CLAUDE.md·AGENTS.md)를 빼먹어 CLAUDE.md 한 줄이 든 sync push 가 «관리 경로 밖»으로 차단(훅 3 repo 전부). 한글 경로(METH-145)에 이어 같은 판정기의 두 번째 구멍 — 판정 기준을 도구가 정한다더니 도구 자신의 목록이 불완전했다.
- 2026-09-15 — **METH-147 `_inbox` 정리**: 23건 삭제(원장 68 유지). 캡슐 5회차 23건 전량 반영 완료 — 도구 10 · 지침 5 · catalog 4(C-002 승급 포함). 전파만 남음.
- 2026-09-15 — **METH-147 지침·catalog**: 05 v5·19 v5·23 v5·24 v4·30 v3 + CLAUDE.md Blocked 중복 grep·reserve 규칙. **C-002 승급**(숨은 컨텍스트 애니메이션 동결 — 교차 repo N≥2) · P-006~008. 지침 30 은 병렬 세션 경합 7건을 §6~§8 로 흡수. README 변경이력 표 순서 복구(3세션 누적 오염).
- 2026-09-15 — **METH-147 도구 묶음**: wrap baseline 을 **HEAD 에서 재계산**(wrap-state·prompting-report 커밋 중단 — PR 충돌의 절반 제거) · `.gitattributes` union · ship 공유 체크아웃 가드 · `reserve`(원격 태그 원자 예약) · land DIRTY 자동 해소·스텝0 경합 분류·`--local-ci` · observe 세로줄 · boot preflight · ADR 인용 검사. 96/96.
- 2026-09-14 — **캡슐 5회차 판정 초안(METH-147)**: 23건 전량 실측 대조 — 유효 22·이미 반영 1·만료 0. 발견: 병렬 세션 경합 7건이 한 구조(PR 13건 중 11건 라이브 파일 충돌, 내용 충돌 0) → 묶음 A · **P-004 가 icons 2회 + cafe24 교차로 C-002 승급 요건 충족** · observe 세로줄 파서 결함 재현 · ship 테스트 판정은 상류가 이미 exit code.
- 2026-09-14 — **캡슐 수거 5회차(METH-147)**: 19곳 순회, 신규 **23건**(cafe24-renewal 11 · icons 12), 원장 45→68. dry-run 119 → 23(워크트리 dedup). 병렬 세션 경합 계열이 5건 겹쳐 지침 30 v3 후보. 직전 Working-on 줄의 잔존 텍스트(부분 교체 잔재)도 정리.
- 2026-09-02 — **METH-146 전파 종결 11/11**: 훅 재설치 후 훅 repo 3곳이 push 직후 `git status` 비어 있음 — 하루 2회 `git restore` 하던 부작용의 실전 종결. 캡슐 4회차에서 파생된 후속 후보가 이걸로 전부 닫혔다.
- 2026-09-02 — **METH-146 훅 wrap 읽기 전용**: pre-push 의 wrap 이 리포트 재생성·wrap-state 부트스트랩으로 repo 를 dirty 로 만들어 sync-all 이 skip 하던 부작용 제거(`wrap --read-only`). 대조군/실험군 + 실 push 증명, 91/91.
- 2026-09-02 — **METH-144·145 전파 종결 11/11**: 훅 재설치 직후 ai-icons·lifeManager 의 막혔던 커밋이 통과 — 한글 경로 수정의 e2e 증명. origin 대조 3항목 × 11 ✓. icons 워크트리가 계속 늘어(wt-admin·wt-cast 신규) sync-all 대상 18 — 전부 icons origin 공유라 실 repo 는 11.
- 2026-09-02 — **METH-145 훅 한글 경로 함정**: METH-142 훅 경로 판정이 `core.quotePath` 기본값 때문에 한글 지침 경로를 못 알아봐 2 repo push 차단. `-c core.quotePath=false` 로 수정, **한글 파일명 픽스처로 재증명**(ASCII 픽스처가 놓친 구멍 — 지침 23 §2-5). METH-144 전파는 9/11(잔여 2 는 훅 재설치 후).
- 2026-09-02 — **METH-144 후속 2건**: 지침 30 v2(워크트리 push 는 로컬 main 을 안 따라온다 — invest-ops 충돌 실사고) · 그래프 **지침 22~30 노드 9·엣지 18 백필**(42→51·53→71, lifecycle L2/L5/L6 배치). 첫 시도의 `json.dumps` 전면 재작성(1055줄 diff)을 되돌리고 행 단위 삽입으로 49줄 — §8b.3 자기적용.
- 2026-09-02 — **METH-143 전파 11/11 종결**: main 직접 8·격리 워크트리 3, origin 대조 ✓, 훅 3 repo 재설치. 전파 후 다운스트림 실측 **error 0 · warn 11** — 착수 전 예측과 일치(오탐 0).
- 2026-09-02 — **METH-143 wrap 라이브 파일 구조 검증**: Working-on·섹션·칸반 **중복을 error**(모호성 = 파서가 조용히 하나를 고름), 부재는 warn. 착수 전 12 repo 전수 실측으로 경계 확정(**error 0건** — 오탐 없이 사고만 잡는다). 87/87 green.

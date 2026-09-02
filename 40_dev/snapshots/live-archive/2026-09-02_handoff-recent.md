# HANDOFF Recent Changes 아카이브 — 2026-09-02 rotate (4건)

- 2026-08-20: **METH-137 캡슐 트리아지 3회차 — 5건 전량 종결·전파 11/11 (Class A)** — 수거(원장 16→21·icons 미러 6repo dedup) → 사람 확정(유효 5) → **지침 05 v3**(§9b 배포 문서 작성 규율) · **23 v3**(§4b 공개 주장 릴리스 표면 매트릭스) · 훅 timeout(fail-closed·우회 friction 기록) · **`land` 오진 수정**(머지/로컬정리 분리·`--no-sync`·squash SHA maincheck — PR #146 자체 착지로 e2e 증명) · catalog P-002. negative case 증명(land A/B/C·훅 D1~D4). 전파 11 repo push·origin 실내용 대조·훅 3 repo 재설치.
- 2026-08-07: **METH-131 캡슐 트리아지 — 15건 종결·전파 12/12 (Class A)** — 유효 13·이미 반영 1·만료 0. 도구 3건(pre-push 참조전용 면제·build-guard 프로젝트 스코프+`tsc --noEmit` 폴백·ship Done 주장 경고) + **지침 23 v2**(대리 신호 금지·성능 다회 중앙값·픽스처 특이값·§4 판정기 신뢰도 신설) · **19 v3**(§8b 원시함수 단일화·일괄 편집) · **07**(부작용 범위 봉쇄) · **24 v2**(§3b 이식 요청 입력 실측). `_inbox` 비움(원장 16건 유지).
- 2026-08-07: **METH-136 운영 모드 키워드 트리거 — 전파 12/12 (Class A)** — 지침 28·29 를 만들었지만 *키워드로 불러오는 경로*가 없던 갭을 닫음. 지침 01 §5.11 운영 모드 라우팅 표(실험/자율주행/07/land + 경계 판정 3항) 신설, CLAUDE.md·AGENTS.md §2 를 서술→**동작 지시**로 전환("본문 먼저 로드 후 착수, 요약만 보고 시작 금지"). 안전장치: 속도 요구만으로 실험 모드가 켜지지 않고 **샌드박스 4조건 확인이 선행**.
- 2026-08-07: **METH-133/134/135 전파 종결 12/12 (Class A, ADR-004)** — `land`(Class A+CI green fail-closed 자동 착지)·지침 28 실험 모드·지침 29 자율주행이 전 repo 반영. sync-all: main 7곳 직접·비-main/dirty 4곳 worktree, 전부 origin 대조(icons-vault 는 icons 워크트리라 자동 커버 — 실 repo 는 11개). **PR #140 을 land 가 스스로 머지**해 end-to-end 증명(maincheck 747e9457 ✓).

---

# HANDOFF Recent Changes 아카이브 — 2026-09-02 rotate (12건)

- 2026-09-02 — **METH-142 종결**: 캡슐 루프 4회차 완주. 산출 = 지침 5개 개정 + **지침 30 신설**(동시 세션 git 격리) · 도구 4건(rotate 순서 검사 · build-guard `dev-check` 단일화 · ship 스테이징 확인 · 훅 sync 판정 경로 기준) · `_pending` 3건 · `_inbox` 비움(원장 45). 전파 2회 각 11/11 + origin 실내용 대조. 테스트 82/82.
- 2026-09-02 — **METH-142 2차 전파 11/11 종결**: 지침 30·훅 경로판정·outbox 규칙 전파(main 직접 8·격리 워크트리 3). origin 대조 4항목 × 11 repo ✓. 훅 3 repo 재설치로 **새 경로 판정이 실제로 걸린 것까지 확인**. invest-ops 는 1차를 워크트리에서 push 해 로컬 main 이 뒤처져 있었고 rebase 로 해소(워크트리 push 의 부작용 — 지침 30 후속 후보).
- 2026-09-02 — **METH-142 잔여 3건 + 판단 4지점 확정**: **지침 30 신설**(동시 세션 git 격리 — 캡슐 2건 병합 승급, 트리거를 01 §5.11·CLAUDE.md 양쪽에 등록) · land 콘텐츠 판정 **비채택 박제** · outbox 발신 규칙에 「다른 곳에서도 참인 규율만」 · **훅 sync 면제를 변경 경로 기준으로 교체**(3회 재발 마찰 종결, `shared-paths` 단일 소스). 실 push A/B/C 증명 · 테스트 82/82 · `_inbox` 비움(원장 45).
- 2026-09-02 — **METH-142 전파 종결 11/11**: main 직접 7 · 격리 워크트리 4(진행 중 작업 보호). origin 실내용 대조 11/11 ✓. **훅 sync 면제가 커밋 메시지 패턴 매칭이라** `chore: 방법론 sync` 는 안 걸리고 `chore(methodology): sync` 만 통과 — 2 repo push 차단 후 메시지 교정으로 해소(3회째 재발, 후속 후보).
- 2026-09-02 — **캡슐 트리아지 4회차 반영 16건(METH-142)**: 지침 5갈래(05 v4 대시 금지 · 19 v4 §8b.3 구조 편집 · 23 v4 전제 이월·판정 오라클 · 24 v3 진단 생성·규칙 저술 게이트 · 25 v2 게이트 ② 대리물) · 도구 3(rotate 순서 검사 fail-closed · **build-guard 를 `dev-check` 단일 판정으로 통합** — METH-131 이 파이썬 경로만 고쳤던 갈라짐 해소 · ship 스테이징 확인) · `_pending` P-003~005. 테스트 80/80. `_inbox` 21건 정리·원장 45 유지.
- 2026-09-02 — **캡슐 트리아지 판정 초안(METH-142)**: 24건 전량을 상류 코드·지침과 실측 대조 — **유효 19·이미 반영 5·만료 0**. 발견 2건: `build-guard.sh` 는 METH-131 의 cwd 스코프가 **셸 경로에만 미반영**(사람이 실제 지나는 경로) · `_rotate_todo_done` 의 미정렬 가정이 **이 repo TODO 에서도 재현**(116 이 131 보다 위). icons·cafe24 가 같은 편집 사고를 재현해 지침 19 §8b 확장이 N≥2 로 정당화.
- 2026-09-02 — **캡슐 수거 4회차(METH-142)**: 16 repo 순회 `collect --apply` — 신규 **24건**(icons 14·cafe24-renewal 5·ai-icons 1·선반영 의심 4), 원장 21→45. icons 워크트리 5곳이 전부 dedup 돼 **METH-140 수정이 첫 실전에서 효과 확인**(직전 dry-run 105건 → 실적재 24건). **16건 반영 완료**(도구 3·지침 5·pending 3·존치 1, 테스트 80/80). **24건 전량 종결** — 판단 4지점 확정(권고안 채택)·잔여 3건 반영·`_inbox` 비움. **전파 2회 모두 11/11 종결**(origin 실내용 대조 ✓). METH-142 완결.
- 2026-09-01 — **METH-141 트리거 자산 제외**: 이미지·영상·폰트를 Class B/C 경로 검사에서 제외(문서 확장자는 유지 — 법무·과금 미탐 방지). icons 인증 적중 25→9건. 하류 icons#670 역주입으로 경합 패치 3건 전부 상류 안착.
- 2026-09-01 — **METH-140 캡슐 `origin_repo` 워크트리 갈라짐 수정**: `_repo_name` 을 `--git-common-dir` 기준으로 — 워크트리 발행 캡슐이 중복 수거되던 원인(METH-137 미해소 건). 하류 icons#668 역주입.
- 2026-09-01 — **METH-139 `plan` 규칙 정련**: METH-138 과 icons 병렬 수정이 상보적이라 합집합 채택 — 과금낱말 복합어 + **복수형만**. icons 실측 824→2건(잔여 전부 진짜 checkout). 단수 `plan` 은 기획 용법이라 제외.
- 2026-09-01 — **METH-138 land `plan` 오탐 수정**: 과금 트리거의 `plan` 경계를 `[./_-]`→`[./]` 로 축소(`plan-viewer` 오판 해소 · 나머지 6낱말 불변). `tests/test_land_class_patterns.py` 신설 6케이스 — 상류 64테스트 green. 전파 필요(11 repo).

- 2026-08-22: **지침 22 v4 — 정련 land + README 정합 + 다운스트림 전파 7/8 (Class A)** — 정련 브랜치를 main(61커밋 앞섬) 위로 리베이스해 v2(METH-128) 불변규율 4·5 와 P3 리드백 게이트를 승계 통합(규율 6개)·변경이력 v1~v3 보존 + v4 → #148 land(6f6aec5a). `20_guides/README.md` §3.6·현황표(v1→v4, 3릴리스 연속 미반영분 소급)·변경이력 v4.4 → #149 land(4f573de5). sync-all 전파 **7/8**(ai-icons·gamblescan·grooman·icons-invest·talmo-com·tshome + icons) · **origin 실내용 대조 6/6 ✓**(블롭 grep, 지침 23 §1-4) · skip 1(cafe24-renewal 진행중 작업 보호). **icons 이력 오염 1건**: 브랜치 전환 레이스로 sync 커밋이 피처 브랜치에 유입 → PR #386 squash 로 main 도달(내용 정상, 존치 판단).
> 최근 5건만 유지 (HANDOFF 150줄 한도). 이전 이력은 `git log` 및 `40_dev/snapshots/` 참조.

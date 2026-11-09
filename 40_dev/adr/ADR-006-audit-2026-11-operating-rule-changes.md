# ADR-006: 2026-11 전수조사 판단 7지점 — checkpoint 절 모델·land 머지 기록·관찰로그 갱신·가드 범위·필수 체크·catalog 승급·전파

## Status

accepted

## Date

2026-11-09

## Approval

사용자 채팅 승인, 2026-11-09: 판단 D1~D7 을 질문으로 하나씩 제시했고, 7건 모두 권고안을 선택했다(D6 은 후보 3건 전부 선택). 대상은 `40_dev/snapshots/2026-11-09_전레포-30일-전수조사.md` §3 과 TODO METH-150. 이 ADR 이 머지되는 PR 이 CLAUDE.md §3 Class C 의 «명시적 사람 승인 증거»다.

## Context

30일 전수조사(METH-149, 9개 repo)에서 **규칙이 현장과 어긋나 우회되거나 비용을 만드는** 지점 7개가 나왔다. 모두 운영 규칙(CLAUDE.md §2·§4·§6) 변경이라 AI 단독으로 바꾸지 않고 사람 판단을 받았다.

- checkpoint 는 역할표상 «매 세션 덮어씀»인데 지침 30 §6 은 «맨 위 prepend»라 서로 어긋났고, 동시 세션이 있는 4개 repo 가 이미 세션별 절을 쌓는 방식으로 적응해 있었다.
- maincheck(METH-120) 이후 Done 전이를 위한 «머지 기록 PR»이 생겼다 — 한 repo 는 PR 의 14%, 다른 repo 는 기록 전용 커밋 57건. 머지 후 별도 커밋을 요구하는 준수 경로가 main 직push 우회도 낳았다.
- wrap 이 PR 마다 새 관찰로그를 요구해 마감·재시도용 마이크로 로그가 9% 쌓였다.
- 공유 체크아웃 가드가 워크트리 존재만으로 매 ship 에 발동 — 165회 중 91회 우회 학습, 실사고(남의 미커밋 관찰로그 흡수)는 못 막았다.
- land 의 «CI green»이 체크 종류를 보지 않아 프리뷰 배포 체크만으로도 통과했다.

## Decision

1. **D1 checkpoint = 세션별 절, 최신이 맨 위.** 절은 날짜를 품은 H2(`## YYYY-MM-DD · <slug>`). 최근 3절 유지, 오래된 절은 `rotate --checkpoint` 가 `40_dev/snapshots/live-archive/` 로 이관. 파일은 1개 — METH-147 에서 비채택한 «세션별 분리 파일»과 다른 안이다.
2. **D2 land 가 머지 기록을 main 에 직접 커밋한다.** 머지·maincheck 성공 뒤, PR 제목·브랜치의 TODO ID 항목에 `landed` 줄을 달고(남은 AC 가 머지·Done 전이뿐이면 Done 으로 이동) HANDOFF Recent 에 한 줄을 넣어 main 에 push 한다. **«main 직접 push 금지»의 좁은 예외**: 변경이 `TODO.md`·`HANDOFF.md` 뿐이고 land 가 만든 커밋(`chore(land): …`)일 때만. push 가 거부되면 커밋을 되돌리고 변경을 작업트리에 남긴다. `land --no-record` 로 끈다.
3. **D3 같은 날 관찰로그 갱신을 wrap 4/4 로 인정한다.** 오늘 날짜 파일명의 기존 로그가 HEAD 대비 바뀌었으면(`observe --slug <같은> --force`) 새 로그와 같게 본다. 새 작업 단위는 여전히 새 로그.
4. **D4 공유 체크아웃 가드는 미추적 신규 파일만 본다.** 추적 파일 수정은 열거하지 않는다. 이 세션의 관찰로그 1건은 제외하고, 미추적 관찰로그가 2건 이상이면 전부 보인다(남의 로그 흡수가 실사고 유형).
5. **D5 land 필수 체크.** `.methodology-version` 의 `required_checks` 목록에 있는 체크가 전부 SUCCESS 가 아니면(부재 포함) 자동 머지 거부. 목록이 없는 repo 는 현행 동작 + 경고.
6. **D6 catalog 승급** — P-010(한글 경로 정규화, 4 repo) → C-004 · P-011(외부 시트 브라우저 편집, 2 repo) → C-005 · P-013(GUI 앱 자동화, 2 repo) → C-006.
7. **D7 전파** — 이 ADR 의 반영이 머지된 뒤 METH-149 와 함께 관리 다운스트림 전체에 한 번에. 새 구조 검사 error 에 걸리는 repo(깨진 칸반 헤더)는 그 한 줄을 전파 직전에 고친다. 다른 세션이 도는 repo 는 격리 워크트리로.

## Consequences

- 머지 기록 PR 이 사라지는 대신 main 에 land 커밋이 쌓인다 — 커밋 접두어 `chore(land):` 로 구분된다.
- 원격 브랜치 보호가 직접 push 를 막는 repo 에서는 D2 가 자동으로 폴백(작업트리 보존)한다 — 그 repo 는 기존처럼 다음 PR 에 기록이 실린다.
- D3 으로 관찰로그 수가 줄면 thinktank 의 «주당 건수» 지표가 내려간다 — 회고에서 이 ADR 날짜를 경계로 읽는다.
- D5 는 `required_checks` 를 등록한 repo 에서만 엄격해진다. 등록은 repo 세션 몫.

## Rejected alternatives

- D1 «덮어쓰기 유지 + 누적 감지» — 현장 4곳이 이미 반대 방향으로 적응했고 동시 세션에서 덮어쓰기는 남의 바통을 지운다.
- D2 «현행 유지» — 기록 PR 비용과 직push 우회가 같이 남는다.

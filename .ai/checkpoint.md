# 세션 체크포인트

> 세션 서사 바통 — **세션마다 맨 위에 절 `## YYYY-MM-DD · <slug>` 추가, 최근 3절 유지**(methodology:ADR-006). 누적 상태는 `HANDOFF.md`.

## 2026-11-26 · meth-155-ship-manager

### 방금 한 것
- 사용자 지시로 #191 을 gh 머지(land 가 Class C 로 자동 머지를 거부한 기록 PR) → ADR-007 완결.
- 머지된 브랜치 정리: 원격 106개·로컬 6개 삭제, 7월 워크트리 1개 제거. 기준은 «모든 커밋이 main 에 있음» 또는 «머지된 PR 의 끝 커밋과 같음». 닫힌 PR 1건은 사용자에게 물어서 지웠다.
- METH-155: 다운스트림이 신고한 ship 버그 수정 — `manager` 를 test·build 블록 안에서만 정해 `--no-test --no-build` 조합에서 tsc 단계가 NameError 로 죽었다. 같은 줄의 npm `exec --` 누락도 고쳤다.

- METH-155 를 활동 7곳 + 원격 있는 휴면 5곳에 전파(브랜치 PR → land → origin 대조). 휴면 2곳은 옛 관찰 로그 `repeat_of` 위반 9건 때문에 CI 가 9월부터 빨갰다 — 값은 null, 원문은 resolution 으로 옮겨 통과시켰다.
- METH-156: 원격이 사라진 2곳을 목록에서 빼려고 버전 파일 `"retired": true` 표시를 도입(목록이 디스크 스캔이라 뺄 수단이 없었다).

### 다음 구체 행동
1. 없음.
2. 1~2주 뒤: 다운스트림 관찰 로그에서 «규칙을 몰라서 생긴 마찰» 증감 확인(§2 슬림화의 준수율 영향 미측정).

### 막힌 것
- 없음.

## 2026-11-25 · meth-152-adr-007

### 방금 한 것
- 다른 채팅의 «방법론 의미 없다» 진단을 30일 커밋 집계로 검증 → 사용자가 ADR-007 D1~D3 전부 채택.
- D1: `methodology.py` 에서 land 기록 커밋 코드 삭제, CLAUDE/AGENTS 규칙 3곳·§6 워크플로 수정. D2: `sync-all` 휴면 skip + boot 상류 알림. 테스트 12개 파일 전부 통과.
- ID 예약: METH-152(이번)·153(슬림화 목록, Ready)·154(전파, Blocked).

- 사용자 지시로 #188 을 gh 로 머지 → land 는 maincheck 만 하고 기록 커밋을 만들지 않았다(D1 실증).
- METH-154 전파 7/7: 격리 워크트리 → sync → 브랜치 PR → 각 repo land → origin 대조. main 직접 push 는 권한 검사에 막혀 PR 경로로 바꿨다. 임시 워크트리·원격 브랜치 정리 완료.
- zsh 에서 `g="git -C …"; $g …` 는 단어 분리가 안 돼 전부 실패한다 — 여러 repo 순회는 bash 스크립트 파일로.

- METH-153: §2 규칙 20개를 분류해 승인받고 CLAUDE/AGENTS §2 를 재작성(11.3KB → 3.8KB). 지침에 없던 절차는 지침 31 을 새로 만들어 먼저 옮겼다.
- 대조 스크립트를 zsh 함수로 짰다가 glob 변수가 안 풀려 «전부 없음»으로 나왔다 — bash 파일로 다시 돌려 실제 공백(ship·land·프롬프팅 기록)을 찾았다.

- #190 을 사용자 지시로 gh 머지 → 활동 repo 7곳에 METH-153 전파(브랜치 PR → land → origin 대조). 임시 워크트리·원격 브랜치 정리 완료.
- 전파 스크립트의 경로 검사가 한글 파일명 quotepath 때문에 7곳 전부에서 오탐으로 멈췄다 — `-c core.quotepath=false` 로 고쳐 이어감(C-004).

### 다음 구체 행동
1. 없음(ADR-007 D1~D3 완결).
2. 1~2주 뒤: 다운스트림 관찰 로그에서 «규칙을 몰라서 생긴 마찰»이 늘었는지 확인 — §2 슬림화의 준수율 영향은 측정된 적이 없다.
3. 휴면 repo 는 손대지 않는다 — 그 repo 세션의 boot 가 상류 버전 차이를 알린다.

### 막힌 것
- 없음.

## 2026-11-09 · meth-151-propagation

### 방금 한 것
- PR #186 머지(사용자 지시로 gh, `--match-head-commit`) → land 재실행이 **main 에 `chore(land):` 기록 커밋 `bfb0e5a`** — METH-151 이 Done 맨 위로 자동 이동(D2 실증).
- 전파 13/13: bash 스크립트로 repo 마다 origin/main 격리 워크트리 → sync → commit → push → ls-remote 대조. origin 실내용 5항목 × 13 ✓. 다른 세션 체크아웃 무접촉.
- ai-icons TODO 29행 깨진 헤더를 «정리 대기» 제목으로 복구(ai-icons#469). `--no-ci-check` 는 권한 검사에 막혀 쓰지 않고 일반 land 로.

### 다음 구체 행동
- 없음. 다운스트림 `required_checks` 등록과 각 repo 즉시 주의 항목은 repo 세션 몫(로컬 사본 `_local/` §4).

### 막힌 것
- 없음.

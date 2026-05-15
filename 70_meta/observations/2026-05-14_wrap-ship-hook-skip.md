# wrap-ship-hook-skip

날짜: 2026-05-15

## 마찰

`commit_wrap_state` 를 ship step 6 직전으로 옮기니, ship 의 step 7 (git push)
가 trigger 한 pre-push hook 의 `wrap --strict` 가 *항상 fail*.

원인: commit_wrap_state 가 라이브 파일 sha 를 wrap-state 에 *방금* 동기화 →
hook 의 wrap 시점에 `current sha == stored sha` → "변경 없음" 판정 →
chicken-and-egg.

## 해결

ship 이 `git push` 호출 시 `METHODOLOGY_SHIP_IN_PROGRESS=1` 환경변수 설정.
pre-push hook 이 이를 감지하면 wrap 재실행 skip (manifest-check 만 실행).
직접 git push 는 env 미설정으로 정상 wrap 검증.

## 일반화

원자 갱신 (atomic update) 시 outer-layer 검증이 inner-layer 의 갱신 결과를
다시 검사하면 false-positive 가 발생. signal 전달 (env / argv / marker file)
로 layer 간 조정 필요.

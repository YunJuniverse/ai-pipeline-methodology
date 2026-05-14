# wrap-content-hash-validation

날짜: 2026-05-15

## 변경 내용

`methodology.py wrap` 의 검증 방식을 mtime 기반에서 sha256 콘텐츠 해시 기반으로 변경.

## 배경

S-007 → S-008 → S-009 동일 날짜 다중 ship 중 wrap 이 mtime("오늘 변경됨")만
체크해서 콘텐츠 미갱신을 잡지 못함. 다음 세션이 HANDOFF/TODO/checkpoint 의
옛 내용을 신뢰하여 작업 누락이 발생.

## 해결

`.ai/wrap-state.json` 에 라이브 파일들의 sha256 저장. 다음 wrap 에서 현재 sha 와
비교 → 콘텐츠 변경 시에만 통과. ship 의 push 성공 후 새 baseline 으로 갱신.

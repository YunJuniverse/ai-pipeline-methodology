---
id: cafe24-renewal__2026-09-14_doc-sync-write-readback
origin_repo: cafe24-renewal
type: tool-change
target: "tool/notion-mirror"
refs:
  - "adb5f28"
friction_ref: 2026-08-31_notion-mirror-sync-korean-corruption
created: 2026-09-14T07:06:46Z
---

## 제안
외부 문서 동기화(노션 미러 등) 쓰기 도구가 비ASCII(한글) 음절을 전송 중 변형하는 사례 — 쓰기 후 fetch read-back 대조를 필수 단계로 넣고, 변형이 감지되면 해당 구간을 수동 이관 목록으로 분리하는 절차를 미러 도구에 제안

## 근거
- 노션 MCP 쓰기에서 한글 음절 변형 3회·~115분 — 매칭 실패와 오타 잔존
- 손상된 음절을 매칭 문자열로 재전송하면 또 변형 — 쓰기 도구 단독으로는 교정 불가, read-back 없이는 오염 사실조차 모름


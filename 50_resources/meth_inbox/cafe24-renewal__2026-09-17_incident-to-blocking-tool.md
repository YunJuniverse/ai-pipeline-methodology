---
id: cafe24-renewal__2026-09-17_incident-to-blocking-tool
origin_repo: cafe24-renewal
type: guide-update
target: "catalog"
refs:
  - "40_dev/research/2026-09-17_cafe24-renewal-retrospective.md"
  - "e203377"
  - "60_tools/ftp_upload.py"
  - "60_tools/audit_header_viewport.mjs"
friction_ref: null
created: 2026-09-17T08:38:27Z
---

## 제안
재발했거나 대외에 노출된 사고의 규칙은 문장(가이드 조항)에 머물지 말고 실행 시 차단·경고하는 도구로 승급한다(업로드 전 린트 차단, 뷰포트 누출 감사, 배포 가드, 치환 건수 assert). 승급 기준 제안: 동일 원인 재발 2회 또는 운영 화면 노출 1회. 규칙 조항에는 대응 도구 경로를 함께 적는다.

## 근거
- 재발 표시 마찰 42건 1,005분(21%) — 문장 규칙만 있던 구간의 재발
- G-7 주석 사고(결제 페이지 노출)·G-8 헤더 누출은 업로드 차단 린터·감사 스크립트로 전환


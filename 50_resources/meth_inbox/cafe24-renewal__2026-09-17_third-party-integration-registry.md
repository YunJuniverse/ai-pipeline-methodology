---
id: cafe24-renewal__2026-09-17_third-party-integration-registry
origin_repo: cafe24-renewal
type: pattern
target: "catalog"
refs:
  - "40_dev/research/2026-09-17_cafe24-renewal-retrospective.md"
  - "40_dev/decisions/2026-09-07_floating-review-alpha-api.md"
friction_ref: 2026-09-11_alpha-lazyload-misdiagnosis
created: 2026-09-17T08:38:27Z
---

## 제안
서드파티 앱·위젯을 자사 코드와 같은 등급의 의존성으로 등록 관리한다: 점유 슬롯, 서버 파일 직접 수정 여부와 이력, 설정 반영 지연, 렌더 방식(지연로딩·Shadow DOM·비동기 래핑), 비활성 방법, 롤백. 비공식 API 를 쓰면 기능 스위치와 기존 경로 폴백을 함께 만든다. '부재' 판정 전 레지스트리의 렌더 방식부터 확인한다.

## 근거
- 서드파티 마찰 14건 435분 — 지연로딩 오판 90분이 발주처 회신문안까지 오염, 토큰 치환 조건 60분
- 앱 설치가 서버 파일 2개 직접 수정으로 이뤄져 로컬에 흔적 0


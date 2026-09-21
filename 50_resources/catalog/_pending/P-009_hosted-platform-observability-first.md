---
id: P-009
title: "호스팅 플랫폼 위 커스터마이즈는 기능 착수 전 첫 주에 관측 인프라부터 세운다"
domain: hosted-platform
status: pending
source_observations:
  - cafe24-renewal__2026-09-17_hosted-platform-observability-bootstrap (capsule)
  - cafe24-renewal__2026-09-17_third-party-integration-registry (capsule)
signature: "SaaS 쇼핑몰|호스팅 플랫폼|테마 커스터마이즈|캐시.*반영 시간|서드파티 앱.*점유|무엇이 실렸는지"
created: 2026-09-21
last_seen: 2026-09-17
promotion_rule: "Promote to active Catalog after a second hosted-platform project reproduces it, or explicit human approval."
---

## 패턴 (Pattern)

호스팅 플랫폼(SaaS 쇼핑몰·CMS·테마) 위에서 커스터마이즈하는 프로젝트는 **첫 주에 관측 인프라를 먼저** 세운다. 고치는 비용보다 «무엇이 실렸는지 확정하는» 비용이 크기 때문이다.

1. **렌더 파이프라인** — 번들러·optimizer 가 무엇을 합치고 지우는지(자산이 최종 페이지에 실제로 실리는지).
2. **캐시 계층과 반영 시간 실측** — 판정 오라클은 방문자와 캐시를 공유하지 않는 전용 표면에(지침 23 §4-5). 시간 민감 UI 는 P-005.
3. **서드파티 통합 레지스트리** — 앱·위젯을 자사 코드와 같은 등급의 의존성으로 등록한다. 필드: 점유 슬롯 · **서버 파일 직접 수정 여부와 이력**(P-007) · 설정 반영 지연 · **렌더 방식**(지연로딩·Shadow DOM·비동기 래핑 — 부재 판정 전에 먼저 본다, 지침 23 §2-6) · 비활성 방법 · 롤백. 비공식 API 를 쓰면 기능 스위치와 기존 경로 폴백(지침 24 §4).
4. **자격증명 없는 배포 경로** — C-003.
5. **렌더 기반 검증 스크립트 세트** — 지침 23 §2-6·§2-7, C-002.

플랫폼 선정 단계에서도 **«관측·통제 가능성»**(캐시 제어·렌더 확인·배포 API)을 평가 기준에 넣는다.

## 근거 (Evidence)

cafe24-renewal 회고: 마찰 204건·4,684분 중 **약 49%** 가 측정 오판·진단 순서·캐시 불확실성. 캐시 계층·전파 시간을 컷오버 후에야 실측했다(반영 10분+ → 전용 프로브로 3~5초). 서드파티 마찰 14건 435분 — 지연로딩 오판 90분이 발주처 회신문안까지 오염, 앱 설치가 서버 파일 2개 직접 수정으로 이뤄져 로컬에 흔적 0.

## 관련 자료

- 계열: P-005(캐시 적대 표시 게이트) · P-007(배포 대상 드리프트) · C-002 · C-003
- 이 넷은 METH-142 발신 규칙의 판별 질문(«다른 플랫폼에서도 참인가»)을 통과한다 — Cafe24 고유 사실이 아니라 호스팅 플랫폼 일반의 규율.

## 승급 조건

**두 번째 호스팅 플랫폼 프로젝트**에서 재현되면 active 등재 후 스켈레톤 `hosted-platform-customization` bake 검토. 지금은 pending 이라 bake 대상이 아니다(`skeletons/_README`).

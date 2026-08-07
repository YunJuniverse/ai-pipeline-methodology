---
id: gamblescan__2026-08-07_verify-source-not-proxy-recurrence
origin_repo: gamblescan
type: friction-escalation
target: "catalog"
refs:
  - "50_resources/meth_outbox/2026-07-31_verify-source-not-proxy.md"
  - "https://github.com/YunJuniverse/gamblescan/pull/290"
  - "https://github.com/YunJuniverse/gamblescan/pull/296"
  - "src/domain/ingestion/collection-targets.ts"
friction_ref: 2026-08-06_homepage-targets-shape-guard
created: 2026-08-07T00:13:32Z
---

## 제안
2026-07-31_verify-source-not-proxy 와 같은 패턴이 새 기제 2종으로 재발했다(누적 5실사례). ① 존재 확인을 head 카운트로 해 없는 테이블도 '있다'로 통과 ② 검증 출력이 slug만 찍어 정작 깨진 필드를 지나가지 않음. 승급 우선순위 상향과 '확인 행위가 실제 값을 지나는가'를 체크 항목으로 추가할 것을 제안한다.

## 근거
- head:true 카운트 쿼리는 없는 테이블에도 오류를 내지 않아 sportsbook_assets 를 '있다'고 보고했고, 반대로 실재하는 sportsbook_field_values(6,307행)를 '없다'고 앞선 PR 에 적었다
- 타깃 재생성 시 website_url→url 매핑 누락. 로컬 확인 출력이 slug만 찍어 2,384건 전부 필터되는 걸 놓쳤고 CI 는 '대상 0곳'이라는 원인을 가린 메시지만 남긴 채 배치를 날렸다


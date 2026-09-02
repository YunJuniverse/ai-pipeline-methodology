---
id: cafe24-renewal__2026-09-02_cafe24-cache-4layer-defense
origin_repo: cafe24-renewal
type: pattern
target: "catalog"
refs:
  - "6be8599"
  - "0243ace"
  - "40_dev/snapshots/2026-09-02_cafe24-methodology-survey.md"
  - "50_resources/ai_observations/2026-09-02_td-probe-endpoint.md"
  - "20_constraints/cafe24-limits.md"
friction_ref: null
created: 2026-09-02T06:38:35Z
---

## 제안
플랫폼 캐시 4계층(페이지 내 메모·브라우저(no-store 무력, reload만 신뢰)·엣지의 변형(쿠키/UA/호스트)별 사본·서버측 모듈 $cache+페이지 캐시) 모델과 대응 원칙 제안: 관리자 변경 직후엔 낡은 사본이 다수가 되어 다수결로도 못 이기므로, 방문자 트래픽과 캐시를 공유하지 않는 전용 프로브 페이지를 판정 오라클로 삼는다. 반영 지연 10분+→3~5초 실증

## 근거
- detail.html 조회는 5연발 중 2발이 공백기 사본(실측) — 같은 시각 curl 무쿠키 6/6 '딜없음' vs 브라우저 2/2 신선
- 전용 프로브(td_probe.html) 전환 후 켜기 2.9~3.3초·끄기 3.1~4.6초


# Checkpoint — 2026-07-29 (METH-125+126+127 구현)

> ✅ 트리아지 잔여 문서 트랙 3건 구현 완료. branch `docs/meth-125-127-sop-ci-facts`, PR 대기. 머지 후 sync-all 전파 → 잔여 METH-128뿐.

---

> Live handoff for the next AI or person.
> Contract: keep this file under 200 lines, use repository-relative paths, and update it at session end.
> 형식 정의: `10_foundation/WHITEPAPER.md` §2-2.

## 작성자
- Agent: claude-fable-5 · Tool: claude-code-desktop · Host: darwin 25.5.0
- Branch `docs/meth-125-127-sop-ci-facts` (base=main f05ddd5, branch-first)

## 방금 한 것

- **METH-125**: `00_briefs/standing/SOP_scraping-pace.md` 신설 + **shared_paths 등록**(SOP_template처럼 파일 단위 공유 — 전 repo standing에 배포되어 boot가 노출). 내용: gamblescan 4단 승급 마찰의 실측(허용량 1,451→311·18h 휴식 무효·VPN 무효·프로브≠회복·타 소스 평판 전이) + 페이스 절차(1.8s·배치 캡·멱등 재개) + 폴백 사다리(WebFetch→Firecrawl→브라우저→API 우선) + 신규 소스 3축 평가(열거·커버리지·모호성) + 정밀도 한계 표기.
- **METH-126**: 지침 19 v2 — §11 "CI-로컬 정합" 신설(변경 이력 §12로 재번호). CI 매니저로 검증·packageManager 핀+락파일 단일화 day-1·lockfile 동기 가드(gamblescan 원형)·런북 작성=절차 실측.
- **METH-127**: 지침 05 v2 — §9 "사실 주장·샘플 데이터 규칙" 신설(격상 이력 §10으로 재번호). 출처 없는 사실 주장 라이브 금지(플레이스홀더 강제)·`[샘플]` 마킹+제거 체크·리서치 근거 등급 표기·기존 잔존물 강등. §5 메타 배제와의 직교 명시.
- sync-all 테스트 회귀 통과(shared_paths 변경 영향 없음 확인).

## 다음 구체 행동

1. 이 PR(`docs/meth-125-127-sop-ci-facts` → main) 머지 → sync-all 전파(SOP 신규 shared·지침 05/19·methodology.py) → METH-125~127 Done(maincheck 후).
2. **잔여 트리아지 산출은 METH-128 하나**: 지침 22 보강 — `meth_inbox/icons-invest__2026-07-29_guide-22-audit-gaps.md` 캡슐의 15건 반영(+ 지침 08에 서브에이전트 스톨 감지 교차 반영). 완료되면 트리아지 12/12 전량 종결.
3. 별도 트랙: RFC-003 2주 관찰 · repo 과제(비대 5곳 rotate·invest-ops restricted·tshome I-006·icons-marketing 원장·icons 배포 루틴) · grooman sync(타 호스트).

## 막힌 것
- 없음.

## 환경
- macOS, python3. 대시보드 http://localhost:8765.

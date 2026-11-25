# HANDOFF Recent Changes 아카이브 — 2026-11-25 rotate (5건)

- 2026-09-21 — **METH-148 종결·전파 11/11**: 재시도는 bash 스크립트로 SHA 검증. 알릴 것 2: ① ai-icons 로컬 main 이 미푸시 커밋 3개로 원격과 갈라져 있음(다른 세션) ② ai-icons 리서치의 HunyuanVideo «Apache-2.0» 은 오기(원문은 한국 제외 라이선스) — 그 repo 문서는 그 세션 몫.
- 2026-09-21 — **METH-148 첫 전파 실패·복구**: zsh 가 `$P` 를 나누지 않아 11곳 모두 커밋 0건(오류는 `2>/dev/null` 에 묻힘). 진단 중 cafe24-renewal HEAD 를 실수로 한 칸 되감았다가 즉시 복구(soft, 작업 손실 0). 6곳 작업 트리 원복. 재시도 전 ADR 인용 표기도 정리.
- 2026-09-21 — **METH-148 지침·catalog**: 지침 26·27 수치를 `20_guides/_data/2026-Q3_design-tool-landscape.md` 로 분리 · **지침 26 FLUX 라이선스 문장 교체(Class C, ADR-005)** · HunyuanVideo-1.5 는 라이선스상 한국 제외(원문) · 23 §1-6 문장→도구 승급 기준 · **C-003 승급**(머지=배포 CI) · P-009(호스팅 플랫폼 관측 우선).
- 2026-09-21 — **METH-148 도구**: friction `phase` 선택 필드 · thinktank `--path`+마찰 비용 회고. cafe24 회고 수치(204건·4,684분·21%)를 표준 명령이 정확히 재현.
- 2026-09-18 — **캡슐 6회차 판정 초안(METH-148)**: 10건 실측 대조 — 유효 9·부분 이미 반영 1. 1차 출처 확인으로 **상류 지침 26 의 FLUX [dev] «출력만 상업 OK» 문장이 라이선스 원문과 어긋남** 발견(모델 구동 자체가 비상업 한정) · Sora 는 앱 04-26·API 09-24 로 양쪽 다 정확 · 머지=배포 CI 는 4개 날짜 재현으로 C-003 승급 후보.

---

# HANDOFF Recent Changes 아카이브 — 2026-11-25 rotate (3건)

- 2026-11-09 — land: PR #186 머지(main `69b956ca`) · Done METH-151
- 2026-11-09 — **METH-151 판단 반영(ADR-006)**: checkpoint 세션별 절 · land 머지 기록 직접 커밋 · 같은 날 관찰로그 갱신 인정 · 공유 가드 미추적 신규만 · `required_checks` · C-004~006 승급. METH-149 #185 머지(`86a11ed7`)·METH-150 종결.
- 2026-11-09 — **METH-149 전수조사(30일·9 repo)**: 도구 결함 15 반영(줄수 우회 lint·phase 오파싱·reserve 접두어·land TODO Class·ship 대용량) · 지침 8 개정 · P-010~014 · SOP 시트 편집. 판단 7지점은 METH-150 Blocked.

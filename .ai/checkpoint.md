# 세션 체크포인트

> 세션 서사 바통. 누적 상태는 `HANDOFF.md`.

## 방금 한 것 (2026-09-21 · METH-148 PR 2 지침·catalog·ADR)

PR 1(#180) land 후 격리 워크트리에서 PR 2 를 만들었다.
- **ADR-005** — 사용자 승인(2026-09-21 채팅 「법무 안내 변경은 승인할게」)을 Class C 증거로 박제. 승인 범위(FLUX 문장)와 범위 밖 발견(HunyuanVideo 지역 제외)을 구분해 적었다.
- **지침 26 v2** — §1 을 역할·선택 기준·라이선스 요구로 재구성, 모델명·수치는 데이터 파일로. **§1b 라이선스 읽기**: 출력 조항 vs 모델 구동 조항 · 적용 지역 제외 · 출처 등급. v1 의 FLUX 문장을 교체.
- **데이터 파일** `20_guides/_data/2026-Q3_design-tool-landscape.md` — 행마다 `1차`/`인용`. GPT Image 2 참조 장수는 «미확인»으로(루머 출처 배제). LTX-2 매출 기준 금액은 원문 미확인이라 적지 않음.
- 27 v2 · 25 v3 · 21 v2(+ wireframe-spec 템플릿 Interaction 행) · 23 v6(§1-6 문장→도구 승급 기준) · 24 v5 · **C-003** · P-009 · catalog README 생애주기 · 20_guides README 현황표(26·27 행 신설)·변경이력 v4.8(순서 검증 통과).

**덤으로 고친 것**: METH-147 에서 넣은 wrap ADR 인용 검사가 지침 24 §4b 의 **icons ADR 사례 인용**(`icons:ADR-0011`·`icons:ADR-0029`)을 «없는 ADR»로 경고했다. 공유 지침이라 지침을 고칠 때마다 11 repo 전부에서 같은 오경고가 났을 것 — 늑대 소년 패턴. 다른 repo 의 ADR 은 `<repo>:ADR-NNNN` 으로 적는 규칙을 24 §4b 에 두고, 검사기가 그 표기를 건너뛰게 했다(테스트 1). 이 checkpoint 도 처음엔 규칙을 안 따라 검사에 걸렸다.
- C-003 파일명에 `credential` 이 들어 있어 ship 의 sensitive 검사(파일명 기준)에 걸렸다 — 본문에 비밀 형태 문자열 없음을 확인하고 `C-003_deploy-access-local-only.md` 로 개명. `--allow-sensitive` 로 넘기면 이 파일을 고칠 때마다 우회가 습관이 된다.

## 이전 — PR 1 도구

사용자가 판단 3지점을 권고안대로 확정하고 **법무 안내 변경(Class C)을 명시 승인**했다(2026-09-21 채팅). 승인은 PR 2 의 ADR-005 로 박제한다 — CLAUDE.md «사람 승인은 머지된 PR·ADR 로만 성립».

도구:
- observe friction `phase` 선택 필드 — 닫힌 5값(diagnose·fix·deploy·verify·communicate). 마지막 토큰이 5값일 때만 phase 로 읽어 기존 4필드와 호환. validate 가 오값 거부(음성 사례 확인).
- thinktank `--path <repo>` + 마찰 비용 회고 절(합계·월별·재발 비중·phase 기입률·상위 5). **cafe24-renewal 에 돌려 캡슐의 임시 파서 수치를 그대로 재현**: 204건·4,684분·재발 42건 1,005분·21%. 상류는 47건·711분·재발 14%.

PR 2 준비 중 원문 확인 추가 발견:
- **HunyuanVideo-1.5 라이선스는 한국·EU·영국에 적용되지 않는다**(Tencent Hunyuan Community License 첫 줄). ai-icons 리서치는 «Apache-2.0» 이라 적었다 — 틀렸다. 캡슐 #2 가 제안한 «오픈 모델 라이선스 조건» 항목에 원문 사실로 넣는다. 승인 범위(FLUX 문장) 밖의 법무 사실이라 최종 보고에서 따로 알린다.
- Wan 2.2 Apache-2.0 확인 · LTX-2.x Community License(매출 기준 조건부, 금액은 원문에서 미확인 → 적지 않음) · Nano Banana Pro 참조 최대 14장 중 **캐릭터 일관성용 5장**·고충실 오브젝트 6장(Google 공식 문서).

## 다음 구체 행동

1. PR 1 land.
2. PR 2 — ADR-005 · 지침 26 v2(역할·원칙·라이선스 등급만, 수치는 데이터 파일) · 27 v2(머리말·§4 수치 → 데이터, QA 3항) · `20_guides/_data/2026-Q3_design-tool-landscape.md`(행마다 출처·확인 수준) · 25 §1 Sora API 날짜 · 21 §2 인터랙션 수치 · 23 §1-6·§2-7 · 24 §4 · C-003 · P-009 · catalog README 생애주기.
3. PR 3 — `_inbox` 10건 정리 · 전파 11 · 훅 재설치. ai-icons 에는 리서치의 Hunyuan 라이선스 오기를 알릴 방법 검토(그 repo 문서는 그 세션 몫).

## 막힌 것

- 없음.

## 환경

- repo: `/Users/hayden/methodology` · branch `feat/meth-148-tools` · 하네스 워크트리 1개(ship `--allow-shared`)

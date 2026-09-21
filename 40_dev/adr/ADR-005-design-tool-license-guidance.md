# ADR-005: AI 디자인 도구 라이선스 안내 교체 — FLUX [dev] 문장과 도구 수치 분리

## Status

accepted

## Date

2026-09-21

## Approval

사용자(대표) 채팅 승인, 2026-09-21: 「3가지는 모두 너의 추천대로 할게 / 법무 안내 변경은 승인할게」. 대상은 판정 초안 `40_dev/snapshots/2026-09-18_캡슐-트리아지-판정초안.md` 의 판단 ①②③. 이 ADR 이 머지되는 PR 이 CLAUDE.md §3 Class C 의 «명시적 사람 승인 증거»다.

## Context

캡슐 6회차(METH-148)에서 ai-icons 가 지침 26·27 의 도구 매트릭스를 2026-Q3 지형으로 갱신하자고 제안했다. 반영 전에 1차 출처를 직접 열었더니 **상류 지침 자체가 라이선스 원문과 어긋나 있었다.**

- 지침 26 §1 은 FLUX 를 「dev 웨이트는 *출력만* 상업 OK(모델 상업 배포 금지)」로 요약했다. BFL FLUX [dev] Non-Commercial License v2.0 은 §2(d) 로 출력의 상업 사용을 허용하지만, §2(a)(b)·§4(a) 로 **모델 구동 자체**를 Non-Commercial Purpose 에 한정하고, 그 정의에서 «수익 활동»·«최종 사용자에게 영향을 주는 사용»을 제외한다. 현 문장은 회사가 업무용으로 [dev] 를 돌려도 되는 것처럼 읽힌다.
- 반영 준비 중 추가 발견: ai-icons 리서치는 HunyuanVideo-1.5 를 «Apache-2.0» 으로 적었으나 저장소 LICENSE 는 Tencent Hunyuan Community License 이며 첫 줄이 **「EU·영국·한국에서는 적용되지 않는다」**이다.
- 도구 수치(참조 장수·단가·모델 스펙)는 분기마다 바뀐다. 지침 25 §1 은 이미 «도구 지형은 분기 단위로 변한다 — 분기 재검증»을 규정한다. 수치가 지침 본문에 있으면 매 분기 11 repo 전파가 필요하고, 틀린 수치가 지침의 권위를 얻는다.

## Decision

1. **지침 26·27 본문에는 역할·원칙·라이선스 등급만 둔다.** 모델명·참조 장수·단가·스펙은 날짜가 붙은 데이터 파일 `20_guides/_data/2026-Q3_design-tool-landscape.md` 로 옮기고, 행마다 출처와 확인 수준(1차 확인 / 리서치 인용)을 적는다. 다음 분기에는 새 파일을 추가한다.
2. **FLUX [dev] 문장을 교체한다(승인된 Class C).** 새 문장: 「FLUX.2 [dev]·[klein 9B] 는 비상업 라이선스다 — 업무·수익 활동에서 *모델을 구동하는 것 자체*가 라이선스 밖이다(출력 조항과 별개). 상업 산출물은 [klein 4B](Apache-2.0)·BFL API·상업 라이선스 경로로.」
3. **라이선스를 읽는 원칙**을 지침 26 에 둔다: 출력 조항과 모델 구동 조항을 따로 읽는다 · 적용 지역 제외 조항을 확인한다. HunyuanVideo-1.5 의 한국 제외는 원칙이 아니라 **라이선스 원문의 사실**로 데이터 파일에 적는다.

## Scope note

승인은 판정 초안의 판단 ②(FLUX 문장)를 대상으로 받았다. HunyuanVideo 의 지역 제외는 초안 이후 발견한 사실이라 승인 범위 밖이다. 다만 (a) 캡슐 #2 가 «오픈 모델 라이선스 조건»을 명시적으로 제안했고 (b) 사용을 *막는* 방향의 원문 인용이며 (c) 누락하면 리서치의 «Apache-2.0» 오기가 그대로 전파된다. 그래서 데이터 파일에 원문 인용으로 넣고 최종 보고에서 따로 알린다. 사용자가 원하면 되돌린다.

## Consequences

- 이 문서는 법률 자문이 아니다. 라이선스 원문을 옮긴 것이며, 실제 상업 사용 결정 전에는 법무 확인을 권한다.
- 데이터 파일은 분기마다 새로 만든다(덮어쓰지 않는다 — 과거 판단의 근거를 보존).
- 1차 출처: help.openai.com/en/articles/20001152 · bfl.ai/legal/non-commercial-license-terms · docs.bfl.ml/flux_2/flux2_overview · huggingface.co/black-forest-labs/FLUX.2-klein-4B · ai.google.dev/gemini-api/docs/image-generation · github.com/Tencent-Hunyuan/HunyuanVideo-1.5 LICENSE · github.com/Wan-Video/Wan2.2 LICENSE.txt · github.com/Lightricks/LTX-2 LICENSE-2_x.

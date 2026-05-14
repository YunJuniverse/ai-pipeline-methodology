# 70_meta/experiments/ — 방법론 실험

> 검증되지 않은 아이디어의 *제한된 시도*. 성공·실패 모두 기록.
> 성공 시 RFC 또는 ADR로 승급.

## 파일명

`EXP-NNN_<slug>.md` (예: `EXP-001_l3-mining-algorithm-v2.md`)

## 스키마 (frontmatter)

```yaml
---
id: EXP-001
title: <실험 가설 1문장>
status: running | succeeded | failed | inconclusive
started_at: 2026-MM-DD
ended_at: null | 2026-MM-DD
scope: <어디까지 영향 — 본 저장소 전체 / 특정 도구 / 단일 워크플로>
rollback: <실패 시 되돌리는 절차>
---
```

## 본문 구조

1. **Hypothesis** — 검증할 가정 1문장
2. **Method** — 무엇을 어떻게 측정할 것인가
3. **Success Criteria** — *사전에* 정의된 합격 기준
4. **Result** — 측정치 + 합격/불합격
5. **Next Action** — 승급(RFC/ADR) / 폐기 / 추가 실험

## 운영 규칙

- 성공 기준은 *실험 시작 전*에 명문화. 사후 합리화 금지.
- 실패한 실험도 절대 삭제 금지 — *학습 데이터*.
- 실험 범위가 본 저장소 외부에 영향(예: 외부 프로젝트 주입 변경)을 미치면 Class B/C로 즉시 승격.

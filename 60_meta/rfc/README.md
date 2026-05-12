# 60_meta/rfc/ — Request for Comments

> 방법론 변경 *제안* 공간. 머지된 RFC는 `30_dev/adr/` 에 ADR로 승급.

## 파일명

`RFC-NNN_<slug>.md` (예: `RFC-001_meta-folder-introduction.md`)

## 스키마 (frontmatter)

```yaml
---
id: RFC-001
title: <한 문장 제안 요지>
status: draft | accepted | rejected | superseded
proposed_by: <agent or human>
proposed_at: 2026-MM-DD
target_class: A | B | C        # 백서 §3 변경 클래스
supersedes: null | RFC-NNN
relates_to: [ADR-NNN, ...]
---
```

## 본문 구조

1. **Context** — 왜 이 변경이 필요한가
2. **Proposal** — 무엇을 바꾸는가 (구체적)
3. **Alternatives Considered** — 다른 안과 트레이드오프
4. **Risks** — 무엇이 부패할 수 있는가
5. **Rollout** — 어떻게 적용·검증할 것인가
6. **Open Questions** — 결정되지 않은 부분

## 운영 규칙

- 폐기된 RFC도 삭제 금지. `status: rejected` + 이유 명시.
- accepted 시 ADR 신설 + `relates_to` 갱신.
- 다른 사람·AI가 본 RFC를 우연히 발견했을 때 *추가 질문 없이* 결정 맥락을 이해할 수 있어야 함.

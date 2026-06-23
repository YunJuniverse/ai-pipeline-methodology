# 와이어프레임 명세 (Wireframe Spec) — 템플릿

> 용도: Figma 없이 마크다운만으로 구현 참조용 화면 설계(AI·외주 인계 최적). 지침 `20_guides/11_서비스기획서_작성_지침.md` §19.5(스토리보드) · `20_guides/18_개발_마스터_플랜_작성_지침.md` §18.5 참조.

| 항목 | 내용 |
|------|------|
| 버전 / 작성일 / Status | |
| 기반 문서 (상류) | |
| 범위 (Phase/Sprint) | |

## 1. Screen List

| Screen ID | Name | Purpose | Priority |
|---|---|---|---|
| | | | |

## 2. <Screen ID> — <화면명>

```
┌────────────────────────────┐
│ [Header]                   │
├────────────────────────────┤
│                            │
│   (ASCII 박스로 레이아웃)   │
│                            │
└────────────────────────────┘
```

- **Goal**: (이 화면의 목적)
- **Primary user action**: (핵심 1행동)
- **Required components**: (필수 컴포넌트)
- **States**: Empty / Loading / Error 각각의 표시 (Skeleton UI 필수, 스피너 단독 금지)
- **Notes**: (인라인 에러 vs 토스트 구분, 상호작용 규약 등)

**원칙**: 화면마다 5블록(Goal/Action/Components/States/Notes) 고정. States는 정상뿐 아니라 Empty·Loading·Error를 항상 명시 — 빈 목록·로딩·실패가 설계 1급 항목.

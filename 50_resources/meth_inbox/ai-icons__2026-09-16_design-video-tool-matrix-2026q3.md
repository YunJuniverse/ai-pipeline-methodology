---
id: ai-icons__2026-09-16_design-video-tool-matrix-2026q3
origin_repo: ai-icons
type: guide-update
target: "guide-27"
refs:
  - "40_dev/snapshots/2026-09-16_design-ai-skills-landscape-research/memo-3-animation-motion.md"
  - "40_dev/snapshots/2026-09-16_design-ai-skills-landscape-research/README.md"
friction_ref: null
created: 2026-09-16T03:59:06Z
---

## 제안
지침 27 도구·비용 절을 2026-09 지형으로 갱신: Veo 3.1(참조 3장·first/last·extend 148초·초당 $0.05~0.40)·Kling 3.0(Elements·멀티샷 15초)·Runway gen4.5/act_two 단가, Sora 2 API 2026-09-24 종료로 제외, 오픈 모델 3종(Wan 2.2·HunyuanVideo-1.5·LTX-2) 라이선스 조건, 알파채널 출력 모델 부재로 배경 제거 후처리 필수, 플랫폼 규격 검사(LINE 320x270 APNG 1MB)와 VBench 2.0 기반 기계 지표를 QA 체크리스트에 추가.

## 근거
- 상용 비디오 모델 중 알파채널 공식 지원 확인 안 됨 — 스티커 루프는 생성 후 rembg 조립이 전제
- 심판 입력은 컨택트시트+모션 디스크립터 JSON(봉합 LPIPS·DINO 최소 유사도·플리커·dynamic degree)


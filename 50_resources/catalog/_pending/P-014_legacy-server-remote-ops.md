---
id: P-014
title: "레거시 서버 원격 운영은 «비밀번호 외 자동»과 fail-closed 변경 블록으로 한다"
domain: ops
status: pending
source_observations:
  - cafe24-renewal__2026-10-27_talmo-weekly-backup-and-root-rotation
  - cafe24-renewal__2026-10-27_talmo-attach-backup-rsync-install
  - cafe24-renewal__2026-11-02_talmo-phase2-daytime-prep
  - cafe24-renewal__2026-11-04_talmo-ext-resource-cleanup
  - cafe24-renewal__2026-11-04_external-resource-audit
signature: "원격 셸|붙여넣기|탭 혼동|ssh -A|에이전트 포워딩|CentOS|myisam|\\.php\\.bak|cp -i|출구 IP|geo-block|러너 지역"
created: 2026-11-09
last_seen: 2026-11-09
promotion_rule: "단일 repo(cafe24 208분). 다른 repo 에서 레거시 서버 인수·운영이 재현되면 active + SOP 승격."
---

## 패턴 (Pattern)

1. **사용자 붙여넣기 단계를 없앤다** — SSH 키 등록 + `ssh -A` 로 AI 가 직접 실행하고, 사용자 입력은 비밀번호만. 서버 블록이 로컬 탭에 붙거나(3회) 줄 단위로 계속 실행되는 사고(운영 사이트 빈 페이지 15~20분)가 이 단계에서 났다.
2. **변경 블록은 fail-closed** — `&&` 체인 · 한 블록 = 한 서버·같은 변수 · `cp -i` 별칭을 피해 `/bin/cp -f` · 판정은 상태 코드가 아니라 **본문 바이트 기준선**(지침 23 §1-9).
3. **웹루트 안에 백업을 두지 않는다** — 다중 확장자 처리로 `.php.bak` 이 PHP 로 실행된다.
4. **재시작이 복구 작업을 부를 수 있다** — `myisam-recover` 류 설정이면 재시작 중 사이트가 멈춘다(6분). 재시작 전 설정을 읽는다.
5. **감시 러너 지역 = 대상 지역**, 장애 판정 전 **자기 출구 IP** 확인(해외 러너 geo-block 으로 만든 기능을 다음 날 폐기).
6. **인프라 해지는 단계 게이트로** — 조회 전용 런북 → 결정 노트(Class B·롤백) → 컷오버 계획(롤백 5분) → 사후 검증 → 관찰 기간 → 해지 판정. 비가역 삭제는 마지막 단계에서 사람 승인.

## 근거 (Evidence)

cafe24-renewal 원격 셸 109분 11건 + 레거시 환경 함정 99분 11건. SSH 키 전환(11-02) 이후 붙여넣기 계열 재발 0.

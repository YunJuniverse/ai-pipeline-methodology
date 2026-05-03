# Migrations

`methodology sync`가 버전 간 자동 변환을 위해 실행하는 스크립트.

## 파일 명명

`v<from>_to_<to>.py` — 예: `v3.0_to_v3.1.py`

## 인터페이스

각 스크립트는 다음 함수를 정의해야 한다:

```python
def migrate(target: Path, dry_run: bool = False) -> None:
    """
    target: 대상 프로젝트 루트
    dry_run: True면 실제 변경하지 않고 로그만 출력
    """
    ...
```

## 멱등성 (Idempotency)

마이그레이션은 멱등이어야 한다 — 두 번 실행해도 같은 결과.
이미 적용된 상태면 skip하라.

## 실행 순서

`methodology sync`는 `.methodology-version`의 현재 버전부터 목표 버전까지의
모든 마이그레이션을 자동으로 체인 실행한다.

예: v2.5 → v3.1 호출 시 v2.5_to_v3.0.py → v3.0_to_v3.1.py 순서.

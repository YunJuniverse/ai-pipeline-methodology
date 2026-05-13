# _start/ — in-spire 진입점

> **더블클릭하면 dashboard 가 자동으로 열립니다.** 자기 OS에 맞는 파일만 사용.

## 사용법

### macOS
- `in-spire.app` 더블클릭
- 첫 실행 시 *"확인되지 않은 개발자"* 경고:
  - **우클릭 → 열기 → 열기** (1회만)
  - 또는 시스템 설정 → 보안 및 개인정보 보호 → *"그래도 열기"*

### Windows
- **첫 실행 1회**: `setup-windows.ps1` 우클릭 → *PowerShell 에서 실행*
  → `in-spire.lnk` (아이콘 박힌 바로가기) 자동 생성
- 이후: **`in-spire.lnk` 더블클릭**
- (대안) `in-spire.bat` 직접 더블클릭도 가능 (아이콘 없음)

### Linux
- **첫 실행 1회**: `bash setup-linux.sh`
  → `in-spire.desktop` 의 절대경로 자동 설정
- 이후 두 가지 선택:
  - `in-spire.sh` 직접 실행
  - `in-spire.desktop` 을 `~/.local/share/applications/` 에 복사 → 시스템 메뉴에서 검색

## 동작

모든 실행파일은 동일한 명령을 호출합니다:
```
python3 50_tools/methodology.py dashboard --open
```

즉:
1. 자동 포트 할당 (8765~8799)
2. background HTTP 서버 시작
3. dashboard.html 빌드 (현재 브랜치·commit 반영)
4. 기본 브라우저로 `http://localhost:<port>` 자동 열기

## 종료

```bash
python3 50_tools/methodology.py dashboard stop --all
```
또는 dashboard UI 의 **Local Dashboards** 카드에서 Stop 버튼.

## 폴더 구조

```
_start/
├── in-spire.app/        ← macOS 더블클릭
├── in-spire.bat         ← Windows 실행 스크립트
├── in-spire.ico         ← Windows 아이콘
├── setup-windows.ps1    ← Windows 1회 setup (.lnk 생성)
├── in-spire.lnk         ← (setup 후 생성됨) Windows 더블클릭
├── in-spire.sh          ← Linux 실행 스크립트
├── in-spire.desktop     ← Linux 데스크톱 항목
├── setup-linux.sh       ← Linux 1회 setup (경로 갱신)
└── icons/               ← 원본 PNG 보관 (1024×1024)
```

## 문제 해결

- **"50_tools/methodology.py not found"**: 본 `_start/` 폴더가 *방법론이 적용된 프로젝트 루트* 안에 있는지 확인.
- **dashboard 가 안 열림**: Python 3 설치 확인 (`python3 --version` / `python --version`).
- **이미 열려 있던 dashboard 와 충돌**: `python3 50_tools/methodology.py dashboard stop --all` 로 정리.

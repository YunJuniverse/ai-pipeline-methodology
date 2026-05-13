#!/usr/bin/env python3
"""build-launchers.py — in-spire 아이콘 3장으로 OS별 실행파일·아이콘 일괄 생성.

입력:
  <project_root>/in-spire-mac.png
  <project_root>/in-spire-win.png
  <project_root>/in-spire-linux.png

출력:
  <project_root>/_start/
  ├── in-spire.app/                 (macOS .app 번들 + .icns)
  ├── in-spire.bat                  (Windows 실행 스크립트)
  ├── in-spire.ico                  (Windows 아이콘 — 멀티 사이즈)
  ├── setup-windows.ps1             (Windows 사용자 1회 실행 — .lnk 생성)
  ├── in-spire.sh                   (Linux 실행 스크립트)
  ├── in-spire.desktop              (Linux 데스크톱 항목 템플릿)
  ├── setup-linux.sh                (Linux 사용자 1회 실행 — Exec/Icon 경로 갱신)
  ├── icons/
  │   ├── in-spire-mac.png          (원본 보관)
  │   ├── in-spire-win.png
  │   ├── in-spire-linux.png
  │   └── in-spire-256-linux.png    (Linux desktop 항목용 256×256)
  └── README.md                     (설치·실행 안내)
"""
from __future__ import annotations

import shutil
import subprocess
import sys
import textwrap
from pathlib import Path

from PIL import Image

ICONSET_SIZES_MAC = [
    ("icon_16x16.png", 16),
    ("icon_16x16@2x.png", 32),
    ("icon_32x32.png", 32),
    ("icon_32x32@2x.png", 64),
    ("icon_128x128.png", 128),
    ("icon_128x128@2x.png", 256),
    ("icon_256x256.png", 256),
    ("icon_256x256@2x.png", 512),
    ("icon_512x512.png", 512),
    ("icon_512x512@2x.png", 1024),
]

ICO_SIZES = [(16, 16), (24, 24), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)]


def info(msg: str) -> None:
    print(f"\033[36m[info]\033[0m {msg}")


def ok(msg: str) -> None:
    print(f"\033[32m[ok]\033[0m {msg}")


def err(msg: str) -> None:
    print(f"\033[31m[err]\033[0m {msg}", file=sys.stderr)


def build_icns(src_png: Path, dst_icns: Path) -> None:
    """macOS .icns 생성 — iconset 디렉터리 + iconutil."""
    iconset = dst_icns.parent / (dst_icns.stem + ".iconset")
    if iconset.exists():
        shutil.rmtree(iconset)
    iconset.mkdir(parents=True)

    img = Image.open(src_png).convert("RGBA")
    for name, size in ICONSET_SIZES_MAC:
        out = iconset / name
        resized = img.resize((size, size), Image.LANCZOS)
        resized.save(out, "PNG")

    subprocess.check_call(
        ["iconutil", "-c", "icns", str(iconset), "-o", str(dst_icns)],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    shutil.rmtree(iconset)
    ok(f"macOS .icns: {dst_icns}")


def build_ico(src_png: Path, dst_ico: Path) -> None:
    """Windows .ico 생성 — 멀티 사이즈 임베드."""
    img = Image.open(src_png).convert("RGBA")
    img.save(dst_ico, format="ICO", sizes=ICO_SIZES)
    ok(f"Windows .ico: {dst_ico}")


def build_macos_app(start_dir: Path, src_icns: Path) -> None:
    """macOS .app 번들 생성."""
    app = start_dir / "in-spire.app"
    if app.exists():
        shutil.rmtree(app)
    (app / "Contents" / "MacOS").mkdir(parents=True)
    (app / "Contents" / "Resources").mkdir(parents=True)

    # AppIcon.icns
    shutil.copy(src_icns, app / "Contents" / "Resources" / "AppIcon.icns")

    # Info.plist
    info_plist = textwrap.dedent("""\
        <?xml version="1.0" encoding="UTF-8"?>
        <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
        <plist version="1.0">
        <dict>
            <key>CFBundleName</key><string>in-spire</string>
            <key>CFBundleDisplayName</key><string>in-spire</string>
            <key>CFBundleIdentifier</key><string>com.in-spire.dashboard</string>
            <key>CFBundleVersion</key><string>1.0</string>
            <key>CFBundleShortVersionString</key><string>1.0</string>
            <key>CFBundleExecutable</key><string>in-spire</string>
            <key>CFBundleIconFile</key><string>AppIcon</string>
            <key>CFBundlePackageType</key><string>APPL</string>
            <key>LSMinimumSystemVersion</key><string>10.10</string>
            <key>NSHighResolutionCapable</key><true/>
        </dict>
        </plist>
    """)
    (app / "Contents" / "Info.plist").write_text(info_plist, encoding="utf-8")

    # MacOS/in-spire — shell script
    script = textwrap.dedent("""\
        #!/bin/bash
        # in-spire — methodology dashboard launcher (macOS)
        # 더블클릭 진입점. .app 번들 위치를 기준으로 프로젝트 루트 탐색.

        APP_BIN="${BASH_SOURCE[0]}"
        # APP_BIN: <ROOT>/_start/in-spire.app/Contents/MacOS/in-spire
        # 4단계 위 = 프로젝트 루트
        PROJECT_ROOT="$(cd "$(dirname "$APP_BIN")/../../../.." && pwd)"

        cd "$PROJECT_ROOT" || {
          osascript -e 'display alert "in-spire" message "프로젝트 루트로 cd 실패"'
          exit 1
        }

        if [ ! -f "50_tools/methodology.py" ]; then
          osascript -e 'display alert "in-spire" message "50_tools/methodology.py 미발견. 방법론이 적용된 프로젝트 루트에 .app 이 있는지 확인."'
          exit 1
        fi

        # 백그라운드 서빙 + 브라우저 자동 열기
        exec /usr/bin/env python3 50_tools/methodology.py dashboard --open
    """)
    script_path = app / "Contents" / "MacOS" / "in-spire"
    script_path.write_text(script, encoding="utf-8")
    script_path.chmod(0o755)

    ok(f"macOS .app: {app}")


def build_windows(start_dir: Path, src_ico: Path) -> None:
    """Windows .bat + setup-windows.ps1 (.lnk 자동 생성)."""
    bat = textwrap.dedent("""\
        @echo off
        REM in-spire — methodology dashboard launcher (Windows)
        REM Double-click entry point.

        cd /d "%~dp0\\.."

        if not exist "50_tools\\methodology.py" (
          echo [err] 50_tools\\methodology.py not found.
          echo Run this file inside a project where methodology is applied.
          pause
          exit /b 1
        )

        python 50_tools\\methodology.py dashboard --open
        echo.
        echo Dashboard is serving in the background. Stop with:
        echo   python 50_tools\\methodology.py dashboard stop --all
        pause
    """)
    (start_dir / "in-spire.bat").write_text(bat, encoding="utf-8")
    ok(f"Windows .bat: {start_dir / 'in-spire.bat'}")

    # PowerShell setup — .lnk 바로가기 자동 생성 (아이콘 박힘)
    ps1 = textwrap.dedent(r"""
        # setup-windows.ps1 — in-spire.lnk 바로가기 자동 생성 (아이콘 임베드)
        # 사용자 1회 실행:
        #   1. _start 폴더에서 우클릭 → PowerShell 에서 실행
        #   2. 또는: powershell -ExecutionPolicy Bypass -File .\setup-windows.ps1

        $here = Split-Path -Parent $MyInvocation.MyCommand.Path
        $batPath = Join-Path $here "in-spire.bat"
        $icoPath = Join-Path $here "in-spire.ico"
        $lnkPath = Join-Path $here "in-spire.lnk"

        if (-not (Test-Path $batPath)) {
            Write-Host "[err] in-spire.bat not found in $here" -ForegroundColor Red
            exit 1
        }

        $shell = New-Object -ComObject WScript.Shell
        $lnk = $shell.CreateShortcut($lnkPath)
        $lnk.TargetPath = $batPath
        $lnk.WorkingDirectory = $here
        if (Test-Path $icoPath) {
            $lnk.IconLocation = "$icoPath,0"
        }
        $lnk.Description = "in-spire — methodology dashboard launcher"
        $lnk.Save()

        Write-Host "[ok] Created in-spire.lnk with icon at $lnkPath" -ForegroundColor Green
        Write-Host "Double-click in-spire.lnk to launch the dashboard."
    """).strip() + "\n"
    (start_dir / "setup-windows.ps1").write_text(ps1, encoding="utf-8")
    ok(f"Windows setup: {start_dir / 'setup-windows.ps1'}")


def build_linux(start_dir: Path, src_png_linux: Path) -> None:
    """Linux .sh + .desktop + setup-linux.sh."""
    # 256×256 PNG (.desktop 표준 사이즈)
    img = Image.open(src_png_linux).convert("RGBA")
    icon_256 = start_dir / "icons" / "in-spire-256-linux.png"
    icon_256.parent.mkdir(parents=True, exist_ok=True)
    img.resize((256, 256), Image.LANCZOS).save(icon_256, "PNG")

    # in-spire.sh
    sh = textwrap.dedent("""\
        #!/bin/bash
        # in-spire — methodology dashboard launcher (Linux)
        SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
        PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"
        cd "$PROJECT_ROOT" || exit 1
        if [ ! -f "50_tools/methodology.py" ]; then
          echo "[err] 50_tools/methodology.py not found"
          exit 1
        fi
        exec /usr/bin/env python3 50_tools/methodology.py dashboard --open
    """)
    sh_path = start_dir / "in-spire.sh"
    sh_path.write_text(sh, encoding="utf-8")
    sh_path.chmod(0o755)
    ok(f"Linux .sh: {sh_path}")

    # .desktop 템플릿 — setup-linux.sh 가 절대경로로 변환
    desktop = textwrap.dedent("""\
        [Desktop Entry]
        Type=Application
        Version=1.0
        Name=in-spire
        Comment=Methodology dashboard launcher
        Exec=__EXEC__
        Icon=__ICON__
        Terminal=false
        Categories=Development;
    """)
    (start_dir / "in-spire.desktop").write_text(desktop, encoding="utf-8")
    ok(f"Linux .desktop template: {start_dir / 'in-spire.desktop'}")

    # setup-linux.sh — Exec/Icon 절대경로 자동 갱신
    setup = textwrap.dedent("""\
        #!/bin/bash
        # setup-linux.sh — in-spire.desktop 의 Exec/Icon 을 현재 절대경로로 갱신.
        # 사용자 1회 실행:
        #   bash setup-linux.sh
        # 그 후 in-spire.desktop 을 ~/.local/share/applications/ 에 복사하면 메뉴 등록.

        HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
        EXEC_PATH="$HERE/in-spire.sh"
        ICON_PATH="$HERE/icons/in-spire-256-linux.png"

        sed -e "s|__EXEC__|$EXEC_PATH|" -e "s|__ICON__|$ICON_PATH|" \\
          "$HERE/in-spire.desktop" > "$HERE/in-spire.desktop.tmp"
        mv "$HERE/in-spire.desktop.tmp" "$HERE/in-spire.desktop"

        echo "[ok] in-spire.desktop updated:"
        echo "  Exec=$EXEC_PATH"
        echo "  Icon=$ICON_PATH"
        echo ""
        echo "To register in app menu:"
        echo "  cp $HERE/in-spire.desktop ~/.local/share/applications/"
        echo "  chmod +x $HERE/in-spire.sh"
    """)
    setup_path = start_dir / "setup-linux.sh"
    setup_path.write_text(setup, encoding="utf-8")
    setup_path.chmod(0o755)
    ok(f"Linux setup: {setup_path}")


def write_start_readme(start_dir: Path) -> None:
    readme = textwrap.dedent("""\
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
        """)
    (start_dir / "README.md").write_text(readme, encoding="utf-8")
    ok(f"_start/README.md")


def main(argv: list[str]) -> int:
    root = Path(argv[1]).resolve() if len(argv) > 1 else Path.cwd().resolve()
    info(f"project root: {root}")

    sources = {
        "mac": root / "in-spire-mac.png",
        "win": root / "in-spire-win.png",
        "linux": root / "in-spire-linux.png",
    }
    for name, p in sources.items():
        if not p.exists():
            err(f"미발견: {p}")
            return 1

    start_dir = root / "_start"
    start_dir.mkdir(exist_ok=True)
    icons_dir = start_dir / "icons"
    icons_dir.mkdir(exist_ok=True)

    # 원본 PNG 보관
    for name, p in sources.items():
        shutil.copy(p, icons_dir / p.name)
    ok(f"원본 PNG 3장 보관: {icons_dir}")

    # macOS — .icns + .app
    icns = start_dir / "AppIcon.icns"
    build_icns(sources["mac"], icns)
    build_macos_app(start_dir, icns)
    icns.unlink()  # .app 내부로 이동했으니 정리

    # Windows — .ico + .bat + setup.ps1
    build_ico(sources["win"], start_dir / "in-spire.ico")
    build_windows(start_dir, start_dir / "in-spire.ico")

    # Linux — .sh + .desktop + setup.sh + 256 PNG
    build_linux(start_dir, sources["linux"])

    # README
    write_start_readme(start_dir)

    print()
    ok("빌드 완료. _start/ 구조:")
    for item in sorted(start_dir.rglob("*")):
        rel = item.relative_to(start_dir)
        depth = len(rel.parts) - 1
        prefix = "  " + "  " * depth + ("📁 " if item.is_dir() else "📄 ")
        print(f"{prefix}{rel.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))

#!/usr/bin/env python3
"""build-launchers.py — in-spire 아이콘 3장으로 OS별 실행파일·아이콘 일괄 생성.

입력 (탐색 순서):
  1. <project_root>/_start/assets/icons/in-spire-{mac,win,linux}.png  (영구 원본)
  2. <project_root>/in-spire-{mac,win,linux}.png                     (최초 빌드 시)

출력 구조 (clean rebuild — 기존 _start 의 옛 파일은 자동 제거):
  <project_root>/_start/
  ├── in-spire (mac).app/        ← macOS 더블클릭 진입점
  ├── in-spire (windows).bat     ← Windows 직접 실행
  ├── in-spire (linux).sh        ← Linux 실행
  ├── setup-windows.ps1          ← Windows 1회 (.lnk 생성)
  ├── setup-linux.sh             ← Linux 1회 (.desktop 경로 갱신)
  ├── README.md                  ← 사용 안내
  └── assets/                    ← 아이콘·메타·원본
      ├── icons/
      │   ├── in-spire-mac.png         (1024×1024)
      │   ├── in-spire-win.png         (1024×1024)
      │   ├── in-spire-linux.png       (1024×1024)
      │   └── in-spire-256-linux.png   (256×256 — .desktop 표준)
      ├── in-spire.ico               (Windows 멀티 사이즈)
      └── in-spire.desktop           (Linux 데스크톱 항목 템플릿)
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

# 파일명 — 사용자 명시 표기: (mac) (windows) (linux)
NAME_APP = "in-spire (mac).app"
NAME_BAT = "in-spire (windows).bat"
NAME_SH = "in-spire (linux).sh"


def info(msg: str) -> None: print(f"\033[36m[info]\033[0m {msg}")
def ok(msg: str) -> None: print(f"\033[32m[ok]\033[0m {msg}")
def warn(msg: str) -> None: print(f"\033[33m[warn]\033[0m {msg}")
def err(msg: str) -> None: print(f"\033[31m[err]\033[0m {msg}", file=sys.stderr)


def find_source_pngs(root: Path) -> dict[str, Path]:
    """3장 원본 PNG 탐색 — assets/icons 우선, 루트 fallback."""
    persistent = root / "_start" / "assets" / "icons"
    legacy_root = root
    sources: dict[str, Path] = {}
    for variant in ("mac", "win", "linux"):
        candidates = [
            persistent / f"in-spire-{variant}.png",
            legacy_root / f"in-spire-{variant}.png",
        ]
        for c in candidates:
            if c.exists():
                sources[variant] = c
                break
        else:
            err(f"in-spire-{variant}.png 미발견. 다음 중 하나여야: {[str(c) for c in candidates]}")
            sys.exit(1)
    return sources


def build_icns(src_png: Path, dst_icns: Path) -> None:
    iconset = dst_icns.parent / (dst_icns.stem + ".iconset")
    if iconset.exists():
        shutil.rmtree(iconset)
    iconset.mkdir(parents=True)
    img = Image.open(src_png).convert("RGBA")
    for name, size in ICONSET_SIZES_MAC:
        img.resize((size, size), Image.LANCZOS).save(iconset / name, "PNG")
    subprocess.check_call(
        ["iconutil", "-c", "icns", str(iconset), "-o", str(dst_icns)],
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
    )
    shutil.rmtree(iconset)
    ok(f"macOS .icns: {dst_icns.name}")


def build_ico(src_png: Path, dst_ico: Path) -> None:
    img = Image.open(src_png).convert("RGBA")
    img.save(dst_ico, format="ICO", sizes=ICO_SIZES)
    ok(f"Windows .ico: {dst_ico.name}")


def build_macos_app(start_dir: Path, src_icns: Path) -> None:
    app = start_dir / NAME_APP
    if app.exists():
        shutil.rmtree(app)
    (app / "Contents" / "MacOS").mkdir(parents=True)
    (app / "Contents" / "Resources").mkdir(parents=True)

    shutil.copy(src_icns, app / "Contents" / "Resources" / "AppIcon.icns")

    info_plist = textwrap.dedent("""\
        <?xml version="1.0" encoding="UTF-8"?>
        <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
        <plist version="1.0">
        <dict>
            <key>CFBundleName</key><string>in-spire</string>
            <key>CFBundleDisplayName</key><string>in-spire (mac)</string>
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

    script = textwrap.dedent("""\
        #!/bin/bash
        # in-spire — methodology dashboard launcher (macOS)
        # 더블클릭 진입점. .app 번들 위치 기준 프로젝트 루트 탐색.

        APP_BIN="${BASH_SOURCE[0]}"
        # APP_BIN: <ROOT>/_start/in-spire (mac).app/Contents/MacOS/in-spire
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

        exec /usr/bin/env python3 50_tools/methodology.py dashboard --open
    """)
    script_path = app / "Contents" / "MacOS" / "in-spire"
    script_path.write_text(script, encoding="utf-8")
    script_path.chmod(0o755)
    ok(f"macOS .app: {app.name}")


def build_windows(start_dir: Path) -> None:
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
    (start_dir / NAME_BAT).write_text(bat, encoding="utf-8")
    ok(f"Windows: {NAME_BAT}")

    # setup-windows.ps1 — .lnk 자동 생성 (assets/in-spire.ico 참조)
    ps1 = textwrap.dedent(r"""
        # setup-windows.ps1 — in-spire (windows).lnk 바로가기 자동 생성 (아이콘 임베드)
        # 사용자 1회 실행:
        #   1. _start 폴더에서 우클릭 → PowerShell 에서 실행
        #   2. 또는: powershell -ExecutionPolicy Bypass -File .\setup-windows.ps1

        $here = Split-Path -Parent $MyInvocation.MyCommand.Path
        $batPath = Join-Path $here "in-spire (windows).bat"
        $icoPath = Join-Path $here "assets\in-spire.ico"
        $lnkPath = Join-Path $here "in-spire (windows).lnk"

        if (-not (Test-Path $batPath)) {
            Write-Host "[err] in-spire (windows).bat not found in $here" -ForegroundColor Red
            exit 1
        }

        $shell = New-Object -ComObject WScript.Shell
        $lnk = $shell.CreateShortcut($lnkPath)
        $lnk.TargetPath = $batPath
        $lnk.WorkingDirectory = $here
        if (Test-Path $icoPath) {
            $lnk.IconLocation = "$icoPath,0"
        }
        $lnk.Description = "in-spire — methodology dashboard launcher (Windows)"
        $lnk.Save()

        Write-Host "[ok] Created 'in-spire (windows).lnk' with icon at $lnkPath" -ForegroundColor Green
        Write-Host "Double-click the .lnk to launch the dashboard."
    """).strip() + "\n"
    (start_dir / "setup-windows.ps1").write_text(ps1, encoding="utf-8")
    ok("Windows setup: setup-windows.ps1")


def build_linux(start_dir: Path, src_png_linux: Path, assets_dir: Path) -> None:
    # 256×256 PNG (.desktop 표준)
    img = Image.open(src_png_linux).convert("RGBA")
    icon_256 = assets_dir / "icons" / "in-spire-256-linux.png"
    icon_256.parent.mkdir(parents=True, exist_ok=True)
    img.resize((256, 256), Image.LANCZOS).save(icon_256, "PNG")

    # in-spire (linux).sh — 셸 스크립트
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
    sh_path = start_dir / NAME_SH
    sh_path.write_text(sh, encoding="utf-8")
    sh_path.chmod(0o755)
    ok(f"Linux: {NAME_SH}")

    # .desktop 템플릿 — Exec/Icon 토큰, setup-linux.sh 가 sed 로 치환
    desktop = textwrap.dedent("""\
        [Desktop Entry]
        Type=Application
        Version=1.0
        Name=in-spire (linux)
        Comment=Methodology dashboard launcher
        Exec=__EXEC__
        Icon=__ICON__
        Terminal=false
        Categories=Development;
    """)
    (assets_dir / "in-spire.desktop").write_text(desktop, encoding="utf-8")
    ok("Linux .desktop template: assets/in-spire.desktop")

    # setup-linux.sh — Exec/Icon 절대경로 자동 갱신
    setup = textwrap.dedent("""\
        #!/bin/bash
        # setup-linux.sh — in-spire.desktop 의 Exec/Icon 을 현재 절대경로로 갱신.
        # 사용자 1회 실행:
        #   bash setup-linux.sh
        # 그 후 assets/in-spire.desktop 을 ~/.local/share/applications/ 에 복사.

        HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
        EXEC_PATH="$HERE/in-spire (linux).sh"
        ICON_PATH="$HERE/assets/icons/in-spire-256-linux.png"
        DESKTOP_FILE="$HERE/assets/in-spire.desktop"

        if [ ! -f "$DESKTOP_FILE" ]; then
          echo "[err] $DESKTOP_FILE not found"
          exit 1
        fi

        # 공백 포함 경로 안전 처리 — | 구분자
        sed -e "s|__EXEC__|$EXEC_PATH|" -e "s|__ICON__|$ICON_PATH|" \\
          "$DESKTOP_FILE" > "$DESKTOP_FILE.tmp"
        mv "$DESKTOP_FILE.tmp" "$DESKTOP_FILE"

        echo "[ok] $DESKTOP_FILE updated:"
        echo "  Exec=$EXEC_PATH"
        echo "  Icon=$ICON_PATH"
        echo ""
        echo "To register in app menu:"
        echo "  cp \\"$DESKTOP_FILE\\" ~/.local/share/applications/"
    """)
    setup_path = start_dir / "setup-linux.sh"
    setup_path.write_text(setup, encoding="utf-8")
    setup_path.chmod(0o755)
    ok("Linux setup: setup-linux.sh")


def write_start_readme(start_dir: Path) -> None:
    readme = textwrap.dedent("""\
        # _start/ — in-spire 진입점

        > **자기 OS 에 맞는 파일을 더블클릭하면 dashboard 가 자동으로 열립니다.**

        ## 진입점

        | OS | 파일 | 사용법 |
        |---|---|---|
        | **macOS** | `in-spire (mac).app` | 더블클릭 ⭐ |
        | **Windows** | `in-spire (windows).bat` (또는 `.lnk` setup 후) | 더블클릭 |
        | **Linux** | `in-spire (linux).sh` | 실행 또는 `.desktop` 메뉴 등록 |

        ## OS 별 1회 설치 (필요한 경우만)

        ### macOS
        첫 실행 시 *"확인되지 않은 개발자"* 경고:
        - **우클릭 → 열기 → 열기** (1회만)
        - 또는 시스템 설정 → 보안 및 개인정보 → *"그래도 열기"*

        ### Windows
        1. `setup-windows.ps1` 우클릭 → *PowerShell 에서 실행*
        2. `in-spire (windows).lnk` (아이콘 박힌 바로가기) 자동 생성
        3. 이후: `.lnk` 또는 `.bat` 더블클릭

        ### Linux
        1. `bash setup-linux.sh` 실행 (`.desktop` 의 절대경로 갱신)
        2. 다음 중 선택:
           - `./in-spire (linux).sh` 직접 실행
           - `cp assets/in-spire.desktop ~/.local/share/applications/` (시스템 메뉴 등록)

        ## 동작

        모든 실행파일은 동일한 명령을 호출:
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
        ├── in-spire (mac).app/          ← macOS 더블클릭
        ├── in-spire (windows).bat       ← Windows 더블클릭
        ├── in-spire (linux).sh          ← Linux 실행
        ├── setup-windows.ps1            ← Windows 1회 (.lnk 생성)
        ├── setup-linux.sh               ← Linux 1회 (.desktop 경로)
        ├── README.md                    ← 본 문서
        └── assets/                      ← 아이콘·메타·원본
            ├── icons/
            │   ├── in-spire-mac.png     (1024×1024)
            │   ├── in-spire-win.png
            │   ├── in-spire-linux.png
            │   └── in-spire-256-linux.png  (Linux .desktop 용)
            ├── in-spire.ico             (Windows 멀티 사이즈)
            └── in-spire.desktop         (Linux 데스크톱 항목)
        ```

        ## 문제 해결

        - **"50_tools/methodology.py not found"**: 본 `_start/` 폴더가 *방법론 적용 프로젝트 루트* 안에 있는지 확인.
        - **Python 3 미설치**: `python3 --version` 으로 확인.
        - **이미 떠 있던 dashboard 충돌**: `python3 50_tools/methodology.py dashboard stop --all` 로 정리.
        """)
    (start_dir / "README.md").write_text(readme, encoding="utf-8")
    ok("README.md")


def clean_legacy(start_dir: Path) -> None:
    """기존 _start/ 의 옛 파일·구조 제거 (clean rebuild)."""
    legacy_items = [
        "in-spire.app",
        "in-spire.bat",
        "in-spire.sh",
        "in-spire.desktop",
        "in-spire.ico",
        "icons",  # 옛 위치 (assets/icons 로 이동)
    ]
    for item in legacy_items:
        p = start_dir / item
        if p.exists():
            if p.is_dir():
                shutil.rmtree(p)
            else:
                p.unlink()
            info(f"  removed legacy: {item}")


def main(argv: list[str]) -> int:
    root = Path(argv[1]).resolve() if len(argv) > 1 else Path.cwd().resolve()
    info(f"project root: {root}")

    sources = find_source_pngs(root)
    info(f"sources: {[str(p.relative_to(root)) for p in sources.values()]}")

    start_dir = root / "_start"
    start_dir.mkdir(exist_ok=True)
    assets = start_dir / "assets"
    assets.mkdir(exist_ok=True)
    (assets / "icons").mkdir(exist_ok=True)

    # 1) 기존 옛 구조 정리
    info("cleaning legacy structure...")
    clean_legacy(start_dir)

    # 2) 원본 PNG 영구 보관 (assets/icons/)
    for variant, src in sources.items():
        dst = assets / "icons" / f"in-spire-{variant}.png"
        if src.resolve() != dst.resolve():
            shutil.copy(src, dst)
    ok(f"원본 PNG 영구 보관: assets/icons/")

    # 3) macOS — .icns + .app
    icns_tmp = assets / "AppIcon.icns"
    build_icns(assets / "icons" / "in-spire-mac.png", icns_tmp)
    build_macos_app(start_dir, icns_tmp)
    icns_tmp.unlink()  # .app 내부로 복사됨

    # 4) Windows — .ico + .bat + setup.ps1
    build_ico(assets / "icons" / "in-spire-win.png", assets / "in-spire.ico")
    build_windows(start_dir)

    # 5) Linux — .sh + .desktop + setup.sh + 256 PNG
    build_linux(start_dir, assets / "icons" / "in-spire-linux.png", assets)

    # 6) README
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

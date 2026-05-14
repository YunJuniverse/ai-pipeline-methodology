# mig-no-replace: 본 스크립트는 path-replace 대상에서 제외 (PATH_MAP 가 self-ref 되지 않도록)
"""v3.2 -> v4.0 마이그레이션 — 폴더 +10 shift + 00_briefs 신설.

변경 요약 (v3.2 옛 폴더명 -> v4.0 새 폴더명):
- 옛0,0_foundation/  ->  10_foundation/
- 옛1,0_guides/      ->  20_guides/
- 옛2,0_planning/    ->  30_planning/
- 옛3,0_dev/         ->  40_dev/
- 옛4,0_resources/   ->  50_resources/
- 옛5,0_tools/       ->  60_tools/
- 옛6,0_meta/        ->  70_meta/      (메타-방법론 격리 유지)
- 9,0_archive/       ->  9,0_archive/   (변경 없음)
- 00_briefs/         ->  신규 — 인간 입력 (리서치·아이디어노트·회의록)

모든 .py / .md / .json / .yml / .yaml / .toml / .ini / .desktop / .plist / .sh / .bat / .ps1
파일 본문에서 'NN_<name>/' 패턴을 새 매핑으로 일괄 치환.

멱등성: 이미 v4.0 (`10_foundation/` 존재 + `00_foundation/` 부재) 이면 skip.
주입 격리: 70_meta 는 적용 프로젝트로 안 옮겨가야 — 본 마이그레이션이 *생성* 하지 않음.
"""
from __future__ import annotations

import re
import shutil
import subprocess
from pathlib import Path
from typing import Iterable


# 옛 폴더명 -> 새 폴더명 매핑. 본 스크립트 자체는 path-replace 제외 처리됨.
PATH_MAP: dict[str, str] = {
    chr(48) + chr(48) + "_foundation": "10_foundation",
    chr(49) + chr(48) + "_guides": "20_guides",
    chr(50) + chr(48) + "_planning": "30_planning",
    chr(51) + chr(48) + "_dev": "40_dev",
    chr(52) + chr(48) + "_resources": "50_resources",
    chr(53) + chr(48) + "_tools": "60_tools",
    chr(54) + chr(48) + "_meta": "70_meta",
}

# 본문 치환 대상 파일 확장자
TEXT_EXTENSIONS = {
    ".py", ".md", ".json", ".yml", ".yaml", ".toml", ".ini",
    ".desktop", ".plist", ".sh", ".bat", ".ps1", ".txt", ".cfg",
}

# 디렉터리 단위 제외 (rename·치환 모두 skip)
EXCLUDE_DIRS = {
    ".git", "node_modules", ".cache", ".venv", "venv", "__pycache__",
    ".methodology-cache", ".pytest_cache", ".next", "dist", "build",
}


def _log(msg: str, dry: bool) -> None:
    prefix = "[migrate v3.2→v4.0]"
    print(f"{prefix} {'(dry-run) ' if dry else ''}{msg}")


def _path_replace_pattern() -> re.Pattern[str]:
    """긴 매칭 우선 — 정확한 폴더명 매칭 (앞에 슬래시·시작·따옴표 등 OK, 뒤에 슬래시·끝)."""
    keys = sorted(PATH_MAP.keys(), key=len, reverse=True)
    return re.compile(r'(?<![\w-])(' + '|'.join(re.escape(k) for k in keys) + r')(?![\w-])')


def _replace_in_text(content: str, pat: re.Pattern[str]) -> str:
    return pat.sub(lambda m: PATH_MAP[m.group(1)], content)


def _is_text_file(path: Path) -> bool:
    return path.suffix.lower() in TEXT_EXTENSIONS


def _iter_files(root: Path) -> Iterable[Path]:
    for p in root.rglob("*"):
        if not p.is_file():
            continue
        # 디렉터리 단위 제외
        parts = set(p.relative_to(root).parts)
        if parts & EXCLUDE_DIRS:
            continue
        yield p


def _rename_folders(target: Path, dry_run: bool) -> int:
    """폴더 rename — git mv 우선, fallback 일반 mv."""
    renamed = 0
    has_git = (target / ".git").exists()
    # 긴 이름 우선 (cascade 회피)
    for old in sorted(PATH_MAP.keys(), key=len, reverse=True):
        old_path = target / old
        new_path = target / PATH_MAP[old]
        if not old_path.exists():
            continue
        if new_path.exists():
            _log(f"skip rename — 이미 존재: {new_path.relative_to(target)}", dry_run)
            continue
        _log(f"rename: {old} → {PATH_MAP[old]}", dry_run)
        if not dry_run:
            if has_git:
                try:
                    subprocess.check_call(
                        ["git", "-C", str(target), "mv", old, PATH_MAP[old]],
                        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
                    )
                except subprocess.CalledProcessError:
                    # untracked 폴더면 일반 mv
                    shutil.move(str(old_path), str(new_path))
            else:
                shutil.move(str(old_path), str(new_path))
        renamed += 1
    return renamed


def _replace_paths_in_files(target: Path, dry_run: bool) -> int:
    pat = _path_replace_pattern()
    touched = 0
    for f in _iter_files(target):
        if not _is_text_file(f):
            continue
        try:
            old_text = f.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        new_text = _replace_in_text(old_text, pat)
        if new_text != old_text:
            if not dry_run:
                f.write_text(new_text, encoding="utf-8")
            touched += 1
    _log(f"path-replace: {touched} files", dry_run)
    return touched


def _create_briefs(target: Path, dry_run: bool) -> None:
    briefs = target / "00_briefs"
    if briefs.exists():
        _log("00_briefs/ 이미 존재 — skip 신설", dry_run)
        return
    _log("create 00_briefs/{current,archived,meetings} + _README.md", dry_run)
    if dry_run:
        return
    (briefs / "current").mkdir(parents=True, exist_ok=True)
    (briefs / "archived").mkdir(exist_ok=True)
    (briefs / "meetings").mkdir(exist_ok=True)
    (briefs / "_README.md").write_text(_BRIEFS_README, encoding="utf-8")


_BRIEFS_README = """\
---
doc_id: briefs-readme
title: 00_briefs/ — 인간 입력 (브리프·리서치·아이디어·회의록)
version: v1.0.0
status: active
last_updated: 2026-05-14
ai_relevance: rule
---

# 00_briefs/ — 인간 입력 공간

> **사용자가 raw 메모·기획·리서치를 던지면, AI 가 매 세션·필요 시 다시 읽고 반영한다.**
> 위상: 모든 작업의 *출발점*. 백서 §3-G1 단일 진입점.

---

## 1. 무엇을 넣는가

| 종류 | 예시 |
|---|---|
| **아이디어 노트** | "사용자 onboarding 단순화 해보면 어떨까" |
| **리서치 결과** | 시장 분석·경쟁사 조사·기술 문서 요약 |
| **회의록** | 사용자 인터뷰·내부 회의 내용 |
| **참고 자료 링크** | URL·PDF 경로 (raw 인용 OK) |
| **방향성 선언** | "이번 분기는 X 에 집중" |

→ *정형 산출물* 은 아님. **raw·자유 형식 OK**. AI 가 읽고 *기획서·개발 산출물* 로 변환.

## 2. 어디에 넣는가

```
00_briefs/
├── _README.md              ← 본 문서
├── current/                ← 활성 브리프 (AI 가 매 세션 읽음)
│   ├── YYYY-MM-DD_<topic>.md
│   └── ...
├── archived/               ← 옛 브리프 (참고용 보관)
└── meetings/               ← 회의록 (선택)
    └── YYYY-MM-DD_<topic>.md
```

**파일명 컨벤션**: `YYYY-MM-DD_<topic-slug>.md` — 시간 순 자동 정렬.

## 3. AI 가 언제 읽는가

| 시점 | 동작 |
|---|---|
| **매 세션 시작** | `.ai/context.json` `must_read_optional` 에 `00_briefs/current/*.md` 자동 포함 |
| **사용자 요청 시** | "브리프 다시 봐줘" → AI 가 `current/` 전체 재로드 |
| **자동 트리거 (향후)** | brief 파일 mtime 변경 감지 → 다음 세션에 highlight |

## 4. 갱신 패턴

- 인간이 *수시로* `current/` 에 새 파일 추가 또는 기존 파일 수정
- 일정 기간 후 (인간 판단) `archived/` 로 이동
- *삭제 금지* — 옛 맥락도 학습 데이터

## 5. AI 측 규칙 (CLAUDE.md / AGENTS.md 반영)

- **세션 부팅 시** must_read 로 `current/*.md` 일별 정렬 후 *전부 읽음*
- 작업 진행 중 *그 브리프 내용을 어떻게 반영했는지* 명시 (예: "TALMOCOM-042 는 2026-05-14_onboarding.md 의 §3 반영")
- *옛 브리프와 충돌* 발생 시 사용자에게 확인 — 자동 결정 금지

## 6. 안티패턴

- ❌ 정형 산출물을 brief 에 넣음 — `30_planning/` 또는 `40_dev/` 로
- ❌ 비밀번호·API 키 — `.env` 또는 secret manager 사용
- ❌ 너무 길게 — 1 파일 200줄 이내 권장 (긴 리서치는 `40_dev/snapshots/` 또는 외부 링크)
- ❌ archived 삭제 — 학습 데이터 손실

## 7. 첫 시드

신규 프로젝트면 `current/` 비어있음. 사용자가 첫 브리프 1장 던지면 AI 가 그걸 baseline 으로 작업 시작.
"""


def migrate(target: Path, dry_run: bool = False) -> None:
    target = target.resolve()
    _log(f"target: {target}", dry_run)

    # 이미 v4.0 인지 확인 — 10_foundation 존재 + 10_foundation 부재
    if (target / "10_foundation").exists() and not (target / "10_foundation").exists():
        _log("이미 v4.0 — skip", dry_run)
        _create_briefs(target, dry_run)  # briefs 만 보장
        return

    # 1) 폴더 rename
    renamed = _rename_folders(target, dry_run)
    _log(f"renamed {renamed} folders", dry_run)

    # 2) 모든 텍스트 파일 path 일괄 치환
    _replace_paths_in_files(target, dry_run)

    # 3) 00_briefs/ 신설
    _create_briefs(target, dry_run)

    _log("완료.", dry_run)


if __name__ == "__main__":
    import sys
    dry = "--dry-run" in sys.argv
    target = Path(sys.argv[1]) if len(sys.argv) > 1 and not sys.argv[1].startswith("--") else Path.cwd()
    migrate(target, dry_run=dry)

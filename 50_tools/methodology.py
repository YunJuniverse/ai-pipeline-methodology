#!/usr/bin/env python3
"""methodology — CLI for distributing & updating the methodology in projects.

Commands
--------
  methodology init <path> --type fullstack|planning-only [--label NAME]
      새 프로젝트에 방법론을 주입한다.

  methodology sync [--apply] [--target <version>]
      현재 폴더(.methodology-version 보유)를 업스트림과 동기화한다.
      --apply 없이 호출하면 변경 미리보기만 출력 (드라이런).

  methodology status
      적용된 버전과 업스트림 버전을 비교한다.

  methodology diff <path>
      특정 파일에서 sync가 어떤 변경을 가할지 단일 파일 diff 표시.

  methodology version
      이 메소돌로지 자신의 버전을 출력한다.

Classification
--------------
  shared          — sync가 항상 덮어쓴다 (10_guides/, 40_resources/, 그래프, 대시보드)
  init_scaffolds  — init이 1회 생성, sync는 절대 안 건드린다 (20_planning/, 30_dev/)
  managed         — sync가 마커 사이만 머지한다 (CLAUDE.md, AGENTS.md)
  project_local   — 프로젝트 산출물, sync 무관 (HANDOFF/TODO/code/...)

Markers
-------
  managed 파일에서 다음 마커 쌍 사이만 sync가 갱신한다:

      <!-- methodology:managed:start id=<block-id> -->
      ...
      <!-- methodology:managed:end -->
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import re
import shutil
import subprocess
import sys
from datetime import date
from difflib import unified_diff
from pathlib import Path
from typing import Callable

# ─── 메소돌로지 자체 버전 ───────────────────────────────────────────────────
METHODOLOGY_VERSION = "v3.1"

METHODOLOGY_ROOT = Path(__file__).resolve().parent.parent

# ─── 매니페스트 ─────────────────────────────────────────────────────────────
MANIFEST = {
    # sync가 항상 덮어쓰는 디렉터리·파일 (재귀 복사)
    "shared_paths": [
        "10_guides",
        "40_resources/templates",
        "40_resources/prompts",
        "50_tools/methodology-graph.json",
        "50_tools/generate-dashboard.py",
        "50_tools/methodology.py",
    ],
    # init이 1회 생성하는 디렉터리·파일 (sync 무시)
    "init_paths": [
        "20_planning",
        "30_dev",
    ],
    # init이 src→dst 매핑으로 복사하는 단일 파일들 (PROJECT_NAME 치환 가능)
    "init_files": [
        # (src_in_methodology, dst_in_project, substitute)
        ("CLAUDE.md", "CLAUDE.md", True),
        ("AGENTS.md", "AGENTS.md", True),
        ("40_resources/templates/HANDOFF.md", "HANDOFF.md", True),
        ("40_resources/templates/TODO.md", "TODO.md", True),
    ],
    # sync가 마커 사이만 머지하는 파일
    "managed_files": [
        "CLAUDE.md",
        "AGENTS.md",
    ],
}

MARKER_RE = re.compile(
    r"<!--\s*methodology:managed:start\s+id=([\w\-]+)\s*-->(.*?)<!--\s*methodology:managed:end\s*-->",
    re.DOTALL,
)

VERSION_FILE_NAME = ".methodology-version"


# ─── 유틸 ───────────────────────────────────────────────────────────────────


def info(msg: str) -> None:
    print(f"\033[36m[info]\033[0m {msg}")


def ok(msg: str) -> None:
    print(f"\033[32m[ok]\033[0m {msg}")


def warn(msg: str) -> None:
    print(f"\033[33m[warn]\033[0m {msg}")


def err(msg: str) -> None:
    print(f"\033[31m[err]\033[0m {msg}", file=sys.stderr)


def read_text(p: Path) -> str:
    return p.read_text(encoding="utf-8")


def write_text(p: Path, content: str) -> None:
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content, encoding="utf-8")


def upstream_commit() -> str:
    try:
        return subprocess.check_output(
            ["git", "-C", str(METHODOLOGY_ROOT), "rev-parse", "--short", "HEAD"],
            text=True,
        ).strip()
    except Exception:
        return "unknown"


def substitute(content: str, label: str, mode: str | None, today: str) -> str:
    out = content.replace("[PROJECT_NAME]", label)
    if mode:
        out = out.replace("[fullstack / planning-only]", mode)
        out = out.replace("[PROJECT_MODE]", mode)
    out = out.replace("[YYYY-MM-DD]", today)
    return out


# ─── 마커 머지 ──────────────────────────────────────────────────────────────


def parse_managed_blocks(text: str) -> dict[str, str]:
    return {m.group(1): m.group(0) for m in MARKER_RE.finditer(text)}


def merge_managed(source_text: str, target_text: str) -> tuple[str, dict]:
    """target의 마커 블록을 source의 같은 id 블록으로 교체.

    반환: (새 target_text, 통계 dict)
    """
    src_blocks = parse_managed_blocks(source_text)
    tgt_blocks = parse_managed_blocks(target_text)

    replaced = 0
    untouched = 0
    deprecated = []  # target에는 있지만 source에 없는 id

    def _sub(m: re.Match) -> str:
        nonlocal replaced, untouched
        block_id = m.group(1)
        if block_id in src_blocks:
            new_block = src_blocks[block_id]
            if new_block.strip() == m.group(0).strip():
                untouched += 1
            else:
                replaced += 1
            return new_block
        deprecated.append(block_id)
        return m.group(0)

    new_text = MARKER_RE.sub(_sub, target_text)

    # source에는 있지만 target에 없는 id → 끝에 추가
    new_in_source = [bid for bid in src_blocks if bid not in tgt_blocks]
    if new_in_source:
        added_blocks = "\n\n".join(src_blocks[bid] for bid in new_in_source)
        new_text = new_text.rstrip() + "\n\n" + added_blocks + "\n"

    return new_text, {
        "replaced": replaced,
        "untouched": untouched,
        "deprecated": deprecated,
        "added": new_in_source,
    }


# ─── 버전 파일 ──────────────────────────────────────────────────────────────


def load_version_file(target: Path) -> dict:
    p = target / VERSION_FILE_NAME
    if not p.exists():
        return {}
    return json.loads(read_text(p))


def write_version_file(target: Path, label: str | None) -> None:
    payload = {
        "methodology_version": METHODOLOGY_VERSION,
        "applied_at": str(date.today()),
        "applied_from": "ai-pipeline-methodology",
        "upstream_commit": upstream_commit(),
        "project_label": label,
    }
    write_text(target / VERSION_FILE_NAME, json.dumps(payload, indent=2, ensure_ascii=False) + "\n")


# ─── 마이그레이션 ───────────────────────────────────────────────────────────


def list_migrations() -> list[tuple[str, str, Path]]:
    """(from_version, to_version, path) 리스트, 버전 순서로 정렬."""
    mig_dir = METHODOLOGY_ROOT / "migrations"
    if not mig_dir.exists():
        return []
    out = []
    for p in mig_dir.glob("v*_to_v*.py"):
        m = re.match(r"^(v[\d.]+)_to_(v[\d.]+)\.py$", p.name)
        if m:
            out.append((m.group(1), m.group(2), p))
    out.sort(key=lambda x: _ver_key(x[0]))
    return out


def _ver_key(v: str) -> tuple[int, ...]:
    return tuple(int(x) for x in v.lstrip("v").split("."))


def find_migration_chain(from_v: str, to_v: str) -> list[tuple[str, str, Path]]:
    """from_v → to_v로 가는 마이그레이션 체인."""
    all_mig = list_migrations()
    chain = []
    cur = from_v
    while cur != to_v:
        nxt = next(((f, t, p) for f, t, p in all_mig if f == cur), None)
        if not nxt:
            break
        chain.append(nxt)
        cur = nxt[1]
        if _ver_key(cur) >= _ver_key(to_v):
            break
    return chain


def run_migration(target: Path, mig_path: Path, dry_run: bool) -> None:
    spec = importlib.util.spec_from_file_location(mig_path.stem, mig_path)
    if not spec or not spec.loader:
        err(f"failed to load migration {mig_path}")
        return
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    if not hasattr(mod, "migrate"):
        err(f"migration {mig_path.name} has no migrate(target, dry_run) function")
        return
    mod.migrate(target, dry_run=dry_run)


# ─── 동작: copy_path / merge_path ───────────────────────────────────────────


def copy_path(src: Path, dst: Path, dry_run: bool, *, prune: bool = False) -> int:
    """src → dst 재귀 복사. prune=True면 src에 없는 파일을 dst에서 제거.

    반환: 변경된 파일 수 (생성/덮어쓰기/삭제 모두 포함)
    """
    changes = 0
    if src.is_file():
        if not dst.exists() or read_text(src) != read_text(dst) if src.suffix in {".md", ".json", ".py", ".yaml", ".yml", ".sh"} else (not dst.exists() or src.read_bytes() != dst.read_bytes()):
            changes = 1
            if not dry_run:
                dst.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(src, dst)
        return changes

    if not src.is_dir():
        return 0

    for sp in src.rglob("*"):
        if sp.is_dir():
            continue
        rel = sp.relative_to(src)
        dp = dst / rel
        same = dp.exists() and dp.is_file() and sp.read_bytes() == dp.read_bytes()
        if not same:
            changes += 1
            if not dry_run:
                dp.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(sp, dp)

    if prune and dst.is_dir():
        src_files = {sp.relative_to(src) for sp in src.rglob("*") if sp.is_file()}
        for dp in dst.rglob("*"):
            if not dp.is_file():
                continue
            rel = dp.relative_to(dst)
            if rel not in src_files:
                changes += 1
                if not dry_run:
                    dp.unlink()
    return changes


def merge_managed_file(src: Path, dst: Path, dry_run: bool) -> dict:
    if not dst.exists():
        # 프로젝트에 아예 없으면 통째로 복사
        if not dry_run:
            shutil.copy2(src, dst)
        return {"copied_new": True, "replaced": 0, "untouched": 0, "deprecated": [], "added": []}
    src_text = read_text(src)
    dst_text = read_text(dst)
    new_text, stats = merge_managed(src_text, dst_text)
    if new_text != dst_text and not dry_run:
        write_text(dst, new_text)
    stats["changed"] = new_text != dst_text
    return stats


# ─── 명령: init ─────────────────────────────────────────────────────────────


def cmd_init(args: argparse.Namespace) -> int:
    target = Path(args.path).resolve()
    label = args.label or target.name
    mode = args.type
    today = str(date.today())

    if target.exists() and any(target.iterdir()):
        err(f"target {target} is not empty — use sync instead")
        return 1

    target.mkdir(parents=True, exist_ok=True)
    info(f"init: {target}  label={label}  type={mode}")

    # 1) shared_paths 복사
    for rel in MANIFEST["shared_paths"]:
        src = METHODOLOGY_ROOT / rel
        dst = target / rel
        if src.exists():
            n = copy_path(src, dst, dry_run=False)
            ok(f"shared    {rel}  ({n} files)")

    # 2) init_paths 복사 (v0 스켈레톤)
    for rel in MANIFEST["init_paths"]:
        src = METHODOLOGY_ROOT / rel
        dst = target / rel
        if src.exists():
            n = copy_path(src, dst, dry_run=False)
            ok(f"scaffold  {rel}  ({n} files)")

    # 3) init_files (치환 적용)
    for src_rel, dst_rel, sub in MANIFEST["init_files"]:
        src = METHODOLOGY_ROOT / src_rel
        dst = target / dst_rel
        if not src.exists():
            warn(f"init_file missing in source: {src_rel}")
            continue
        content = read_text(src)
        if sub:
            content = substitute(content, label, mode, today)
        write_text(dst, content)
        ok(f"file      {dst_rel}")

    # 4) .github/PULL_REQUEST_TEMPLATE.md (있으면)
    pr_src = METHODOLOGY_ROOT / ".github" / "PULL_REQUEST_TEMPLATE.md"
    if pr_src.exists():
        write_text(target / ".github" / "PULL_REQUEST_TEMPLATE.md", read_text(pr_src))
        ok("file      .github/PULL_REQUEST_TEMPLATE.md")

    # 5) fullstack 시 src/, tests/
    if mode == "fullstack":
        (target / "src").mkdir(exist_ok=True)
        (target / "tests" / "unit").mkdir(parents=True, exist_ok=True)
        (target / "tests" / "integration").mkdir(parents=True, exist_ok=True)
        ok("dir       src/, tests/")

    # 6) .methodology-version
    write_version_file(target, label)
    ok(f"version   {VERSION_FILE_NAME} → {METHODOLOGY_VERSION}")

    info("done. 다음:")
    print("  cd", target)
    print("  python3 50_tools/generate-dashboard.py --serve   # 대시보드 확인")
    print(f"  방법론 갱신 시: python3 {METHODOLOGY_ROOT}/50_tools/methodology.py sync --apply")
    return 0


# ─── 명령: sync ─────────────────────────────────────────────────────────────


def cmd_sync(args: argparse.Namespace) -> int:
    target = Path(args.path or ".").resolve()
    apply = args.apply
    dry = not apply

    vinfo = load_version_file(target)
    if not vinfo:
        err(f"{VERSION_FILE_NAME} 없음 — 이 폴더는 methodology init으로 만든 프로젝트가 아닙니다.")
        err("처음 적용한다면: 50_tools/methodology.py init <path> 또는 빈 .methodology-version 파일 만들고 재시도")
        return 2

    cur_v = vinfo.get("methodology_version", "v0.0")
    target_v = args.target or METHODOLOGY_VERSION
    info(f"sync: {target}  ({cur_v} → {target_v})  {'DRY-RUN' if dry else 'APPLY'}")

    # 1) 마이그레이션 실행
    chain = find_migration_chain(cur_v, target_v)
    if cur_v != target_v and not chain:
        warn(f"마이그레이션 경로 없음: {cur_v} → {target_v}. 직접 적용으로 진행.")
    for f, t, p in chain:
        info(f"migrate   {f} → {t}  ({p.name})")
        run_migration(target, p, dry_run=dry)

    # 2) shared_paths: 항상 덮어쓰기
    total_changes = 0
    for rel in MANIFEST["shared_paths"]:
        src = METHODOLOGY_ROOT / rel
        dst = target / rel
        if not src.exists():
            continue
        n = copy_path(src, dst, dry_run=dry, prune=src.is_dir())
        if n:
            total_changes += n
            tag = "would update" if dry else "updated"
            ok(f"shared    {tag:13s} {rel}  ({n} files)")

    # 3) managed_files: 마커 머지
    for rel in MANIFEST["managed_files"]:
        src = METHODOLOGY_ROOT / rel
        dst = target / rel
        if not src.exists():
            continue
        stats = merge_managed_file(src, dst, dry_run=dry)
        if stats.get("copied_new"):
            ok(f"managed   created {rel}")
            total_changes += 1
        elif stats.get("changed"):
            tag = "would merge" if dry else "merged"
            msg = f"managed   {tag:13s} {rel}  (replaced={stats['replaced']}, added={len(stats['added'])}, deprecated={len(stats['deprecated'])})"
            ok(msg)
            if stats["deprecated"]:
                warn(f"          deprecated 블록 (확인 필요): {', '.join(stats['deprecated'])}")
            total_changes += 1
        else:
            info(f"managed   unchanged   {rel}")

    # 4) 버전 파일 갱신
    if not dry:
        write_version_file(target, vinfo.get("project_label"))
        ok(f"version   {VERSION_FILE_NAME} → {target_v}")
    else:
        info(f"version   would set {VERSION_FILE_NAME} → {target_v}")

    if dry:
        info(f"총 {total_changes}개 변경 예정. 적용하려면 --apply")
    else:
        ok(f"sync 완료. 총 {total_changes}개 파일 변경.")
    return 0


# ─── 명령: status ───────────────────────────────────────────────────────────


def cmd_status(args: argparse.Namespace) -> int:
    target = Path(args.path or ".").resolve()
    vinfo = load_version_file(target)
    if not vinfo:
        err(f"{VERSION_FILE_NAME} 없음 — methodology 적용 안 된 폴더")
        return 2
    cur_v = vinfo.get("methodology_version", "?")
    print(f"project          {target}")
    print(f"applied version  {cur_v}")
    print(f"upstream version {METHODOLOGY_VERSION}")
    print(f"upstream commit  {upstream_commit()}")
    if cur_v != METHODOLOGY_VERSION:
        chain = find_migration_chain(cur_v, METHODOLOGY_VERSION)
        if chain:
            print(f"migrations needed: {len(chain)}")
            for f, t, p in chain:
                print(f"  {f} → {t}  ({p.name})")
        else:
            print("migrations:      (직접 동기화)")
    else:
        print("status:          최신 ✓")
    return 0


# ─── 명령: diff ─────────────────────────────────────────────────────────────


def cmd_diff(args: argparse.Namespace) -> int:
    target = Path(args.path or ".").resolve()
    rel = args.file
    src = METHODOLOGY_ROOT / rel
    dst = target / rel
    if not src.exists():
        err(f"upstream에 없음: {rel}")
        return 1
    if not dst.exists():
        info(f"{rel} 은 새 파일 — 전체가 추가될 예정")
        print(read_text(src))
        return 0

    if rel in MANIFEST["managed_files"]:
        new_text, stats = merge_managed(read_text(src), read_text(dst))
        old_text = read_text(dst)
        info(f"managed merge: replaced={stats['replaced']}, added={len(stats['added'])}, deprecated={len(stats['deprecated'])}")
    else:
        old_text = read_text(dst)
        new_text = read_text(src)
        info("shared overwrite (전체 교체)")

    if old_text == new_text:
        ok("동일 — 변경 없음")
        return 0

    diff = unified_diff(old_text.splitlines(keepends=True), new_text.splitlines(keepends=True),
                        fromfile=f"a/{rel}", tofile=f"b/{rel}")
    sys.stdout.writelines(diff)
    return 0


# ─── 명령: version ──────────────────────────────────────────────────────────


def cmd_version(args: argparse.Namespace) -> int:
    print(f"methodology {METHODOLOGY_VERSION}  ({upstream_commit()})  @ {METHODOLOGY_ROOT}")
    return 0


# ─── main ──────────────────────────────────────────────────────────────────


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(prog="methodology", description="방법론 배포·갱신 CLI")
    sub = p.add_subparsers(dest="cmd", required=True)

    pi = sub.add_parser("init", help="새 프로젝트에 방법론 주입")
    pi.add_argument("path", help="대상 디렉터리 (없으면 생성)")
    pi.add_argument("--type", choices=["fullstack", "planning-only"], default="fullstack")
    pi.add_argument("--label", help="프로젝트 라벨 (기본: 디렉터리명)")
    pi.set_defaults(func=cmd_init)

    ps = sub.add_parser("sync", help="현재 폴더를 업스트림과 동기화")
    ps.add_argument("--apply", action="store_true", help="실제 적용 (없으면 dry-run)")
    ps.add_argument("--target", help="목표 버전 (기본: 최신)")
    ps.add_argument("--path", help="대상 폴더 (기본: 현재 디렉터리)")
    ps.set_defaults(func=cmd_sync)

    pst = sub.add_parser("status", help="버전 비교")
    pst.add_argument("--path", help="대상 폴더 (기본: 현재)")
    pst.set_defaults(func=cmd_status)

    pd = sub.add_parser("diff", help="단일 파일이 어떻게 갱신되는지 표시")
    pd.add_argument("file", help="대상 폴더 기준 상대 경로")
    pd.add_argument("--path", help="대상 폴더 (기본: 현재)")
    pd.set_defaults(func=cmd_diff)

    pv = sub.add_parser("version", help="메소돌로지 버전 출력")
    pv.set_defaults(func=cmd_version)

    args = p.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())

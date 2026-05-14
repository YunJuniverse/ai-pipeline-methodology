#!/usr/bin/env python3
"""swap-icon-color.py — in-spire 아이콘의 그라데이션 색상만 OS별로 swap.

원본(macOS teal/navy)의 흰색 stroke 와 squircle 바깥 흰색 배경은 보호하고,
그라데이션 영역만 새 색상으로 대체. 그라데이션 방향(top-left → bottom-right)
은 원본 위치 좌표 기반으로 재계산되어 자연스럽게 유지된다.

사용:
  python3 60_tools/swap-icon-color.py <source.png>

출력:
  <source>-mac.png        (원본 그대로 복사, 검증용)
  <source>-win.png        (royal blue → midnight blue)
  <source>-linux.png      (amber → burnt sienna)
"""
from __future__ import annotations

import sys
from pathlib import Path

from PIL import Image


# OS 별 (start, end) RGB — top-left → bottom-right
PALETTES: dict[str, tuple[tuple[int, int, int], tuple[int, int, int]]] = {
    "mac":   ((0x0f, 0x76, 0x6e), (0x0c, 0x4a, 0x6e)),   # teal → navy (원본)
    "win":   ((0x25, 0x63, 0xeb), (0x1e, 0x3a, 0x8a)),   # royal blue → midnight blue
    "linux": ((0xea, 0x58, 0x0c), (0x7c, 0x2d, 0x12)),   # amber → burnt sienna
}

# 흰색 보호 임계값 — 모든 채널이 이 값 이상이면 stroke 또는 외부 배경으로 간주
WHITE_THRESHOLD = 220


def swap_gradient(
    src_path: Path,
    dst_path: Path,
    color_start: tuple[int, int, int],
    color_end: tuple[int, int, int],
) -> None:
    img = Image.open(src_path).convert("RGBA")
    w, h = img.size
    px = img.load()
    diag = max(w + h, 1)

    swapped = 0
    preserved = 0

    for y in range(h):
        for x in range(w):
            r, g, b, a = px[x, y]

            # 흰색(stroke 또는 외부 배경) 보호
            if r >= WHITE_THRESHOLD and g >= WHITE_THRESHOLD and b >= WHITE_THRESHOLD:
                preserved += 1
                continue

            # 그라데이션 위치 t (top-left=0, bottom-right=1)
            t = (x + y) / diag

            new_r = int(round(color_start[0] * (1 - t) + color_end[0] * t))
            new_g = int(round(color_start[1] * (1 - t) + color_end[1] * t))
            new_b = int(round(color_start[2] * (1 - t) + color_end[2] * t))

            px[x, y] = (new_r, new_g, new_b, a)
            swapped += 1

    img.save(dst_path, "PNG", optimize=True)
    total = w * h
    print(f"  [ok] {dst_path.name}  ({swapped:,} pixels swapped, {preserved:,} preserved, total {total:,})")


def main(argv: list[str]) -> int:
    if len(argv) < 2:
        print("usage: swap-icon-color.py <source.png>", file=sys.stderr)
        return 2

    src = Path(argv[1]).resolve()
    if not src.exists():
        print(f"[err] 원본 미발견: {src}", file=sys.stderr)
        return 1

    # 출력은 원본 디렉터리에 in-spire-{mac,win,linux}.png
    out_dir = src.parent
    base = "in-spire"
    print(f"source: {src}")
    print(f"output dir: {out_dir}")
    print()

    for variant, (c_start, c_end) in PALETTES.items():
        out = out_dir / f"{base}-{variant}.png"
        print(f"swap → {variant}  ({'#%02x%02x%02x' % c_start} → {'#%02x%02x%02x' % c_end})")
        swap_gradient(src, out, c_start, c_end)

    print()
    print(f"완료. {len(PALETTES)}장 생성:")
    for variant in PALETTES:
        print(f"  {out_dir / f'{base}-{variant}.png'}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))

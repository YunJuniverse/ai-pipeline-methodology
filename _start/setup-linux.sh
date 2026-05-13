#!/bin/bash
# setup-linux.sh — in-spire.desktop 의 Exec/Icon 을 현재 절대경로로 갱신.
# 사용자 1회 실행:
#   bash setup-linux.sh
# 그 후 in-spire.desktop 을 ~/.local/share/applications/ 에 복사하면 메뉴 등록.

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
EXEC_PATH="$HERE/in-spire.sh"
ICON_PATH="$HERE/icons/in-spire-256-linux.png"

sed -e "s|__EXEC__|$EXEC_PATH|" -e "s|__ICON__|$ICON_PATH|" \
  "$HERE/in-spire.desktop" > "$HERE/in-spire.desktop.tmp"
mv "$HERE/in-spire.desktop.tmp" "$HERE/in-spire.desktop"

echo "[ok] in-spire.desktop updated:"
echo "  Exec=$EXEC_PATH"
echo "  Icon=$ICON_PATH"
echo ""
echo "To register in app menu:"
echo "  cp $HERE/in-spire.desktop ~/.local/share/applications/"
echo "  chmod +x $HERE/in-spire.sh"

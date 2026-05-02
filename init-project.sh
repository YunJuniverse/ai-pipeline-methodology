#!/bin/bash
# init-project.sh — evidence-driven AI development project scaffold
#
# Usage:
#   bash init-project.sh <project-name> --type <fullstack|planning-only>

set -euo pipefail

PROJECT_NAME=""
PROJECT_TYPE="fullstack"

while [[ $# -gt 0 ]]; do
    case "$1" in
        --type)
            PROJECT_TYPE="${2:-}"
            shift 2
            ;;
        *)
            PROJECT_NAME="$1"
            shift
            ;;
    esac
done

if [ -z "$PROJECT_NAME" ]; then
    echo "Usage: bash init-project.sh <project-name> --type <fullstack|planning-only>"
    echo ""
    echo "Types:"
    echo "  fullstack      code + tests + PR workflow"
    echo "  planning-only  research + snapshot + approval workflow"
    exit 1
fi

case "$PROJECT_TYPE" in
    fullstack|planning-only) ;;
    *)
        echo "Error: Invalid type '$PROJECT_TYPE'"
        echo "Use: fullstack or planning-only"
        exit 1
        ;;
esac

METHODOLOGY_DIR="$(cd "$(dirname "$0")" && pwd)"
TARGET_DIR="$PROJECT_NAME"
PROJECT_LABEL="$(basename "$PROJECT_NAME")"
TODAY="$(date +%F)"

if [ -d "$TARGET_DIR" ]; then
    echo "Error: Directory '$TARGET_DIR' already exists."
    exit 1
fi

echo "Creating project: $PROJECT_NAME (type: $PROJECT_TYPE)"
echo ""

mkdir -p "$TARGET_DIR"
mkdir -p "$TARGET_DIR/.github"
mkdir -p "$TARGET_DIR/briefs"
mkdir -p "$TARGET_DIR/briefs/updates"
mkdir -p "$TARGET_DIR/docs/adr"
mkdir -p "$TARGET_DIR/docs/snapshots/plans/business"
mkdir -p "$TARGET_DIR/docs/snapshots/plans/service"
mkdir -p "$TARGET_DIR/docs/snapshots/plans/ops"
mkdir -p "$TARGET_DIR/docs/snapshots/plans/marketing"
mkdir -p "$TARGET_DIR/docs/snapshots/plans/brand"
mkdir -p "$TARGET_DIR/docs/snapshots/plans/pm"
mkdir -p "$TARGET_DIR/docs/snapshots/dev-specs"
mkdir -p "$TARGET_DIR/docs/guides/planning"

cp "$METHODOLOGY_DIR/CLAUDE.md" "$TARGET_DIR/CLAUDE.md"
cp "$METHODOLOGY_DIR/AGENTS.md" "$TARGET_DIR/AGENTS.md"
cp "$METHODOLOGY_DIR/generate-dashboard.py" "$TARGET_DIR/generate-dashboard.py"
cp "$METHODOLOGY_DIR/.github/PULL_REQUEST_TEMPLATE.md" "$TARGET_DIR/.github/PULL_REQUEST_TEMPLATE.md"
cp "$METHODOLOGY_DIR/docs/guides/planning/"* "$TARGET_DIR/docs/guides/planning/"

sed -i '' "s|\\[PROJECT_NAME\\]|$PROJECT_LABEL|g" "$TARGET_DIR/CLAUDE.md"
sed -i '' "s|\\[PROJECT_NAME\\]|$PROJECT_LABEL|g" "$TARGET_DIR/AGENTS.md"
sed -i '' "s|\\[fullstack / planning-only\\]|$PROJECT_TYPE|g" "$TARGET_DIR/CLAUDE.md"
sed -i '' "s|\\[fullstack / planning-only\\]|$PROJECT_TYPE|g" "$TARGET_DIR/AGENTS.md"
sed -i '' "s|\\[YYYY-MM-DD\\]|$TODAY|g" "$TARGET_DIR/CLAUDE.md"
sed -i '' "s|\\[YYYY-MM-DD\\]|$TODAY|g" "$TARGET_DIR/AGENTS.md"

cp "$METHODOLOGY_DIR/docs/templates/HANDOFF.md" "$TARGET_DIR/HANDOFF.md"
sed -i '' "s|\\[PROJECT_NAME\\]|$PROJECT_LABEL|g" "$TARGET_DIR/HANDOFF.md"
sed -i '' "s|\\[PROJECT_MODE\\]|$PROJECT_TYPE|g" "$TARGET_DIR/HANDOFF.md"
sed -i '' "s|\\[YYYY-MM-DD\\]|$TODAY|g" "$TARGET_DIR/HANDOFF.md"

cat > "$TARGET_DIR/TODO.md" << TODO_EOF
# TODO.md

> Ordered backlog. Each item needs acceptance criteria.

## Ready

### TODO-001
- title:
- mode: ${PROJECT_TYPE}
- change-class: A
- owner: human
- acceptance criteria:
  - [ ]
  - [ ]
- notes:

## In Progress

- none

## Blocked

- none

## Done

- none
TODO_EOF

if [ "$PROJECT_TYPE" = "fullstack" ]; then
    mkdir -p "$TARGET_DIR/src"
    mkdir -p "$TARGET_DIR/tests/unit"
    mkdir -p "$TARGET_DIR/tests/integration"
    echo "  + src/"
    echo "  + tests/"
fi

touch "$TARGET_DIR/briefs/.gitkeep"
touch "$TARGET_DIR/briefs/updates/.gitkeep"
touch "$TARGET_DIR/docs/adr/.gitkeep"
touch "$TARGET_DIR/docs/snapshots/plans/business/.gitkeep"
touch "$TARGET_DIR/docs/snapshots/plans/service/.gitkeep"
touch "$TARGET_DIR/docs/snapshots/plans/ops/.gitkeep"
touch "$TARGET_DIR/docs/snapshots/plans/marketing/.gitkeep"
touch "$TARGET_DIR/docs/snapshots/plans/brand/.gitkeep"
touch "$TARGET_DIR/docs/snapshots/plans/pm/.gitkeep"
touch "$TARGET_DIR/docs/snapshots/dev-specs/.gitkeep"

echo "  + CLAUDE.md"
echo "  + AGENTS.md"
echo "  + HANDOFF.md"
echo "  + TODO.md"
echo "  + generate-dashboard.py"
echo "  + .github/PULL_REQUEST_TEMPLATE.md"
echo "  + briefs/"
echo "  + briefs/updates/"
echo "  + docs/adr/"
echo "  + docs/snapshots/plans/{business,service,ops,marketing,brand,pm}/"
echo "  + docs/snapshots/dev-specs/"
echo "  + docs/guides/planning/"

echo ""
echo "Done: $TARGET_DIR"
echo ""
echo "Next steps:"
echo "  1. cd $TARGET_DIR"
echo "  2. Put brief files (idea notes, PDFs, docs) in briefs/"
echo "  3. Fill Project Settings in CLAUDE.md and AGENTS.md"
echo "  4. Start a session with the Kickoff Prompt (Brief-Based template)"
echo ""
echo "Dashboard:"
echo "  python3 generate-dashboard.py --serve   # 실시간 (권장)"
echo "  python3 generate-dashboard.py           # 정적 파일"

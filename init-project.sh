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
mkdir -p "$TARGET_DIR/10_guides"
mkdir -p "$TARGET_DIR/20_planning/16_AI_기능"
mkdir -p "$TARGET_DIR/30_dev/adr"
mkdir -p "$TARGET_DIR/30_dev/snapshots"
mkdir -p "$TARGET_DIR/40_resources/templates"
mkdir -p "$TARGET_DIR/40_resources/prompts"

cp "$METHODOLOGY_DIR/CLAUDE.md" "$TARGET_DIR/CLAUDE.md"
cp "$METHODOLOGY_DIR/AGENTS.md" "$TARGET_DIR/AGENTS.md"
cp "$METHODOLOGY_DIR/.github/PULL_REQUEST_TEMPLATE.md" "$TARGET_DIR/.github/PULL_REQUEST_TEMPLATE.md"

sed -i '' "s|\\[PROJECT_NAME\\]|$PROJECT_LABEL|g" "$TARGET_DIR/CLAUDE.md"
sed -i '' "s|\\[PROJECT_NAME\\]|$PROJECT_LABEL|g" "$TARGET_DIR/AGENTS.md"
sed -i '' "s|\\[fullstack / planning-only\\]|$PROJECT_TYPE|g" "$TARGET_DIR/CLAUDE.md"
sed -i '' "s|\\[fullstack / planning-only\\]|$PROJECT_TYPE|g" "$TARGET_DIR/AGENTS.md"
sed -i '' "s|\\[YYYY-MM-DD\\]|$TODAY|g" "$TARGET_DIR/CLAUDE.md"
sed -i '' "s|\\[YYYY-MM-DD\\]|$TODAY|g" "$TARGET_DIR/AGENTS.md"

cp -R "$METHODOLOGY_DIR/10_guides/." "$TARGET_DIR/10_guides/"
cp -R "$METHODOLOGY_DIR/20_planning/." "$TARGET_DIR/20_planning/"
cp -R "$METHODOLOGY_DIR/30_dev/." "$TARGET_DIR/30_dev/"
cp -R "$METHODOLOGY_DIR/40_resources/." "$TARGET_DIR/40_resources/"
cp "$METHODOLOGY_DIR/methodology-graph.json" "$TARGET_DIR/methodology-graph.json"
cp "$METHODOLOGY_DIR/generate-dashboard.py" "$TARGET_DIR/generate-dashboard.py"
cp "$METHODOLOGY_DIR/40_resources/templates/HANDOFF.md" "$TARGET_DIR/HANDOFF.md"
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

echo "  + CLAUDE.md / AGENTS.md / HANDOFF.md / TODO.md"
echo "  + .github/PULL_REQUEST_TEMPLATE.md"
echo "  + 10_guides/         (작성 지침서 11종)"
echo "  + 20_planning/       (기획 산출물 v0)"
echo "  + 30_dev/            (MASTER_PLAN.md, SPRINTS.md, adr/, snapshots/)"
echo "  + 40_resources/      (templates/, prompts/)"
echo "  + methodology-graph.json + generate-dashboard.py"

echo ""
echo "Done: $TARGET_DIR"
echo ""
echo "Next steps:"
echo "  1. cd $TARGET_DIR"
echo "  2. Fill Project Settings in CLAUDE.md and AGENTS.md"
echo "  3. Update TODO.md with the first real task"
echo "  4. Start a session with the Kickoff Prompt"

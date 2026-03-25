#!/bin/bash
# init-project.sh — 하네스 기반 애자일 프로젝트 초기화
#
# Usage:
#   ./init-project.sh <project-name> --type <fullstack|planning-only|research|coding-only>

set -e

PROJECT_NAME=""
PROJECT_TYPE="fullstack"

while [[ $# -gt 0 ]]; do
    case $1 in
        --type)
            PROJECT_TYPE="$2"
            shift 2
            ;;
        *)
            PROJECT_NAME="$1"
            shift
            ;;
    esac
done

if [ -z "$PROJECT_NAME" ]; then
    echo "Usage: ./init-project.sh <project-name> --type <fullstack|planning-only|research|coding-only>"
    echo ""
    echo "Types:"
    echo "  fullstack      리서치 → 기획 → 개발명세 → 구현 → 리뷰 → 환류"
    echo "  planning-only  리서치 → 기획 → 보고/환류"
    echo "  research       리서치 중심"
    echo "  coding-only    기존 기획 기반 구현/리뷰/환류"
    exit 1
fi

case "$PROJECT_TYPE" in
    fullstack|planning-only|research|coding-only) ;;
    *)
        echo "Error: Invalid type '$PROJECT_TYPE'"
        echo "Use: fullstack, planning-only, research, coding-only"
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

mkdir -p "$TARGET_DIR/.claude/skills"
mkdir -p "$TARGET_DIR/docs"

cp "$METHODOLOGY_DIR/CLAUDE.md" "$TARGET_DIR/CLAUDE.md"
cp "$METHODOLOGY_DIR/AGENTS.md" "$TARGET_DIR/AGENTS.md"
cp "$METHODOLOGY_DIR/KICKOFF_PROMPT.md" "$TARGET_DIR/KICKOFF_PROMPT.md"

sed -i '' "s|\[PROJECT_NAME\]|$PROJECT_LABEL|g" "$TARGET_DIR/CLAUDE.md"
sed -i '' "s|\[PROJECT_NAME\]|$PROJECT_LABEL|g" "$TARGET_DIR/AGENTS.md"
sed -i '' "s|\[fullstack\]|$PROJECT_TYPE|g" "$TARGET_DIR/CLAUDE.md"
sed -i '' "s|\[fullstack\]|$PROJECT_TYPE|g" "$TARGET_DIR/AGENTS.md"
sed -i '' "s|\[YYYY-MM-DD\]|$TODAY|g" "$TARGET_DIR/CLAUDE.md"
sed -i '' "0,/\\[YYYY-MM-DD\\]/s//${TODAY}/" "$TARGET_DIR/AGENTS.md"

cp "$METHODOLOGY_DIR/.claude/skills/ai-planning.md" "$TARGET_DIR/.claude/skills/"
cp "$METHODOLOGY_DIR/.claude/skills/ai-relay.md" "$TARGET_DIR/.claude/skills/"

if [ "$PROJECT_TYPE" = "fullstack" ] || [ "$PROJECT_TYPE" = "coding-only" ]; then
    cp "$METHODOLOGY_DIR/.claude/skills/vibe-coding.md" "$TARGET_DIR/.claude/skills/"
    echo "  + vibe-coding skill"
fi

if [ -d "$METHODOLOGY_DIR/docs/planning-guides" ]; then
    cp -r "$METHODOLOGY_DIR/docs/planning-guides" "$TARGET_DIR/docs/"
    echo "  + planning-guides"
fi

if [ -d "$METHODOLOGY_DIR/docs/relay-templates" ]; then
    cp -r "$METHODOLOGY_DIR/docs/relay-templates" "$TARGET_DIR/docs/"
    echo "  + relay-templates"
fi

if [ -d "$METHODOLOGY_DIR/docs/vibe-templates" ]; then
    cp -r "$METHODOLOGY_DIR/docs/vibe-templates" "$TARGET_DIR/docs/"
    echo "  + vibe-templates"
fi

if [ -d "$METHODOLOGY_DIR/docs/agile-templates" ]; then
    cp -r "$METHODOLOGY_DIR/docs/agile-templates" "$TARGET_DIR/docs/"
    echo "  + agile-templates"
fi

cp "$METHODOLOGY_DIR/docs/agile-deliverables-map.md" "$TARGET_DIR/docs/agile-deliverables-map.md"

mkdir -p "$TARGET_DIR/docs/research"
mkdir -p "$TARGET_DIR/docs/planning"
mkdir -p "$TARGET_DIR/docs/development"
mkdir -p "$TARGET_DIR/docs/sprints"
mkdir -p "$TARGET_DIR/docs/governance"
mkdir -p "$TARGET_DIR/docs/adr"

if [ "$PROJECT_TYPE" = "fullstack" ] || [ "$PROJECT_TYPE" = "coding-only" ]; then
    mkdir -p "$TARGET_DIR/src/domain"
    mkdir -p "$TARGET_DIR/src/application/ports"
    mkdir -p "$TARGET_DIR/src/infrastructure"
    mkdir -p "$TARGET_DIR/src/interface"
    mkdir -p "$TARGET_DIR/src/shared/types"
    mkdir -p "$TARGET_DIR/src/shared/utils"
    mkdir -p "$TARGET_DIR/src/shared/constants"
    mkdir -p "$TARGET_DIR/tests/unit"
    mkdir -p "$TARGET_DIR/tests/integration"
    mkdir -p "$TARGET_DIR/tests/e2e"
    echo "  + src/ 4-layer structure"
    echo "  + tests/ structure"
fi

echo "" > "$TARGET_DIR/docs/research/.gitkeep"
echo "" > "$TARGET_DIR/docs/planning/.gitkeep"
echo "" > "$TARGET_DIR/docs/development/.gitkeep"
echo "" > "$TARGET_DIR/docs/sprints/.gitkeep"
echo "" > "$TARGET_DIR/docs/governance/.gitkeep"
echo "" > "$TARGET_DIR/docs/adr/.gitkeep"

echo ""
echo "Done: $TARGET_DIR"
echo ""
echo "Next steps:"
echo "  1. cd $TARGET_DIR"
echo "  2. Edit CLAUDE.md and AGENTS.md — fill in objective, stack, sprint goal"
echo "  3. Review docs/agile-deliverables-map.md"
echo "  4. Run: claude"
echo "  5. Start with: \"CLAUDE.md를 읽고 Discovery Research와 Planning Docs v0.1부터 시작해줘.\""

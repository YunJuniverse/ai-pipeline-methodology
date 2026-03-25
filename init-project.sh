#!/bin/bash
# init-project.sh — 새 프로젝트 폴더 초기화
#
# Usage:
#   ./init-project.sh <project-name> --type <fullstack|planning-only|research|coding-only>
#
# Examples:
#   ./init-project.sh grooming-community --type fullstack
#   ./init-project.sh hair-products --type planning-only
#   ./init-project.sh market-research --type research

set -e

# Parse arguments
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
    echo "  fullstack      Stage 0→1→2→3→4  (기획부터 코딩까지)"
    echo "  planning-only  Stage 0→1→2→3    (기획 산출물만)"
    echo "  research       Stage 0→1        (리서치/사업성 검토만)"
    echo "  coding-only    Stage 0→2→4      (기존 기획 기반 바로 코딩)"
    exit 1
fi

# Validate type
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

if [ -d "$TARGET_DIR" ]; then
    echo "Error: Directory '$TARGET_DIR' already exists."
    exit 1
fi

echo "Creating project: $PROJECT_NAME (type: $PROJECT_TYPE)"
echo ""

# Create directory structure
mkdir -p "$TARGET_DIR/.claude/skills"
mkdir -p "$TARGET_DIR/docs"

# Copy CLAUDE.md
cp "$METHODOLOGY_DIR/CLAUDE.md" "$TARGET_DIR/CLAUDE.md"

# Update project type in CLAUDE.md
sed -i '' "s|\[fullstack / planning-only / research / coding-only\]|$PROJECT_TYPE|" "$TARGET_DIR/CLAUDE.md"

# Copy skills (always copy planning and relay)
cp "$METHODOLOGY_DIR/.claude/skills/ai-planning.md" "$TARGET_DIR/.claude/skills/"
cp "$METHODOLOGY_DIR/.claude/skills/ai-relay.md" "$TARGET_DIR/.claude/skills/"

# Copy vibe-coding skill only for coding projects
if [ "$PROJECT_TYPE" = "fullstack" ] || [ "$PROJECT_TYPE" = "coding-only" ]; then
    cp "$METHODOLOGY_DIR/.claude/skills/vibe-coding.md" "$TARGET_DIR/.claude/skills/"
    echo "  + vibe-coding skill"
fi

# Copy planning guides (always — used for 완성본 참조)
if [ -d "$METHODOLOGY_DIR/docs/planning-guides" ]; then
    cp -r "$METHODOLOGY_DIR/docs/planning-guides" "$TARGET_DIR/docs/"
    echo "  + planning-guides (8 files)"
fi

# Copy relay templates
if [ -d "$METHODOLOGY_DIR/docs/relay-templates" ]; then
    cp -r "$METHODOLOGY_DIR/docs/relay-templates" "$TARGET_DIR/docs/"
    echo "  + relay-templates (4 files)"
fi

# Copy vibe templates for coding projects
if [ "$PROJECT_TYPE" = "fullstack" ] || [ "$PROJECT_TYPE" = "coding-only" ]; then
    if [ -d "$METHODOLOGY_DIR/docs/vibe-templates" ]; then
        cp -r "$METHODOLOGY_DIR/docs/vibe-templates" "$TARGET_DIR/docs/"
        echo "  + vibe-templates (CPS/PRD/ADR/ARCHITECTURE)"
    fi
fi

# Create src/ 4-layer structure for coding projects
if [ "$PROJECT_TYPE" = "fullstack" ] || [ "$PROJECT_TYPE" = "coding-only" ]; then
    mkdir -p "$TARGET_DIR/src/domain"
    mkdir -p "$TARGET_DIR/src/application/ports"
    mkdir -p "$TARGET_DIR/src/infrastructure"
    mkdir -p "$TARGET_DIR/src/interface"
    mkdir -p "$TARGET_DIR/src/shared/types"
    mkdir -p "$TARGET_DIR/src/shared/utils"
    mkdir -p "$TARGET_DIR/src/shared/constants"
    echo "  + src/ 4-layer structure"
fi

# Create docs/adr/ for ADR logs
mkdir -p "$TARGET_DIR/docs/adr"

echo ""
echo "Done: $TARGET_DIR"
echo ""
echo "Next steps:"
echo "  1. cd $TARGET_DIR"
echo "  2. Edit CLAUDE.md — fill in [PROJECT_NAME], [목적], [스택]"
echo "  3. Run: claude"
echo "  4. Say: \"CLAUDE.md 읽고 프로젝트 구조 파악해줘. 오늘 작업: [YOUR TASK]\""

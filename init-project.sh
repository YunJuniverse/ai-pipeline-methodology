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
    echo "  fullstack      Phase 1~10: 리서치 → 기획서 6종 → 개발명세서 8종 → 구현 → 리뷰 → 환류"
    echo "  planning-only  Phase 1~2:  리서치 → 기획서 6종"
    echo "  research       Phase 1:    리서치 중심"
    echo "  coding-only    Phase 3~10: 기존 기획/개발명세서 기반 구현 → 리뷰 → 환류"
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

# --- Core files ---
mkdir -p "$TARGET_DIR/.claude/skills"
mkdir -p "$TARGET_DIR/docs"

cp "$METHODOLOGY_DIR/CLAUDE.md" "$TARGET_DIR/CLAUDE.md"
cp "$METHODOLOGY_DIR/AGENTS.md" "$TARGET_DIR/AGENTS.md"
cp "$METHODOLOGY_DIR/KICKOFF_PROMPT.md" "$TARGET_DIR/KICKOFF_PROMPT.md"

sed -i '' "s|\[PROJECT_NAME\]|$PROJECT_LABEL|g" "$TARGET_DIR/CLAUDE.md"
sed -i '' "s|\[PROJECT_NAME\]|$PROJECT_LABEL|g" "$TARGET_DIR/AGENTS.md"
sed -i '' "s|\[fullstack / planning-only / research / coding-only\]|$PROJECT_TYPE|g" "$TARGET_DIR/CLAUDE.md"
sed -i '' "s|\[fullstack / planning-only / research / coding-only\]|$PROJECT_TYPE|g" "$TARGET_DIR/AGENTS.md"
sed -i '' "s|\[YYYY-MM-DD\]|$TODAY|g" "$TARGET_DIR/CLAUDE.md"
sed -i '' "0,/\\[YYYY-MM-DD\\]/s//${TODAY}/" "$TARGET_DIR/AGENTS.md"
echo "  + CLAUDE.md, AGENTS.md, KICKOFF_PROMPT.md"

# --- Skills ---
cp "$METHODOLOGY_DIR/.claude/skills/ai-planning.md" "$TARGET_DIR/.claude/skills/"
cp "$METHODOLOGY_DIR/.claude/skills/ai-relay.md" "$TARGET_DIR/.claude/skills/"
echo "  + ai-planning, ai-relay skills"

if [ "$PROJECT_TYPE" = "fullstack" ] || [ "$PROJECT_TYPE" = "coding-only" ]; then
    cp "$METHODOLOGY_DIR/.claude/skills/vibe-coding.md" "$TARGET_DIR/.claude/skills/"
    echo "  + vibe-coding skill"
fi

# --- Reference docs ---
if [ -d "$METHODOLOGY_DIR/docs/planning-guides" ]; then
    cp -r "$METHODOLOGY_DIR/docs/planning-guides" "$TARGET_DIR/docs/"
    echo "  + planning-guides (기획서 작성 지침)"
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
echo "  + agile-deliverables-map.md"

# --- Cleanup copied finder metadata ---
find "$TARGET_DIR" -name .DS_Store -delete

# --- Folder structure ---
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

# --- Starter artifacts: research ---
cat > "$TARGET_DIR/docs/research/research.md" << 'RESEARCH_EOF'
# Research

> Version: v0.1 | Date: YYYY-MM-DD | Status: Draft

## 1. Research Objective
- Question:
- Why this matters:

## 2. Scope
- Included:
- Excluded:

## 3. Sources
| Type | Source | Reliability | Notes |
|------|--------|-------------|-------|
| | | | |

## 4. Key Findings
1.

## 5. Implications For Product
- Planning impact:
- Development impact:
- Risk impact:

## 6. Open Questions
1.

## 7. Recommendation
- Action:
- Confidence:
- Human decision needed:

## Change Log
| Version | Date | Summary |
|---------|------|---------|
| v0.1 | YYYY-MM-DD | Initial research |
RESEARCH_EOF
sed -i '' "s|YYYY-MM-DD|$TODAY|g" "$TARGET_DIR/docs/research/research.md"
echo "  + docs/research/research.md (starter)"

# --- Starter artifacts: 기획서 6종 ---
if [ "$PROJECT_TYPE" = "fullstack" ] || [ "$PROJECT_TYPE" = "planning-only" ]; then
    PLANNING_DOCS=("business-plan" "service-plan" "operations-plan" "marketing-plan" "brand-plan" "project-management")
    PLANNING_LABELS=("사업기획서" "서비스기획서" "운영기획서" "마케팅기획서" "브랜드기획서" "프로젝트관리기획서")

    for i in "${!PLANNING_DOCS[@]}"; do
        DOC="${PLANNING_DOCS[$i]}"
        LABEL="${PLANNING_LABELS[$i]}"
        TEMPLATE="$METHODOLOGY_DIR/docs/agile-templates/planning/${DOC}-template.md"
        TARGET="$TARGET_DIR/docs/planning/${DOC}.md"

        if [ -f "$TEMPLATE" ]; then
            cp "$TEMPLATE" "$TARGET"
            sed -i '' "s|YYYY-MM-DD|$TODAY|g" "$TARGET"
        else
            cat > "$TARGET" << PLAN_EOF
# ${LABEL}

> Version: v0.1 | Date: ${TODAY} | Status: Draft

<!-- 내용을 채워주세요 -->

## Change Log
| Version | Date | Summary |
|---------|------|---------|
| v0.1 | ${TODAY} | Initial draft |
PLAN_EOF
        fi
    done
    echo "  + docs/planning/ (기획서 6종 starter)"
fi

# --- Starter artifacts: 개발명세서 8종 ---
if [ "$PROJECT_TYPE" = "fullstack" ] || [ "$PROJECT_TYPE" = "coding-only" ]; then
    DEV_DOCS=("service-overview" "requirements" "user-stories" "information-architecture" "user-flow" "wireframes" "functional-spec" "data-model")

    for DOC in "${DEV_DOCS[@]}"; do
        TEMPLATE="$METHODOLOGY_DIR/docs/agile-templates/development/${DOC}-template.md"
        TARGET="$TARGET_DIR/docs/development/${DOC}.md"

        if [ -f "$TEMPLATE" ]; then
            cp "$TEMPLATE" "$TARGET"
            sed -i '' "s|YYYY-MM-DD|$TODAY|g" "$TARGET"
        else
            cat > "$TARGET" << DEV_EOF
# ${DOC}

> Version: v0.1 | Date: ${TODAY} | Status: Draft

<!-- 내용을 채워주세요 -->

## Change Log
| Version | Date | Summary |
|---------|------|---------|
| v0.1 | ${TODAY} | Initial draft |
DEV_EOF
        fi
    done
    echo "  + docs/development/ (개발명세서 8종 starter)"
fi

# --- Starter artifacts: governance ---
GOVERNANCE_DOCS=("approval-log" "definition-of-ready-done" "requirements-traceability-matrix" "human-readable-code-guide" "executive-decision-brief")

for DOC in "${GOVERNANCE_DOCS[@]}"; do
    TEMPLATE="$METHODOLOGY_DIR/docs/agile-templates/governance/${DOC}-template.md"
    TARGET="$TARGET_DIR/docs/governance/${DOC}.md"

    if [ -f "$TEMPLATE" ]; then
        cp "$TEMPLATE" "$TARGET"
        sed -i '' "s|YYYY-MM-DD|$TODAY|g" "$TARGET"
    fi
done
echo "  + docs/governance/ (거버넌스 starter)"

echo ""
echo "Done: $TARGET_DIR"
echo ""
echo "Next steps:"
echo "  1. cd $TARGET_DIR"
echo "  2. Edit CLAUDE.md and AGENTS.md — fill in objective, stack, sprint goal"
echo "  3. Review docs/agile-deliverables-map.md"
echo "  4. Run: claude"

case "$PROJECT_TYPE" in
    fullstack)
        echo "  5. Start with: \"CLAUDE.md를 읽고 Discovery Research부터 시작해줘.\""
        echo ""
        echo "Pipeline: Phase 1 리서치 → Gate 1 → Phase 2 기획서 6종 → Gate 2 → Phase 3 개발명세서 8종 → Gate 3 → Phase 4~10"
        ;;
    planning-only)
        echo "  5. Start with: \"CLAUDE.md를 읽고 Discovery Research부터 시작해줘.\""
        echo ""
        echo "Pipeline: Phase 1 리서치 → Gate 1 → Phase 2 기획서 6종"
        ;;
    research)
        echo "  5. Start with: \"CLAUDE.md를 읽고 Discovery Research부터 시작해줘.\""
        echo ""
        echo "Pipeline: Phase 1 리서치"
        ;;
    coding-only)
        echo "  5. Start with: \"CLAUDE.md를 읽고 개발명세서 8종 기준으로 Definition of Ready를 점검해줘.\""
        echo ""
        echo "Pipeline: Phase 3 개발명세서 확인 → Gate 3 → Phase 4~10"
        ;;
esac

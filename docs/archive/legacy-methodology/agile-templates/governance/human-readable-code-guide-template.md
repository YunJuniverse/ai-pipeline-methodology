# Human-Readable Code Guide Template

> Version: v0.1 | Date: YYYY-MM-DD

## 1. Goal
- Code should be easy for a new teammate to read, modify, and review without hidden assumptions.

## 2. Naming Rules
- Use names that describe intent, not implementation trivia
- Prefer full words over unclear abbreviations
- Function names should describe behavior
- Variable names should describe meaning, not temporary position

## 3. Structure Rules
- One function, one responsibility
- Avoid deep nesting when early return is clearer
- Prefer explicit control flow over clever compact code
- Keep domain rules close to domain types and use cases

## 4. Comment Rules
- Comment why, not what, when code is already clear
- Add comments for non-obvious tradeoffs, constraints, and business rules
- Remove stale comments when code changes

## 5. Review Questions
- Can a new engineer understand this file in one read?
- Are names understandable without extra explanation?
- Is control flow easy to follow?
- Are error paths visible and intentional?
- Is the code aligned with current architecture and ADRs?

## 6. Common Anti-Patterns
| Anti-Pattern | Why It Hurts Readability | Preferred Direction |
|--------------|--------------------------|---------------------|
| vague naming | hides intent | use domain-specific names |
| giant functions | too much mental load | split by responsibility |
| mixed layers | blurs architecture | separate concerns clearly |
| hidden side effects | breaks predictability | make effects explicit |

## 7. AI Coding Rules
- AI-generated code must be reviewed for readability, not just correctness
- Passing lint is not enough
- If generated code is hard to explain, refactor before approval
- Readability feedback should be recorded in sprint review artifacts

## 8. Change Log
| Version | Date | Summary |
|---------|------|---------|
| v0.1 | YYYY-MM-DD | Initial draft |

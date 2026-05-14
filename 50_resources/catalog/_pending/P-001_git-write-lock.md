---
id: P-001
title: "Git metadata write blocked in sandboxed agent session"
domain: meta
status: pending
source_observations:
  - 2026-05-07_l1-observe-flow
signature: "git.*(index.lock|refs).*Operation not permitted|cannot lock ref"
created: 2026-05-08
last_seen: 2026-05-07
promotion_rule: "Promote to active Catalog after N>=2 observations or explicit human approval."
---

## 증상 (Symptom)

Agent can edit workspace files but cannot create Git lock/ref files under `.git/`, so branch creation, staging, commit, or push fails.

## 임시 해결 (Current Workaround)

Leave file changes in the workspace and ask the human to run Git commands from a local terminal with normal repository permissions.

## 승급 조건

Same friction appears in another L1 observation, or a human explicitly approves active Catalog promotion.

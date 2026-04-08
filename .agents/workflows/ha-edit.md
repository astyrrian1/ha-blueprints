---
description: Edit Home Assistant blueprint YAML files
---

# HA Blueprint Edit Workflow

> **IMPORTANT:** Before starting, read `.agents/skills/ha-mandatory-workflow/SKILL.md`
> for the full mandatory gate checklist.

## Before editing

// turbo

1. Sync from git:

```bash
git pull --rebase
```

2. Review existing blueprints for conventions:

```bash
ls automation/
```

## While editing

3. Edit blueprint YAML in `automation/`. Every blueprint must:
   - Have a `blueprint:` header with `name`, `description`, `domain`
   - Define all `input:` variables with `name`, `description`, `selector`
   - Use `!input` references — never hardcode entity IDs
   - Include `source_url` pointing to the GitHub raw URL

## After editing

// turbo

4. Lint:

```bash
make lint
```

5. Test by importing the blueprint into the main HA instance.

## Commit

// turbo

6. Commit and push:

```bash
git add -A && git commit -m "<msg>" && git push
```

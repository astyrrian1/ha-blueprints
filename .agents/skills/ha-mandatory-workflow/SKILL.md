---
name: ha-mandatory-workflow
description: >
  MANDATORY GATE — Read this skill BEFORE any Home Assistant blueprint edit.

  TRIGGER THIS SKILL WHEN:
  - Editing ANY blueprint YAML file in automation/
  - Creating or modifying blueprint inputs, triggers, or actions
  - ANY task involving Home Assistant blueprint YAML in this repository
  - User asks to add, change, fix, or debug a blueprint

  NOTE: This repo contains HA blueprints, NOT the main HA config.
  Blueprints are deployed by users importing them — there is no make deploy here.
---

# HA Blueprint Mandatory Workflow Gate

**These blueprints are used by other Home Assistant users. Test before publishing.**

You MUST complete every phase below in order.

---

## Phase 1: Pre-Edit (BEFORE touching any file)

```bash
git pull --rebase
```

Review existing blueprints to understand conventions:
- Check `automation/` for existing blueprints
- Follow the naming and input patterns already established

---

## Phase 2: Edit

Edit blueprint YAML files in `automation/`. Rules:

- Follow the HA blueprint schema exactly
- Every input must have a `name`, `description`, and `selector`
- Use `default` values where sensible
- Test the blueprint in your own HA instance before committing

---

## Phase 3: Validate (AFTER all edits)

```bash
make lint
```

If you have a local HA instance, import and test the blueprint manually.

---

## Phase 4: Commit + Release

```bash
git add -A && git commit -m "<msg>" && git push
```

---

## Common Mistakes to Avoid

- **Don't skip linting** — YAML syntax errors break blueprint imports
- **Don't use hardcoded entity IDs** — blueprints must use input variables
- **Don't forget selectors** — every input needs a proper selector type
- **Test in a real HA instance** — schema validation alone doesn't catch logic errors

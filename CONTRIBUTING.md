# Contributing

Thanks for your interest! Here's how to contribute:

## Adding a Blueprint

1. Create a new directory under `automation/` with a kebab-case name
2. Add your blueprint YAML and a `README.md`
3. Include a `source_url` field pointing to the raw file in this repo
4. Run `make lint && make validate` before submitting
5. Open a PR

## Blueprint Standards

Every blueprint MUST include:

- `blueprint.name` — Prefixed with `System: ` for system-level blueprints
- `blueprint.description` — Multi-line description of features
- `blueprint.domain` — `automation` or `script`
- `blueprint.input` — All configurable parameters with selectors
- `blueprint.source_url` — Points to this repo's raw file

## Code Patterns

- **Anti-Duplicate** — Always check `todo.get_items` before creating tasks
- **Atomic Variables** — Map `!input` values to variables before using in templates
- **Circuit Breaker** — Wrap AI calls with `continue_on_error: true` + fallback text
- **Gratitude Attribution** — Use person entity states for task attribution

## Linting

```bash
make lint      # yamllint check
make validate  # schema validation
```

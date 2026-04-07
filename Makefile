.PHONY: lint validate all

# Configuration — override with: make deploy HA_HOST=192.168.1.100
HA_HOST ?= homeassistant.local
HA_BLUEPRINT_PATH ?= /homeassistant/blueprints/automation/astyrrian1

all: lint validate

lint:
	@echo "🔍 Linting YAML files..."
	@yamllint -c .yamllint.yml .
	@echo "✅ Lint passed"

validate:
	@echo "🔍 Validating blueprint schemas..."
	@for f in $$(find automation -name '*.yaml'); do \
		echo "  Checking $$f..."; \
		python3 -c "\
import yaml, sys; \
data = yaml.safe_load(open('$$f')); \
bp = data.get('blueprint', {}); \
assert 'name' in bp, 'Missing name'; \
assert 'domain' in bp, 'Missing domain'; \
assert 'input' in bp, 'Missing input'; \
assert 'source_url' in bp, 'Missing source_url'; \
print(f'  ✓ {bp[\"name\"]}'); \
" || exit 1; \
	done
	@echo "✅ All blueprints valid"

deploy:
	@echo "📤 Deploying blueprints to $(HA_HOST)..."
	@for dir in automation/*/; do \
		for f in $$dir*.yaml; do \
			[ -f "$$f" ] || continue; \
			echo "  Copying $$f..."; \
			scp "$$f" root@$(HA_HOST):$(HA_BLUEPRINT_PATH)/$$(basename "$$f"); \
		done; \
	done
	@echo "✅ Deploy complete — reload blueprints in HA"

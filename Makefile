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
	@python3 tools/validate_blueprints.py
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

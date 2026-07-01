#!/usr/bin/env python3
"""Validate Home Assistant blueprint YAML files."""

from __future__ import annotations

from pathlib import Path
import sys

import yaml
from yaml.constructor import ConstructorError


ROOT = Path(__file__).resolve().parents[1]
BLUEPRINT_DIRS = ("automation", "script")
REQUIRED_BLUEPRINT_FIELDS = ("name", "domain", "input", "source_url")
VALID_DOMAINS = {"automation", "script"}


class HomeAssistantBlueprintLoader(yaml.SafeLoader):
    """PyYAML loader that accepts HA tags and rejects duplicate keys."""

    def construct_mapping(self, node, deep=False):  # type: ignore[override]
        mapping = {}
        for key_node, value_node in node.value:
            key = self.construct_object(key_node, deep=deep)
            if key in mapping:
                raise ConstructorError(
                    "while constructing a mapping",
                    node.start_mark,
                    f"found duplicate key {key!r}",
                    key_node.start_mark,
                )
            mapping[key] = self.construct_object(value_node, deep=deep)
        return mapping


def construct_ha_tag(loader: HomeAssistantBlueprintLoader, _tag_suffix: str, node):
    if isinstance(node, yaml.ScalarNode):
        return loader.construct_scalar(node)
    if isinstance(node, yaml.SequenceNode):
        return loader.construct_sequence(node)
    if isinstance(node, yaml.MappingNode):
        return loader.construct_mapping(node)
    return None


HomeAssistantBlueprintLoader.add_multi_constructor("!", construct_ha_tag)


def blueprint_files() -> list[Path]:
    files: list[Path] = []
    for dirname in BLUEPRINT_DIRS:
        directory = ROOT / dirname
        if directory.exists():
            files.extend(sorted(directory.rglob("*.yaml")))
    return files


def validate_file(path: Path) -> list[str]:
    relative = path.relative_to(ROOT)
    errors: list[str] = []

    try:
        data = yaml.load(path.read_text(), Loader=HomeAssistantBlueprintLoader)
    except Exception as exc:
        return [f"{relative}: YAML parse failed: {exc}"]

    if data is None:
        return [f"{relative}: empty file"]
    if not isinstance(data, dict):
        return [f"{relative}: top-level document must be a mapping"]

    blueprint = data.get("blueprint")
    if not isinstance(blueprint, dict):
        return [f"{relative}: missing blueprint mapping"]

    for field in REQUIRED_BLUEPRINT_FIELDS:
        if field not in blueprint:
            errors.append(f"{relative}: missing blueprint.{field}")

    domain = blueprint.get("domain")
    if domain not in VALID_DOMAINS:
        errors.append(f"{relative}: invalid blueprint.domain {domain!r}")

    return errors


def main() -> int:
    files = blueprint_files()
    if not files:
        print("No blueprint YAML files found")
        return 1

    errors: list[str] = []
    for path in files:
        errors.extend(validate_file(path))

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    print(f"Validated {len(files)} blueprint file(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

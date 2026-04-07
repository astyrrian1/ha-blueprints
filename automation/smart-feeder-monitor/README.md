# 🐾 Smart Feeder Monitor V11 (Stable)

[![Import Blueprint](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fgithub.com%2Fastyrrian1%2Fha-blueprints%2Fblob%2Fmain%2Fautomation%2Fsmart-feeder-monitor%2Fpet_feeder_monitor.yaml)

Complete smart pet feeder management — monitors food level, desiccant life, and dispenser jams.

## Features

- **Three-Way Monitoring** — Food level, desiccant days remaining, and dispenser jams
- **Per-Issue Tasks** — Creates targeted to-do items: "Refill [Feeder]", "Replace Desiccant: [Feeder]", "Fix Jam: [Feeder]"
- **Anti-Duplicate** — Manages three distinct task types without collision
- **Auto-Complete** — Resolves tasks when issues clear
- **Gratitude Attribution** — Credits the person who services the feeder
- **Entity ID Lookup** — Safe attribution that prevents string errors

## Inputs

| Input | Description | Default |
|-------|-------------|---------|
| Feeder Name | Display name for task titles | "Feeder" |
| Food Status | Binary sensor for empty/low food | Required |
| Desiccant Days | Sensor for desiccant life remaining | Required |
| Dispenser/Jam | Binary sensor for dispenser jams | Required |
| Desiccant Threshold | Days remaining before alerting | 3 |
| To-Do List | Where tasks are created | Required |
| Mobile Target | Devices to notify | Required |

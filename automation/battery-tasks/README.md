# 🪫 Battery Tasks (Individual)

[![Import Blueprint](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fgithub.com%2Fastyrrian1%2Fha-blueprints%2Fblob%2Fmain%2Fautomation%2Fbattery-tasks%2Fbattery_tasks.yaml)

Scans for low batteries and creates **one task per device** in your to-do list.

## Features

- **Per-Device Tasks** — Creates distinct items (e.g., "Replace Battery: Kitchen", "Replace Battery: Hallway")
- **Smart De-Duplication** — Checks if "Replace Battery: [Name]" already exists
- **Summary Notification** — Sends one notification summarizing all added items with percentages

## Inputs

| Input | Description | Default |
|-------|-------------|---------|
| Check Time | Daily scan time | 08:00 |
| Battery Threshold (%) | Battery level that triggers task creation | 5 |
| To-Do List | Where tasks are created | Required |
| Notify Devices | Mobile devices to notify | Required |
| Exclude Sensors | Batteries to skip | None |

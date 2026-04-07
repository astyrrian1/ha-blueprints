# 🔋 Battery Warden V12.4 (Atomic)

[![Import Blueprint](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fgithub.com%2Fastyrrian1%2Fha-blueprints%2Fblob%2Fmain%2Fautomation%2Fbattery-warden%2Fbattery_warden.yaml)

Scans **ALL** battery sensors in your Home Assistant instance every 15 minutes.

## Features

- **Global Scan** — Automatically discovers all battery sensors
- **Atomic Logic** — Calculates attribution in one step to prevent object errors
- **Anti-Duplicate** — Checks for active tasks before creating new ones
- **Gratitude Attribution** — Credits the person who replaces batteries
- **Configurable Threshold** — Set your low battery percentage (default: 20%)
- **Entity Exclusions** — Skip specific batteries you don't want monitored

## Inputs

| Input | Description | Default |
|-------|-------------|---------|
| Low Threshold (%) | Battery level that triggers alerts | 20 |
| Excluded Batteries | Sensors to skip | None |
| To-Do List | Where tasks are created | Required |
| Mobile Notification Target | Devices to notify | Required |
| TTS Entity | Text-to-speech engine | `tts.google_ai_tts_3` |

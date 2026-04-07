# 🌿 Plant Warden V6.0 (Hybrid Scanner)

[![Import Blueprint](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fgithub.com%2Fastyrrian1%2Fha-blueprints%2Fblob%2Fmain%2Fautomation%2Fplant-warden%2Fplant_warden.yaml)

Hybrid plant management — reacts instantly to state changes AND scans every 30 minutes to catch anything missed.

## Features

- **Hybrid Engine** — Instant state-change reactions + periodic safety scan
- **Startup Safety Net** — Checks all plants immediately on HA restart
- **Atomic Logic** — Fixed attribution to prevent crashes
- **Anti-Duplicate** — Safely scans repeatedly without creating duplicate tasks
- **Gratitude Attribution** — Credits the person who waters plants

## Inputs

| Input | Description | Default |
|-------|-------------|---------|
| Plants to Monitor | Plant entities to watch | Required |
| To-Do List | Where watering tasks are created | Required |
| Mobile Target | Devices to notify | Required |
| TTS Entity | Text-to-speech engine | `tts.google_ai_tts_3` |
| Excluded Plants | Plants to skip | None |

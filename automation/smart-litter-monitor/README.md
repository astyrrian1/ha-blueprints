# ✨ Smart Litter Monitor V15.1 (Hybrid)

[![Import Blueprint](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fgithub.com%2Fastyrrian1%2Fha-blueprints%2Fblob%2Fmain%2Fautomation%2Fsmart-litter-monitor%2Flitter_box_monitor.yaml)

Complete litter box management — tracks both cleanliness (full/empty) and refill (insufficient litter) as two independent tasks.

## Features

- **Dual Monitoring** — Cleanliness status (full → needs emptying) and litter level (insufficient → needs refill)
- **Collision-Free Tasks** — Two distinct task types that never interfere with each other
- **Auto-Complete** — Tasks resolve when status returns to normal
- **Gratitude Attribution** — Credits the person who cleans or refills
- **Multi-Device Notifications** — Push alerts to all configured devices

## Inputs

| Input | Description | Default |
|-------|-------------|---------|
| Litter Box Name | Display name for task titles | "Litter Box" |
| Cleanliness Sensor | Detects full/empty status | Required |
| Litter Level Sensor | Detects insufficient litter | Required |
| To-Do List | Where tasks are created | Required |
| Mobile Target | Devices to notify | Required |

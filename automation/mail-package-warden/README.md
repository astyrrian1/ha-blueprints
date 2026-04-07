# 📦 Mail & Package Warden V2.3 (State Guard)

[![Import Blueprint](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fgithub.com%2Fastyrrian1%2Fha-blueprints%2Fblob%2Fmain%2Fautomation%2Fmail-package-warden%2Fmail_package_warden.yaml)

Multi-carrier mail and package management with USPS, UPS, FedEx, and Amazon tracking.

## Features

- **Multi-Carrier** — Monitors USPS mail, USPS/UPS/FedEx/Amazon packages
- **Vision Verification** — Doorbell camera AI confirms package count
- **State Guard** — Prevents double-counting mail after HA reboots
- **Door Interaction** — Auto-completes package tasks when front door opens and porch clears
- **AI Sassy Announcements** — Carrier-specific AI voice broadcasts with circuit-breaker fallback
- **Configurable Volume** — Enforced volume control for announcements

## Inputs

| Input | Description | Default |
|-------|-------------|---------|
| USPS Mail Sensor | Mail piece count sensor | Required |
| USPS/UPS/FedEx/Amazon Package Sensors | Package count sensors per carrier | Required |
| Doorbell Package Count | Vision-based package detection | `sensor.front_door_doorbell_package_count` |
| Front Door Sensor | Door open/close sensor | `binary_sensor.qolsys_panel_front_door` |
| AI Task Entity | For generating sassy announcements | Required |
| To-Do List | Where tasks are created | Required |
| Mobile Target | Devices to notify | Required |
| Announcement Volume | Voice broadcast volume | 0.5 |
| TTS Provider | Text-to-speech engine | `tts.google_ai_tts_3` |

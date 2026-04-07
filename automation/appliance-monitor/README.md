# 🏠 Appliance Monitor V13 (Nuclear)

[![Import Blueprint](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fgithub.com%2Fastyrrian1%2Fha-blueprints%2Fblob%2Fmain%2Fautomation%2Fappliance-monitor%2Fappliance_monitor.yaml)

Full-featured appliance cycle monitoring with AI-generated announcements and hourly nag reminders.

## Features

- **Finish + Power Sensors** — Detects cycle completion and appliance unload
- **Blocking Entity** — Skip alerts when another appliance is running (e.g., dryer blocks washer alerts)
- **AI Sassy Announcements** — Context-aware voice broadcasts ("finished" vs "nag" tone)
- **Hourly Nag** — Repeats alerts every hour if the appliance sits unattended
- **Auto-Complete** — Tasks resolve when power sensor goes off (appliance emptied)
- **Multi-Channel Alerts** — Voice, mobile push, and Signal notifications
- **Circuit Breaker** — Falls back to static messages if AI is unavailable

## Inputs

| Input | Description | Default |
|-------|-------------|---------|
| Appliance Name | Display name (e.g., "Dryer", "Washer") | "Dryer" |
| Finish Sensor | Binary sensor that turns ON when cycle completes | Required |
| Power Status Sensor | Turns OFF when machine is powered down/unloaded | Required |
| Blocking Entity | If ON, skips alerts (e.g., dryer running) | None |
| To-Do List | Where tasks are created | Required |
| Mobile Targets | Devices to notify | Required |
| AI Generator | AI entity for sassy announcements | `ai_task.google_ai_task` |
| TTS Entity | Text-to-speech engine | `tts.google_ai_tts_3` |
| Announcement Volume | Voice broadcast volume | 0.6 |

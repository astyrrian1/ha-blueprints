# 💅 Sassy Task Mistress V4.0 (The Resurrection)

[![Import Blueprint](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fgithub.com%2Fastyrrian1%2Fha-blueprints%2Fblob%2Fmain%2Fautomation%2Fsassy-task-mistress%2Fsassy_task_mistress.yaml)

AI-powered task reminder engine with drag-queen-level sass and urgency-based frequency gating.

## Features

- **Urgency Math** — Frequency gating based on time of day:
  - 4am–12pm: Low urgency (every 3 hours)
  - 12pm–5pm: Medium (every 2 hours)
  - 5pm–8pm: High (hourly)
  - 8pm–10pm: Very High (every 30 minutes)
  - 10pm+: Nuclear (every 15 minutes)
- **Morning Wake-Up Detection** — Waits for motion sensor activity before announcing (4am–6am)
- **Unplugged Trigger** — Fires when phone leaves charger (person waking up)
- **Sleep Guard** — Silences alerts if the designated sleep person is home alone and charging (sleeping)
- **Do Not Disturb** — Configurable end-of-day cutoff to prevent late-night reminders
- **Circuit Breaker** — AI outages degrade to static sass (capped at 5 tasks) instead of crashing
- **Multi-Channel** — Voice broadcast + mobile push with deep link to to-do list

## Inputs

| Input | Description | Default |
|-------|-------------|---------|
| To-Do List | Task source | Required |
| Sleep Person Entity | Person to apply sleep guard | Required |
| Sleep Person Phone Battery State | Phone charging sensor | Required |
| Morning Activity Sensor | Motion sensor for wake-up detection | Required |
| Do Not Disturb After | Stop sending reminders after this time | `23:00:00` |
| Volume | Voice broadcast volume | `0.6` |
| TTS Provider | Text-to-speech engine | `tts.google_ai_tts_3` |
| AI Generator | AI entity for sass generation | `ai_task.google_ai_task` |
| Mobile Targets | Devices to notify | Required |

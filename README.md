# 🏠 Home Assistant Blueprints

A collection of production-ready Home Assistant automation blueprints for smart home task management, monitoring, and AI-powered voice announcements.

## Blueprints

### 🔋 Battery Management

| Blueprint | Description | Import |
|-----------|-------------|--------|
| [Battery Warden V12.4](automation/battery-warden/) | Scans ALL battery sensors globally. Atomic logic, anti-duplicate task creation, and gratitude attribution. | [![Import](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fgithub.com%2Fastyrrian1%2Fha-blueprints%2Fblob%2Fmain%2Fautomation%2Fbattery-warden%2Fbattery_warden.yaml) |
| [Battery Tasks](automation/battery-tasks/) | Per-device battery task creation. Creates distinct to-do items for each low battery device with smart de-duplication. | [![Import](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fgithub.com%2Fastyrrian1%2Fha-blueprints%2Fblob%2Fmain%2Fautomation%2Fbattery-tasks%2Fbattery_tasks.yaml) |

### 🌿 Plant Care

| Blueprint | Description | Import |
|-----------|-------------|--------|
| [Plant Warden V6.0](automation/plant-warden/) | Hybrid plant scanner — reacts instantly to changes AND scans every 30 minutes. Anti-duplicate with startup safety net. | [![Import](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fgithub.com%2Fastyrrian1%2Fha-blueprints%2Fblob%2Fmain%2Fautomation%2Fplant-warden%2Fplant_warden.yaml) |

### 📦 Mail & Packages

| Blueprint | Description | Import |
|-----------|-------------|--------|
| [Mail & Package Warden V2.3](automation/mail-package-warden/) | Multi-carrier mail/package management with USPS, UPS, FedEx, Amazon. Vision verification via doorbell AI. State guard prevents double-counting. | [![Import](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fgithub.com%2Fastyrrian1%2Fha-blueprints%2Fblob%2Fmain%2Fautomation%2Fmail-package-warden%2Fmail_package_warden.yaml) |

### 🐾 Pet Care

| Blueprint | Description | Import |
|-----------|-------------|--------|
| [Smart Feeder Monitor V11](automation/smart-feeder-monitor/) | Monitors food level, desiccant life, and dispenser jams. Creates targeted tasks per issue type with gratitude attribution. | [![Import](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fgithub.com%2Fastyrrian1%2Fha-blueprints%2Fblob%2Fmain%2Fautomation%2Fsmart-feeder-monitor%2Fpet_feeder_monitor.yaml) |
| [Smart Litter Monitor V15.1](automation/smart-litter-monitor/) | Hybrid litter management — cleanliness (full/empty) and refill (insufficient) tracking as two distinct, collision-free tasks. | [![Import](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fgithub.com%2Fastyrrian1%2Fha-blueprints%2Fblob%2Fmain%2Fautomation%2Fsmart-litter-monitor%2Flitter_box_monitor.yaml) |

### 🏠 Appliances

| Blueprint | Description | Import |
|-----------|-------------|--------|
| [Appliance Monitor V13](automation/appliance-monitor/) | Monitors appliance finish/power sensors with AI-generated sassy announcements, hourly nag reminders, blocking entity support, and multi-channel alerts. | [![Import](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fgithub.com%2Fastyrrian1%2Fha-blueprints%2Fblob%2Fmain%2Fautomation%2Fappliance-monitor%2Fappliance_monitor.yaml) |

### 💅 Task Management

| Blueprint | Description | Import |
|-----------|-------------|--------|
| [Sassy Task Mistress V3.0](automation/sassy-task-mistress/) | AI-powered task reminder engine with urgency-based frequency gating, circuit-breaker AI fallback, and morning wake-up detection. | [![Import](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fgithub.com%2Fastyrrian1%2Fha-blueprints%2Fblob%2Fmain%2Fautomation%2Fsassy-task-mistress%2Fsassy_task_mistress.yaml) |

---

## Common Features

These blueprints share a consistent architecture:

- **Anti-Duplicate Logic** — Checks for existing tasks before creating new ones
- **Gratitude Attribution** — Credits the household member who completed a task
- **To-Do Integration** — Creates, reopens, and completes tasks in HA's native to-do lists
- **Mobile Notifications** — Push notifications to configured mobile devices
- **AI Voice Broadcasts** — Optional AI-generated sassy announcements via TTS (with circuit-breaker fallback)

## Requirements

- Home Assistant 2024.1+
- A To-Do list entity (e.g., `todo.household_tasks`)
- Mobile app integration for push notifications
- (Optional) AI Task entity and TTS entity for voice broadcasts
- (Optional) `script.system_smart_voice_broadcast` for centralized voice announcements

## Installation

### One-Click Import

Click any **Import Blueprint** button above, or use this URL pattern:

```
https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https://github.com/astyrrian1/ha-blueprints/blob/main/automation/<folder>/<file>.yaml
```

### Manual Import

1. In Home Assistant: **Settings → Automations & Scenes → Blueprints**
2. Click **Import Blueprint**
3. Paste the raw GitHub URL for the blueprint you want

## Development

```bash
# Clone
git clone https://github.com/astyrrian1/ha-blueprints.git
cd ha-blueprints

# Lint
make lint

# Validate blueprint schemas
make validate

# Deploy to HA (configure HA_HOST)
make deploy HA_HOST=homeassistant.local
```

## License

[MIT](LICENSE)

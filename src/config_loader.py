import json
import os

CONFIG_PATH = os.path.join(os.path.dirname(__file__), "../config/calendar_config.json")


def load_calendar_config():
    """Loads calendar configuration file safely."""
    try:
        with open(CONFIG_PATH, "r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"❌ Error loading config file: {e}")
        return {"calendars": {}}

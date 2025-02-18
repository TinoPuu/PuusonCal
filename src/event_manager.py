from config_loader import load_calendar_config
from file_selector import select_json_file
from calendar_utils import create_calendar_event
from auth import authenticate_google_calendar
from googleapiclient.discovery import build
import json


def load_events(json_path):
    try:
        with open(json_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            return [
                (
                    event["date"],
                    event["start_time"],
                    event["end_time"],
                    event["summary"],
                    event["description"],
                )
                for event in data.get("events", [])
            ]
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"⚠️ Error loading events: {e}")
        return []


def choose_option(options, prompt="Choose an option: "):
    if not options:
        print("🚫 No available options to choose from.")
        return None

    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")

    while True:
        try:
            choice = int(input(f"\n{prompt} ")) - 1
            if 0 <= choice < len(options):
                return options[choice]
        except ValueError:
            pass
        print("🚫 Invalid choice. Try again.")


def process_events():
    selected_file = select_json_file("../input")
    if not selected_file:
        print("🚫 No valid file selected. Exiting.")
        return

    events = load_events(selected_file)
    if not events:
        print("🚫 No valid events found in selected file. Exiting.")
        return

    print(f"\n📜 Selected file: {selected_file}")

    creds = authenticate_google_calendar()
    service = build("calendar", "v3", credentials=creds)

    config = load_calendar_config()
    calendar_ids = config.get("calendars", {})

    if not calendar_ids:
        print("🚨 No calendars found in calendar_config.json. Please add them first.")
        return

    print("\n📅 Choose a calendar to add events:")
    chosen_calendar_name = choose_option(
        list(calendar_ids.keys()), "Enter calendar number: "
    )
    if not chosen_calendar_name:
        print("🚫 No valid calendar selected. Exiting.")
        return

    calendar_id = calendar_ids[chosen_calendar_name]
    print(f"\n📌 Using Calendar: {chosen_calendar_name} ({calendar_id})")

    for date, start, end, summary, description in events:
        create_calendar_event(
            service, calendar_id, date, start, end, summary, description
        )

    print("🎊 All events added successfully!")

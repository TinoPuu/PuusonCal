from googleapiclient.errors import HttpError
from datetime import datetime
import pytz


def create_calendar_event(
    service,
    calendar_id,
    date,
    start_time,
    end_time,
    summary,
    description,
    timezone="Europe/Helsinki",
):
    start_datetime = datetime.strptime(f"{date} {start_time}", "%d.%m.%Y %H:%M")
    end_datetime = datetime.strptime(f"{date} {end_time}", "%d.%m.%Y %H:%M")

    local_tz = pytz.timezone(timezone)
    start_datetime = local_tz.localize(start_datetime).isoformat()
    end_datetime = local_tz.localize(end_datetime).isoformat()

    event = {
        "summary": summary,
        "description": description,
        "start": {"dateTime": start_datetime, "timeZone": timezone},
        "end": {"dateTime": end_datetime, "timeZone": timezone},
    }

    try:
        event_result = (
            service.events().insert(calendarId=calendar_id, body=event).execute()
        )
        print(f"🎉 Event created: {event_result.get('htmlLink')}")
    except HttpError as e:
        print(f"❗ Failed to create event: {e}")

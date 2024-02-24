from gcsa.event import Event
from gcsa.google_calendar import GoogleCalendar

from datetime import datetime, timedelta

CURRENT_CAL_ID = "3a784af39e091f5fb78f38e1f205f562548f7cba1819c5a4c2c0ef7c10194e4b@group.calendar.google.com"

CREDENTIALS_PATH = "/home/glfharris/src/current/.credentials/credentials.json"

calendar = GoogleCalendar(CURRENT_CAL_ID,
        credentials_path=CREDENTIALS_PATH)

event = Event(
        "Appendix",
        start=datetime.now(),
        end=datetime.now() + timedelta(minutes=90),
        description="Some text goes here"
        )

calendar.add_event(event)

for event in calendar:
    print(event)

from gcsa.event import Event
from gcsa.google_calendar import GoogleCalendar

from datetime import datetime, timedelta

import json

from current.api.models import CaseRequest

CURRENT_CAL_ID = "3a784af39e091f5fb78f38e1f205f562548f7cba1819c5a4c2c0ef7c10194e4b@group.calendar.google.com"

CREDENTIALS_PATH = "/home/glfharris/src/current/.credentials/credentials.json"

calendar = GoogleCalendar(CURRENT_CAL_ID,
                          credentials_path=CREDENTIALS_PATH)

def create_case(case_request):
    meta = {}
    meta['priorty'] = case_request.priority
    meta['equipment'] = case_request.equipment

    start_time = datetime.now().replace(hour=7, minute=0)
    end_time = start_time + timedelta(minutes=case_request.estimated_length)

    event = Event(
            case_request.operation_name,
            start=start_time,
            end=end_time,
            description=json.dumps(meta)
)
    
    calendar.add_event(event)

def allocate(day=datetime.today()):

    events = calendar.get_events()
#            time_min=day.replace(hour=0, minute=0),
#            time_max=day.replace(hour=23, minute=59)

#    for e in events:
#        e.meta = json.loads(e.description)

    return events

if __name__ == "__main__":
    events = calendar.get_events()

    for e in events:
        print(e)

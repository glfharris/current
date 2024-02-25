from gcsa.event import Event
from gcsa.google_calendar import GoogleCalendar
import os

from datetime import datetime, timedelta

import json

from current.api.models import CaseRequest

from current.cal import calendar
from current.cal.spoof import gen_spoof_data,del_spoof_data

def list_case(case_request):
    meta = {}
    meta['priority'] = case_request.priority
    meta['equipment'] = case_request.equipment

    if "appendix" in case_request.operation_name.lower():
        meta['equipment'].append("Laproscopic Set")
    if "hernia" in case_request.operation_name.lower():
        meta['equipment'].append("Mesh")
    if "laparotomy" in case_request.operation_name.lower():
        meta['equipment'].append("Scalpel")

    meta['surgeon'] = "Mr Knives"
    meta['anaesthetist'] = "Dr Sleep"

    start_time = datetime.now().replace(hour=7, minute=0)
    end_time = start_time + timedelta(minutes=case_request.estimated_length)

    event = Event(
            case_request.operation_name,
            start=start_time,
            end=end_time,
            location="Theatre 2",
            description=json.dumps(meta)
)
    
    calendar.add_event(event)

def get_todays_events():
    day = datetime.today()
    events = calendar.get_events(
            time_min=day.replace(hour=0, minute=0),
            time_max=day.replace(hour=23, minute=59))

    return events

def allocate(day=datetime.today(), buffer=15):

    events = get_todays_events()

    t = datetime.now().replace(hour=8,minute=0)
    buffer = timedelta(minutes=buffer)

    events=sorted(events, key=lambda e: e.start - e.end, reverse=True)

    for e in events:
        duration = e.end - e.start
        e.start = t
        e.end = e.start + duration
        t = e.end + buffer

        calendar.update_event(e)

    return calendar.get_events(
            time_min=day.replace(hour=0, minute=0),
            time_max=day.replace(hour=23, minute=59))

def apply_meta(event):
    event.meta = json.loads(event.description)
    return event

if __name__ == "__main__":
    events = get_todays_events()

    for event in events:
        print(apply_meta(event).meta['surgeon'])



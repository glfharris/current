from fastapi import FastAPI
from .models import CaseRequest
from gcsa.event import Event
from datetime import datetime, timedelta

from current.cal.main import calendar

app = FastAPI()

@app.post("/caserequest")
async def create_case_request(case: CaseRequest):

    event = Event(
        case.operation_name,
        start=datetime.now(),
        end=datetime.now() + timedelta(minutes=case.estimated_length),
        description=case.requested_date
        )

    calendar.add_event(event)

    return case


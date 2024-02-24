from fastapi import FastAPI
from .models import CaseRequest
from gcsa.event import Event
from datetime import datetime, timedelta

from current.cal.main import create_case

app = FastAPI()

@app.post("/caserequest")
async def create_case_request(case: CaseRequest):
    create_case(case)


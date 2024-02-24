from fastapi import FastAPI, Form, Request
from .models import CaseRequest
from gcsa.event import Event
from datetime import datetime, timedelta
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

# from current.cal.main import calendar

app = FastAPI()

# app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="current/static/templates")
@app.get("/", response_class=HTMLResponse)
async def request_form(request: Request):
    return templates.TemplateResponse(
        "request.html", {"request": request, "result": "res"}
    )

#handle the form, we are expecting it to use the CaseRequest model
@app.post("/case-request")
async def create_case_request(casename: str = Form(...), length: int = Form(...), nhsno: int = Form(...)):
 
    event = Event(
        casename,
        start=datetime.now(),
        end=datetime.now() + timedelta(minutes=length),
        description=nhsno
        )

    # calendar.add_event(event)

    return {"casename": casename, "length": length, "nhsno": nhsno}

# @app.post("/caserequest")
# async def create_case_request(case: CaseRequest):

#     event = Event(
#         case.operation_name,
#         start=datetime.now(),
#         end=datetime.now() + timedelta(minutes=case.estimated_length),
#         description=case.requested_date
#         )

#     calendar.add_event(event)

#     return case


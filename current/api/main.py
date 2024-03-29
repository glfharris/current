from fastapi import FastAPI, Form, Request
from .models import CaseRequest
from gcsa.event import Event
from datetime import datetime, timedelta
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
# from current.cal import calendar
from current.cal.main import list_case, allocate, get_todays_events, apply_meta, badge_status
from current.cal.spoof import del_spoof_data

from datetime import datetime

app = FastAPI()

app.mount("/static", StaticFiles(directory="current/static"), name="static")

templates = Jinja2Templates(directory="current/static/templates")
@app.get("/", response_class=HTMLResponse)
async def request_form(request: Request):
    today = datetime.now().strftime("%Y-%m-%d")
    return templates.TemplateResponse(
            "request.html", {"request": request, "result": "res", "today": today, "title": "List your case" }
    )

#handle the form, we are expecting it to use the CaseRequest model
@app.post("/case-request")
async def create_case_request(casename: str = Form(...), length: int = Form(...), nhsno: int = Form(...)):
    case = CaseRequest(operation_name=casename, estimated_length=length, requested_date=str(datetime.now()), priority=0, equipment=[])
    list_case(case)
    allocate()
    return RedirectResponse("/calendar")

@app.get("/calendar")
@app.post("/calendar")
async def get_calendar(request: Request):
    calendar = [badge_status(apply_meta(event)) for event in get_todays_events()]
    return templates.TemplateResponse(
            "events.html", {"request": request, "calendar": calendar, "title": "Cases"}
    )

@app.get("/delete")
async def del_data(request: Request):
    del_spoof_data()
    return RedirectResponse("/calendar")

@app.get("/allocate")
async def allocate_cases(request: Request):
    allocate()
    return RedirectResponse("/calendar")


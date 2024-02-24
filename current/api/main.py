from fastapi import FastAPI, Form, Request
from .models import CaseRequest
from gcsa.event import Event
from datetime import datetime, timedelta
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
# from current.cal import calendar
from current.cal.main import list_case, allocate

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
    case = CaseRequest(operation_name=casename, estimated_length=length, requested_date=str(datetime.now()), priority=0, equipment=[])
    list_case(case)
    
    return case

@app.get("/calendar")
async def get_calendar(request: Request):
    calendar = allocate()
    return templates.TemplateResponse(
        "events.html", {"request": request, "calendar":calendar}
    )


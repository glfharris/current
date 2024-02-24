from fastapi import FastAPI
from .models import CaseRequest
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

@app.post("/caserequest")
async def create_case_request(case: CaseRequest):

    
    return case


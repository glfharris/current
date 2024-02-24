from current.api.models import CaseRequest

from . import calendar

from datetime import datetime

def gen_spoof_data():
    
    c1 = CaseRequest(operation_name="Appendix",
                     estimated_length=90,
                     requested_date="24/1/24",
                     priority=2,
                     equipment=["Laproscopic Set", "Scalpel"])

    c2 = CaseRequest(operation_name="Hernia",
                     estimated_length=60,
                     requested_date="24/1/24",
                     priority=3,
                     equipment=["Laproscopic Set", "Scalpel", "Mesh"])
                     
    c3 = CaseRequest(operation_name="Laparotomy",
                     estimated_length=180,
                     requested_date="24/1/24",
                     priority=1,
                     equipment=["Cleaver", "Drain", "Rectus Sheath Catheter"])

    return [c1,c2,c3]

def del_spoof_data():
    events = calendar.get_events(
            time_min=datetime.now().replace(hour=0,minute=0),
            time_max=datetime.now().replace(hour=23,minute=59))

    for e in events:
        calendar.delete_event(e) 


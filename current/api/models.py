from pydantic import BaseModel, Field


class CaseRequest(BaseModel):
    operation_name: str = Field(..., title="Operation Name", description="Name of the operation")
    estimated_length: int = Field(..., title="Estimated Length", description="Estimated length of the operation in minutes")
    requested_date: str = Field(..., title="Requested Date", description="Date of the operation")
    priority: int = Field(..., title="Operation Priority", description="0 (most) - 3 (least)")
    equipment: list

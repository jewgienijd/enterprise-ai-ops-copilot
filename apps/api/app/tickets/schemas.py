from typing import Literal

from pydantic import BaseModel, ConfigDict, Field

class TicketCreateRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")
    
    customer_id: int = Field(gt=0)

    subject: str = Field(
        min_length=3,
        max_length=200,
    )

    description: str = Field(
        min_length=10,
        max_length=4000,
    )

    priority: Literal[
        "low",
        "medium",
        "high",
        "critical",
    ]
    
class TicketResponse(BaseModel):
    model_config = ConfigDict(
        from_attributes=True
    )
    
    id: int
    customer_id: int
    subject: str
    description: str
    status: Literal[
        "open",
        "in_progress",
        "resolved",
        "closed",
    ]
    priority: Literal[
        "low",
        "medium",
        "high",
        "critical",
    ]
from fastapi import APIRouter, status

from app.api.dependencies import TicketServiceDep
from app.tickets.schemas import TicketCreateRequest, TicketResponse


router = APIRouter(
    prefix="/tickets",
    tags=["tickets"],
)

@router.get("")
def get_tickets(
    ticket_service: TicketServiceDep,
    ticket_status: str | None = None,
    priority: str | None = None,
):
    return ticket_service.filter_tickets(status=ticket_status, priority=priority)
    

@router.post(
    "",
    status_code=status.HTTP_201_CREATED,
)
def create_ticket(
    request: TicketCreateRequest,
    ticket_service: TicketServiceDep,
) -> TicketResponse:
    ticket = ticket_service.create_ticket(
        customer_id=request.customer_id,
        subject=request.subject,
        description=request.description,
        priority=request.priority,
    )

    return TicketResponse.model_validate(ticket)


@router.get("/{ticket_id}", response_model=TicketResponse)
def get_ticket(
    ticket_id: int,
    ticket_service: TicketServiceDep,
) -> TicketResponse:
    ticket = ticket_service.get_ticket_by_id(ticket_id)

    return TicketResponse.model_validate(ticket)

from typing import Annotated

from fastapi import Depends

from app.customers.service import CustomerService
from app.tickets.service import TicketService


def get_customer_service() -> CustomerService:
    return CustomerService()


CustomerServiceDep = Annotated[
    CustomerService,
    Depends(get_customer_service),
]


def get_ticket_service(
    customer_service: CustomerServiceDep,
) -> TicketService:
    return TicketService(
        customer_service=customer_service,
    )


TicketServiceDep = Annotated[
    TicketService,
    Depends(get_ticket_service),
]

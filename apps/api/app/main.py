from fastapi import FastAPI, HTTPException, status  # type: ignore

from .core.exceptions import ApplicationError
from .customers.exceptions import CustomerNotFoundError, InactiveCustomerError
from .customers.model import Customer
from .customers.service import (
    get_customer_by_id,
    get_customer_tickets,
    list_customers,
)
from .subscriptions.exceptions import SubscriptionNotFoundError
from .subscriptions.service import get_active_customer_subscription
from .tickets.exceptions import InvalidTicketPriorityError, TicketNotFoundError
from .tickets.service import create_ticket, filter_tickets, get_ticket_by_id

app = FastAPI(
    title="Enterprise AI Ops Copilot API",
    version="0.1.0",
)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}

@app.get("/customers")
def get_customers(active: bool | None = None) -> list[Customer]:
    return list_customers(active=active)


@app.get("/customers/{customer_id}")
def get_customer(customer_id: int) -> Customer:
    try:
        return get_customer_by_id(customer_id)
    except CustomerNotFoundError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(exc),
        ) from exc
        
@app.get("/tickets")
def get_tickets(
    ticket_status: str | None = None,
    priority: str | None = None,
):
    return filter_tickets(status=ticket_status, priority=priority)

@app.get("/tickets/{ticket_id}")
def get_ticket(ticket_id: int):
    try:
        return get_ticket_by_id(ticket_id)
    except TicketNotFoundError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(exc),
        ) from exc


def main() -> None:
    customer = get_customer_by_id(1)
    subscription = get_active_customer_subscription(customer.id)
    customer_tickets = get_customer_tickets(customer.id)
    open_tickets = filter_tickets(status="open", customer_id=customer.id)
    escalated_tickets = [
        ticket
        for ticket in customer_tickets
        if ticket.requires_escalation
    ]

    print(f"Customer: {customer.display_name}")
    print(f"Plan: {subscription.plan.title()}")

    print()
    print("Open tickets:")
    for ticket in open_tickets:
        print(f"- {ticket.subject} [{ticket.priority.upper()}]")

    print()
    print("Escalation required:")
    for ticket in escalated_tickets:
        print(f"- {ticket.subject}")

    print()
    print("Ticket creation scenarios:")

    try:
        ticket = create_ticket(
            customer_id=1,
            subject="Cannot access reports",
            description="Reports page returns an error.",
            priority="high",
        )
    except ApplicationError as exc:
        print(f"Error: {exc}")
    else:
        print(f"Created ticket {ticket.id}")
    finally:
        print("Ticket creation attempt finished")

    try:
        create_ticket(
            customer_id=999,
            subject="Test",
            description="Test",
            priority="high",
        )
    except CustomerNotFoundError as exc:
        print(f"Cannot create ticket: {exc}")

    try:
        create_ticket(
            customer_id=5,
            subject="Test",
            description="Test",
            priority="high",
        )
    except InactiveCustomerError as exc:
        print(f"Cannot create ticket: {exc}")

    try:
        create_ticket(
            customer_id=1,
            subject="Test",
            description="Test",
            priority="urgentissimo",
        )
    except (
        CustomerNotFoundError,
        InactiveCustomerError,
        InvalidTicketPriorityError,
    ) as exc:
        print(f"Cannot create ticket: {exc}")

    try:
        get_active_customer_subscription(5)
    except SubscriptionNotFoundError as exc:
        print(f"Subscription problem: {exc}")
        
    


if __name__ == "__main__":
    main()

from .core.exceptions import ApplicationError
from .customers.exceptions import CustomerNotFoundError, InactiveCustomerError
from .customers.service import get_customer_by_id, get_customer_tickets
from .subscriptions.exceptions import SubscriptionNotFoundError
from .subscriptions.service import get_active_customer_subscription
from .tickets.exceptions import InvalidTicketPriorityError
from .tickets.service import create_ticket, filter_tickets
from fastapi import FastAPI # type: ignore

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

from .customers.service import get_customer_by_id, get_customer_tickets
from .subscriptions.service import get_customer_subscription
from .tickets.service import filter_tickets, should_escalate_ticket


def main() -> None:
    customer = get_customer_by_id(1)

    if customer is None:
        return

    subscription = get_customer_subscription(customer.id)
    customer_tickets = get_customer_tickets(customer.id)
    open_tickets = filter_tickets(status="open", customer_id=customer.id)
    escalated_tickets = [
        ticket
        for ticket in customer_tickets
        if should_escalate_ticket(ticket)
    ]

    print(f"Customer: {customer.company_name}")

    if subscription is not None:
        print(f"Plan: {subscription.plan.title()}")

    print()
    print("Open tickets:")
    for ticket in open_tickets:
        print(f"- {ticket.subject} [{ticket.priority.upper()}]")

    print()
    print("Escalation required:")
    for ticket in escalated_tickets:
        print(f"- {ticket.subject}")


if __name__ == "__main__":
    main()

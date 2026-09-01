from ..customers.service import get_customers_by_ids
from ..tickets.service import filter_tickets, get_ticket_sla_hours


def print_support_summary(
    *,
    status: str | None = None,
    priorities: tuple[str, ...] | None = None,
) -> None:
    filtered_tickets = filter_tickets(status=status)

    if priorities is not None:
        priority_filters = set(priorities)
        filtered_tickets = [
            ticket
            for ticket in filtered_tickets
            if ticket.priority in priority_filters
        ]

    report_customers = get_customers_by_ids(
        *[ticket.customer_id for ticket in filtered_tickets]
    )
    customers_by_id = {
        customer.id: customer
        for customer in report_customers
    }

    print("SUPPORT SUMMARY")
    print()
    print("Filters:")
    print(f"status: {status if status is not None else 'all'}")
    print(
        "priorities: "
        f"{', '.join(priorities) if priorities is not None else 'all'}"
    )
    print()
    print(f"Tickets: {len(filtered_tickets)}")
    print()

    for index, ticket in enumerate(filtered_tickets, start=1):
        customer = customers_by_id.get(ticket.customer_id)
        customer_name = customer.display_name if customer is not None else "Unknown"
        escalation = "YES" if ticket.requires_escalation else "NO"

        print(f"{index}. {ticket.subject}")
        print(f"   Customer: {customer_name}")
        print(f"   Priority: {ticket.priority.upper()}")
        print(f"   SLA: {get_ticket_sla_hours(ticket)}h")
        print(f"   Escalation: {escalation}")
        print()

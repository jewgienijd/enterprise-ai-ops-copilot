from ..customers.service import CustomerService
from ..tickets.service import TicketService

customer_service = CustomerService()
ticket_service = TicketService(customer_service=customer_service)


def print_support_summary(
    *,
    status: str | None = None,
    priorities: tuple[str, ...] | None = None,
) -> None:
    filtered_tickets = ticket_service.filter_tickets(status=status)

    if priorities is not None:
        priority_filters = set(priorities)
        filtered_tickets = [
            ticket
            for ticket in filtered_tickets
            if ticket.priority in priority_filters
        ]

    report_customers = customer_service.get_customers_by_ids(
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
        print(f"   SLA: {ticket_service.get_ticket_sla_hours(ticket)}h")
        print(f"   Escalation: {escalation}")
        print()

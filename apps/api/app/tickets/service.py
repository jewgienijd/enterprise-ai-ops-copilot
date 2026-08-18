from ..customers.service import get_customers_by_ids
from ..data.seed import customers, tickets
from .model import Ticket

def get_tickets_by_ids(*ticket_ids: int) -> list[Ticket]:
    print(type(ticket_ids))

    return [
        ticket
        for ticket in tickets
        if ticket.id in ticket_ids
    ]


def get_open_tickets() -> list[Ticket]:
    return [
        ticket
        for ticket in tickets
        if ticket.status == "open"
    ]


def get_high_priority_tickets() -> list[Ticket]:
    return [
        ticket
        for ticket in tickets
        if ticket.priority in ("high", "critical")
    ]

def should_escalate_ticket(ticket: Ticket) -> bool:
    if ticket.priority == "critical":
        return True

    if ticket.priority == "high" and ticket.status == "open":
        return True

    return False

def filter_tickets(
    *,
    status: str | None = None,
    priority: str | None = None,
    customer_id: int | None = None,
    requires_escalation: bool | None = None,
) -> list[Ticket]:
    filtered_tickets = tickets

    if status is not None:
        filtered_tickets = [
            ticket
            for ticket in filtered_tickets
            if ticket.status == status
        ]

    if priority is not None:
        filtered_tickets = [
            ticket
            for ticket in filtered_tickets
            if ticket.priority == priority
        ]

    if customer_id is not None:
        filtered_tickets = [
            ticket
            for ticket in filtered_tickets
            if ticket.customer_id == customer_id
        ]

    if requires_escalation is not None:
        filtered_tickets = [
            ticket
            for ticket in filtered_tickets
            if should_escalate_ticket(ticket) == requires_escalation
        ]

    return filtered_tickets

def count_tickets_by_status() -> dict[str, int]:
    status_counts = {status: 0 for status in Ticket.ALLOWED_STATUSES}

    for ticket in tickets:
        status_counts[ticket.status] += 1

    return status_counts

def group_tickets_by_customer() -> dict[int, list[Ticket]]:
    customer_ticket_map = {customer.id: [] for customer in customers}

    for ticket in tickets:
        customer_ticket_map[ticket.customer_id].append(ticket)

    return customer_ticket_map

def get_tickets_sorted_by_priority() -> list[Ticket]:
    priority_order = {"critical": 0, "high": 1, "medium": 2, "low": 3}

    return sorted(
        tickets,
        key=lambda ticket: priority_order[ticket.priority]
    )


def get_ticket_sla_hours(ticket: Ticket) -> int:
    match ticket.priority:
        case "critical":
            return 1
        case "high":
            return 4
        case "medium":
            return 12
        case "low":
            return 48
        case _:
            raise ValueError(f"Unsupported ticket priority: {ticket.priority}")


def get_ticket_response_strategy(ticket: Ticket) -> str:
    match ticket.priority:
        case "critical":
            return "immediate_escalation"
        case "high":
            return "priority_support"
        case "medium":
            return "standard_support"
        case "low":
            return "async_support"
        case _:
            raise ValueError(f"Unsupported ticket priority: {ticket.priority}")
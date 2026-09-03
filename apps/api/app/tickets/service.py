from ..customers.service import CustomerService
from ..data.seed import customers, tickets
from .exceptions import InvalidTicketPriorityError, TicketNotFoundError
from .model import Ticket


class TicketService:
    def __init__(self, customer_service: CustomerService) -> None:
        self.customer_service = customer_service

    def find_ticket_by_id(self, ticket_id: int) -> Ticket | None:
        for ticket in tickets:
            if ticket.id == ticket_id:
                return ticket

        return None

    def get_ticket_by_id(self, ticket_id: int) -> Ticket:
        ticket = self.find_ticket_by_id(ticket_id)

        if ticket is None:
            raise TicketNotFoundError(ticket_id)

        return ticket

    def get_tickets_by_ids(self, *ticket_ids: int) -> list[Ticket]:
        return [
            ticket
            for ticket in tickets
            if ticket.id in ticket_ids
        ]

    def get_open_tickets(self) -> list[Ticket]:
        return [
            ticket
            for ticket in tickets
            if ticket.is_open
        ]

    def get_high_priority_tickets(self) -> list[Ticket]:
        return [
            ticket
            for ticket in tickets
            if ticket.priority in ("high", "critical")
        ]

    def should_escalate_ticket(self, ticket: Ticket) -> bool:
        return ticket.requires_escalation

    def filter_tickets(
        self,
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
                if ticket.requires_escalation == requires_escalation
            ]

        return filtered_tickets

    def count_tickets_by_status(self) -> dict[str, int]:
        status_counts = {status: 0 for status in Ticket.ALLOWED_STATUSES}

        for ticket in tickets:
            status_counts[ticket.status] += 1

        return status_counts

    def group_tickets_by_customer(self) -> dict[int, list[Ticket]]:
        customer_ticket_map = {customer.id: [] for customer in customers}

        for ticket in tickets:
            customer_ticket_map[ticket.customer_id].append(ticket)

        return customer_ticket_map

    def get_tickets_sorted_by_priority(self) -> list[Ticket]:
        priority_order = {"critical": 0, "high": 1, "medium": 2, "low": 3}

        return sorted(
            tickets,
            key=lambda ticket: priority_order[ticket.priority],
        )

    def get_ticket_sla_hours(self, ticket: Ticket) -> int:
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
                raise InvalidTicketPriorityError(ticket.priority)

    def get_ticket_response_strategy(self, ticket: Ticket) -> str:
        return ticket.response_strategy

    def create_ticket(
        self,
        *,
        customer_id: int,
        subject: str,
        description: str,
        priority: str,
    ) -> Ticket:
        customer = self.customer_service.get_customer_by_id(customer_id)
        self.customer_service.validate_customer_can_create_ticket(customer)

        ticket = Ticket.create_new(
            id=max(ticket.id for ticket in tickets) + 1,
            customer_id=customer_id,
            subject=subject,
            description=description,
            priority=priority,
        )
        tickets.append(ticket)

        return ticket

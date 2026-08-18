from ..core.exceptions import NotFoundError, ValidationError


class TicketNotFoundError(NotFoundError):
    def __init__(self, ticket_id: int):
        self.ticket_id = ticket_id
        super().__init__(f"Ticket with id={ticket_id} was not found")


class InvalidTicketStatusError(ValidationError):
    def __init__(self, status: str):
        self.status = status
        super().__init__(f"Unsupported ticket status: {status}")


class InvalidTicketPriorityError(ValidationError):
    def __init__(self, priority: str):
        self.priority = priority
        super().__init__(f"Unsupported ticket priority: {priority}")

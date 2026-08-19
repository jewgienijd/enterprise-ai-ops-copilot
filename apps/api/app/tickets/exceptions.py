from ..core.exceptions import BusinessRuleError, NotFoundError, ValidationError


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


class InvalidTicketTransitionError(BusinessRuleError):
    def __init__(self, current_status: str, new_status: str):
        self.current_status = current_status
        self.new_status = new_status
        super().__init__(
            f"Cannot change ticket status from {current_status!r} to {new_status!r}"
        )



from .exceptions import InvalidTicketPriorityError, InvalidTicketStatusError


class Ticket:
    ALLOWED_STATUSES = ("open", "in_progress", "resolved", "closed")
    ALLOWED_PRIORITIES = ("low", "medium", "high", "critical")

    def __init__(
        self,
        id: int,
        customer_id: int,
        subject: str,
        description: str,
        status: str,
        priority: str,
    ):
        if status not in self.ALLOWED_STATUSES:
            raise InvalidTicketStatusError(status)

        if priority not in self.ALLOWED_PRIORITIES:
            raise InvalidTicketPriorityError(priority)

        self.id = id
        self.customer_id = customer_id
        self.subject = subject
        self.description = description
        self.status = status
        self.priority = priority

    def __repr__(self) -> str:
        return (
            "Ticket("
            f"id={self.id}, "
            f"customer_id={self.customer_id}, "
            f"subject={self.subject!r}, "
            f"description={self.description!r}, "
            f"status={self.status!r}, "
            f"priority={self.priority!r}"
            ")"
        )

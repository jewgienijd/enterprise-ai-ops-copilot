from dataclasses import dataclass
from typing import ClassVar

from .exceptions import (
    InvalidTicketPriorityError,
    InvalidTicketStatusError,
    InvalidTicketTransitionError,
)


@dataclass
class Ticket:
    ALLOWED_STATUSES: ClassVar[tuple[str, ...]] = (
        "open",
        "in_progress",
        "resolved",
        "closed",
    )
    ALLOWED_PRIORITIES: ClassVar[tuple[str, ...]] = (
        "low",
        "medium",
        "high",
        "critical",
    )
    ALLOWED_TRANSITIONS: ClassVar[dict[str, set[str]]] = {
        "open": {"in_progress", "resolved"},
        "in_progress": {"resolved"},
        "resolved": {"closed", "in_progress"},
        "closed": set(),
    }

    id: int
    customer_id: int
    subject: str
    description: str
    status: str
    priority: str

    @classmethod
    def create_new(
        cls,
        *,
        id: int,
        customer_id: int,
        subject: str,
        description: str,
        priority: str,
    ) -> "Ticket":
        return cls(
            id=id,
            customer_id=customer_id,
            subject=subject,
            description=description,
            status="open",
            priority=priority,
        )

    def __post_init__(self) -> None:
        self._validate_status(self.status)
        self.change_priority(self.priority)

    @property
    def is_open(self) -> bool:
        return self.status == "open"

    @property
    def requires_escalation(self) -> bool:
        if self.priority == "critical":
            return True

        if self.priority == "high" and self.is_open:
            return True

        return False

    @property
    def response_strategy(self) -> str:
        match self.priority:
            case "critical":
                return "immediate_escalation"
            case "high":
                return "priority_support"
            case "medium":
                return "standard_support"
            case "low":
                return "async_support"
            case _:
                raise InvalidTicketPriorityError(self.priority)

    def change_priority(self, priority: str) -> None:
        if priority not in self.ALLOWED_PRIORITIES:
            raise InvalidTicketPriorityError(priority)

        self.priority = priority

    def change_status(self, new_status: str) -> None:
        self._validate_status(new_status)

        if new_status == self.status:
            return

        allowed_next_statuses = self.ALLOWED_TRANSITIONS[self.status]
        if new_status not in allowed_next_statuses:
            raise InvalidTicketTransitionError(self.status, new_status)

        self.status = new_status

    def start_progress(self) -> None:
        self.change_status("in_progress")

    def resolve(self) -> None:
        self.change_status("resolved")

    def close(self) -> None:
        self.change_status("closed")

    def _validate_status(self, status: str) -> None:
        if status not in self.ALLOWED_STATUSES:
            raise InvalidTicketStatusError(status)

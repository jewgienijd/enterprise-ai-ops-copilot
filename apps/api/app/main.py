class Customer:
    def __init__(self, id: int, name: str, email: str, company_name: str, is_active: bool):
        self.id = id
        self.name = name
        self.email = email
        self.company_name = company_name
        self.is_active = is_active

    def __repr__(self) -> str:
        return (
            "Customer("
            f"id={self.id}, "
            f"name={self.name!r}, "
            f"email={self.email!r}, "
            f"company_name={self.company_name!r}, "
            f"is_active={self.is_active}"
            ")"
        )


class Subscription:
    ALLOWED_PLANS = ("starter", "business", "enterprise")

    def __init__(
        self,
        id: int,
        customer_id: int,
        plan: str,
        is_active: bool,
        monthly_price: float,
    ):
        if plan not in self.ALLOWED_PLANS:
            raise ValueError(f"Unsupported subscription plan: {plan}")

        self.id = id
        self.customer_id = customer_id
        self.plan = plan
        self.is_active = is_active
        self.monthly_price = monthly_price

    def __repr__(self) -> str:
        return (
            "Subscription("
            f"id={self.id}, "
            f"customer_id={self.customer_id}, "
            f"plan={self.plan!r}, "
            f"is_active={self.is_active}, "
            f"monthly_price={self.monthly_price}"
            ")"
        )


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
            raise ValueError(f"Unsupported ticket status: {status}")

        if priority not in self.ALLOWED_PRIORITIES:
            raise ValueError(f"Unsupported ticket priority: {priority}")

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


customers = [
    Customer(1, "Alice Morgan", "alice.morgan@acmecloud.example", "Acme Cloud", True),
    Customer(2, "Victor Stone", "victor.stone@globex.example", "Globex", True),
    Customer(3, "Bruce Wayne", "bruce.wayne@wayne.example", "Wayne Enterprises", True),
    Customer(4, "Pepper Potts", "pepper.potts@stark.example", "Stark Industries", True),
    Customer(5, "Ada Wong", "ada.wong@umbrella.example", "Umbrella Corp", False),
]


subscriptions = [
    Subscription(1, 1, "business", True, 199.0),
    Subscription(2, 2, "starter", True, 49.0),
    Subscription(3, 3, "enterprise", True, 999.0),
    Subscription(4, 4, "enterprise", True, 1299.0),
    Subscription(5, 5, "business", False, 199.0),
]


tickets = [
    Ticket(
        1,
        1,
        "Cannot invite new users",
        "Admin user receives an error while sending team invitations.",
        "open",
        "high",
    ),
    Ticket(
        2,
        1,
        "Billing email needs update",
        "Customer wants invoices sent to a new finance mailbox.",
        "in_progress",
        "medium",
    ),
    Ticket(
        3,
        2,
        "Dashboard loads slowly",
        "Main analytics dashboard takes more than 20 seconds to load.",
        "open",
        "medium",
    ),
    Ticket(
        4,
        2,
        "Export contains duplicate rows",
        "CSV export from ticket history includes repeated records.",
        "resolved",
        "low",
    ),
    Ticket(
        5,
        3,
        "SSO login fails",
        "Employees cannot sign in through the configured identity provider.",
        "in_progress",
        "critical",
    ),
    Ticket(
        6,
        3,
        "Add audit log retention",
        "Customer requests a longer audit log retention period.",
        "open",
        "high",
    ),
    Ticket(
        7,
        4,
        "Webhook delivery retries",
        "Webhook endpoint is healthy, but events are still marked as failed.",
        "open",
        "high",
    ),
    Ticket(
        8,
        4,
        "New workspace setup",
        "Customer needs a separate workspace for a research team.",
        "closed",
        "medium",
    ),
    Ticket(
        9,
        5,
        "Subscription cancellation question",
        "Customer asks what happens to archived support tickets after cancellation.",
        "resolved",
        "low",
    ),
    Ticket(
        10,
        5,
        "Security alert review",
        "Customer asks support to review an unexpected admin login alert.",
        "open",
        "critical",
    ),
]


def get_customer_by_id(customer_id: int):
    for customer in customers:
        if customer.id == customer_id:
            return customer

    return None


def get_customer_subscription(customer_id: int):
    for subscription in subscriptions:
        if subscription.customer_id == customer_id:
            return subscription

    return None


def get_customer_tickets(customer_id: int) -> list[Ticket]:
    return [
        ticket
        for ticket in tickets
        if ticket.customer_id == customer_id
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
    status: str | None = None,
    priority: str | None = None,
    customer_id: int | None = None,
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

def get_customer_ids_with_critical_tickets() -> set[int]:
    critical_ticket_customer_ids = set()

    for ticket in tickets:
        if ticket.priority == "critical":
            critical_ticket_customer_ids.add(ticket.customer_id)

    return critical_ticket_customer_ids

def get_tickets_sorted_by_priority() -> list[Ticket]:
    priority_order = {"critical": 0, "high": 1, "medium": 2, "low": 3}

    return sorted(
        tickets,
        key=lambda ticket: priority_order[ticket.priority]
    )
    
customer_names = [
    "Acme Cloud",
    "Globex",
    "Wayne Enterprises",
]

health_scores = [
    88,
    63,
    95,
]

for q, a in zip(customer_names, health_scores):
    print('{0}: {1}'.format(q, a))


if __name__ == "__main__":
    customer = get_customer_by_id(1)

    if customer is not None:
        subscription = get_customer_subscription(customer.id)
        customer_tickets = get_customer_tickets(customer.id)
        open_customer_tickets = filter_tickets(status="open")
        escalated_tickets = []

        for ticket in customer_tickets:
            if ticket.status == "open":
                open_customer_tickets.append(ticket)

            if should_escalate_ticket(ticket):
                escalated_tickets.append(ticket)

        print(f"Customer: {customer.company_name}")

        if subscription is not None:
            print(f"Plan: {subscription.plan.title()}")

        print()
        print("Open tickets:")
        for ticket in open_customer_tickets:
            print(f"- {ticket.subject} [{ticket.priority.upper()}]")

        print()
        print("Escalation required:")
        for ticket in escalated_tickets:
            print(f"- {ticket.subject}")

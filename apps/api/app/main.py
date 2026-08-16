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
    customer_tickets = []

    for ticket in tickets:
        if ticket.customer_id == customer_id:
            customer_tickets.append(ticket)

    return customer_tickets


def get_open_tickets() -> list[Ticket]:
    open_tickets = []

    for ticket in tickets:
        if ticket.status == "open":
            open_tickets.append(ticket)

    return open_tickets


def get_high_priority_tickets() -> list[Ticket]:
    high_priority_tickets = []

    for ticket in tickets:
        if ticket.priority in ("high", "critical"):
            high_priority_tickets.append(ticket)

    return high_priority_tickets


def should_escalate_ticket(ticket: Ticket) -> bool:
    if ticket.priority == "critical":
        return True

    if ticket.priority == "high" and ticket.status == "open":
        return True

    return False


if __name__ == "__main__":
    customer = get_customer_by_id(1)

    if customer is not None:
        subscription = get_customer_subscription(customer.id)
        customer_tickets = get_customer_tickets(customer.id)
        open_customer_tickets = []
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

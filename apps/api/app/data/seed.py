from ..customers.model import Customer
from ..subscriptions.model import Subscription
from ..tickets.model import Ticket

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

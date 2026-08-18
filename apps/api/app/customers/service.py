from ..data.seed import customers, tickets
from ..tickets.model import Ticket
from .model import Customer


def get_customer_by_id(customer_id: int):
    for customer in customers:
        if customer.id == customer_id:
            return customer

    return None


def get_customer_tickets(customer_id: int) -> list[Ticket]:
    return [
        ticket
        for ticket in tickets
        if ticket.customer_id == customer_id
    ]
    
def get_customer_ids_with_critical_tickets() -> set[int]:
    critical_ticket_customer_ids = set()

    for ticket in tickets:
        if ticket.priority == "critical":
            critical_ticket_customer_ids.add(ticket.customer_id)

    return critical_ticket_customer_ids

def get_customers_by_ids(*customer_ids: int) -> list[Customer]:
    unique_customer_ids = set(customer_ids)

    return [
        customer
        for customer in customers
        if customer.id in unique_customer_ids
    ]

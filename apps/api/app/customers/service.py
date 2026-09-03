from ..data.seed import customers, tickets
from ..tickets.model import Ticket
from .exceptions import (
    CustomerNotFoundError,
    InactiveCustomerError,
    InvalidCustomerIdError,
)
from .model import Customer


class CustomerService:
    def find_customer_by_id(self, customer_id: int) -> Customer | None:
        for customer in customers:
            if customer.id == customer_id:
                return customer

        return None

    def get_customer_by_id(self, customer_id: int) -> Customer:
        customer = self.find_customer_by_id(customer_id)

        if customer is None:
            raise CustomerNotFoundError(customer_id)

        return customer

    def validate_customer_can_create_ticket(self, customer: Customer) -> None:
        if customer.is_active is False:
            raise InactiveCustomerError(customer.id)

    def parse_customer_id(self, value: str) -> int:
        try:
            return int(value)
        except ValueError as exc:
            raise InvalidCustomerIdError(value) from exc

    def list_customers(self, active: bool | None = None) -> list[Customer]:
        if active is None:
            return customers

        return [
            customer
            for customer in customers
            if customer.is_active == active
        ]

    def get_customer_tickets(self, customer_id: int) -> list[Ticket]:
        return [
            ticket
            for ticket in tickets
            if ticket.customer_id == customer_id
        ]

    def get_customer_ids_with_critical_tickets(self) -> set[int]:
        critical_ticket_customer_ids = set()

        for ticket in tickets:
            if ticket.priority == "critical":
                critical_ticket_customer_ids.add(ticket.customer_id)

        return critical_ticket_customer_ids

    def get_customers_by_ids(self, *customer_ids: int) -> list[Customer]:
        unique_customer_ids = set(customer_ids)

        return [
            customer
            for customer in customers
            if customer.id in unique_customer_ids
        ]

from ..core.exceptions import BusinessRuleError, NotFoundError, ValidationError


class CustomerNotFoundError(NotFoundError):
    def __init__(self, customer_id: int):
        self.customer_id = customer_id
        super().__init__(f"Customer with id={customer_id} was not found")


class InactiveCustomerError(BusinessRuleError):
    def __init__(self, customer_id: int):
        self.customer_id = customer_id
        super().__init__(f"Customer with id={customer_id} is inactive")


class InvalidCustomerIdError(ValidationError):
    def __init__(self, value: str):
        self.value = value
        super().__init__(f"Customer id must be an integer, got {value!r}")

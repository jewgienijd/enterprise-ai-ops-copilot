from ..core.exceptions import BusinessRuleError, NotFoundError, ValidationError


class CustomerNotFoundError(NotFoundError):
    code = "customer_not_found"

    def __init__(self, customer_id: int):
        self.customer_id = customer_id
        super().__init__(f"Customer with id={customer_id} was not found")


class InactiveCustomerError(BusinessRuleError):
    code = "inactive_customer"

    def __init__(self, customer_id: int):
        self.customer_id = customer_id
        super().__init__(f"Customer with id={customer_id} is inactive")


class InvalidCustomerIdError(ValidationError):
    code = "invalid_customer_id"

    def __init__(self, value: str):
        self.value = value
        super().__init__(f"Customer id must be an integer, got {value!r}")

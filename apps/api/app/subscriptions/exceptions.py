from ..core.exceptions import NotFoundError, ValidationError


class SubscriptionNotFoundError(NotFoundError):
    def __init__(self, customer_id: int):
        self.customer_id = customer_id
        super().__init__(
            f"Active subscription for customer id={customer_id} was not found"
        )


class InvalidSubscriptionPlanError(ValidationError):
    def __init__(self, plan: str):
        self.plan = plan
        super().__init__(f"Unsupported subscription plan: {plan}")

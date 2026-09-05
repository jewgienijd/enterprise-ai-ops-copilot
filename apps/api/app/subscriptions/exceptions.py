from ..core.exceptions import NotFoundError, ValidationError


class SubscriptionNotFoundError(NotFoundError):
    code = "subscription_not_found"

    def __init__(self, customer_id: int):
        self.customer_id = customer_id
        super().__init__(
            f"Active subscription for customer id={customer_id} was not found"
        )


class InvalidSubscriptionPlanError(ValidationError):
    code = "invalid_subscription_plan"

    def __init__(self, plan: str):
        self.plan = plan
        super().__init__(f"Unsupported subscription plan: {plan}")

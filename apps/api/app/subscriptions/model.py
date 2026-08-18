from .exceptions import InvalidSubscriptionPlanError


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
            raise InvalidSubscriptionPlanError(plan)

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

from dataclasses import dataclass
from typing import ClassVar

from .exceptions import InvalidSubscriptionPlanError


@dataclass
class Subscription:
    ALLOWED_PLANS: ClassVar[tuple[str, ...]] = ("starter", "business", "enterprise")

    id: int
    customer_id: int
    plan: str
    is_active: bool
    monthly_price: float

    def __post_init__(self) -> None:
        if self.plan not in self.ALLOWED_PLANS:
            raise InvalidSubscriptionPlanError(self.plan)

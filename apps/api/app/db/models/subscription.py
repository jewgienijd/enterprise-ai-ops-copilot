from sqlalchemy import Boolean, ForeignKey, Numeric, String
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class SubscriptionORM(Base):
    __tablename__ = "subscriptions"

    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    customer_id: Mapped[int] = mapped_column(
        ForeignKey("customers.id")
    )

    plan: Mapped[str] = mapped_column(
        String(20)
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
    )

    monthly_price: Mapped[float] = mapped_column(
        Numeric(10, 2)
    )

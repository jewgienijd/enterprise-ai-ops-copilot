from ..data.seed import subscriptions
from .exceptions import SubscriptionNotFoundError
from .model import Subscription


def find_customer_subscription(customer_id: int) -> Subscription | None:
    for subscription in subscriptions:
        if subscription.customer_id == customer_id:
            return subscription

    return None


def get_customer_subscription(customer_id: int) -> Subscription | None:
    return find_customer_subscription(customer_id)


def find_active_customer_subscription(customer_id: int) -> Subscription | None:
    for subscription in subscriptions:
        if subscription.customer_id == customer_id and subscription.is_active:
            return subscription

    return None


def get_active_customer_subscription(customer_id: int) -> Subscription:
    subscription = find_active_customer_subscription(customer_id)

    if subscription is None:
        raise SubscriptionNotFoundError(customer_id)

    return subscription

from ..data.seed import subscriptions

def get_customer_subscription(customer_id: int):
    for subscription in subscriptions:
        if subscription.customer_id == customer_id:
            return subscription

    return None

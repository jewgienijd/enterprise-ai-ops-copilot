from fastapi import APIRouter

from app.api.dependencies import CustomerServiceDep
from app.customers.model import Customer


router = APIRouter(
    prefix="/customers",
    tags=["customers"],
)

@router.get("")
def get_customers(      
    customer_service: CustomerServiceDep,
    active: bool | None = None,
) -> list[Customer]:
    return customer_service.list_customers(active=active)


@router.get("/{customer_id}", response_model=Customer)
def get_customer(
    customer_id: int,
    customer_service: CustomerServiceDep,
) -> Customer:
    return customer_service.get_customer_by_id(customer_id)

from fastapi import APIRouter

from app.api.routes import (
    customers,
    health,
    tickets,
)

api_router = APIRouter(prefix="/api/v1")

api_router.include_router(
    health.router
)

api_router.include_router(
    customers.router
)

api_router.include_router(
    tickets.router
)
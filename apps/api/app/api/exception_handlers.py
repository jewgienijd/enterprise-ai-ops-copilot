from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse

from app.core.exceptions import (
    ApplicationError,
    BusinessRuleError,
    NotFoundError,
    ValidationError,
)


def error_response(
    exc: ApplicationError,
    status_code: int,
) -> JSONResponse:
    return JSONResponse(
        status_code=status_code,
        content={
            "error": exc.code,
            "detail": str(exc),
        },
    )


async def not_found_error_handler(
    request: Request,
    exc: NotFoundError,
) -> JSONResponse:
    return error_response(exc, status.HTTP_404_NOT_FOUND)


async def validation_error_handler(
    request: Request,
    exc: ValidationError,
) -> JSONResponse:
    return error_response(exc, status.HTTP_400_BAD_REQUEST)


async def business_rule_error_handler(
    request: Request,
    exc: BusinessRuleError,
) -> JSONResponse:
    return error_response(exc, status.HTTP_409_CONFLICT)


def register_exception_handlers(
    app: FastAPI,
) -> None:
    app.add_exception_handler(
        NotFoundError,
        not_found_error_handler,
    )
    app.add_exception_handler(
        ValidationError,
        validation_error_handler,
    )
    app.add_exception_handler(
        BusinessRuleError,
        business_rule_error_handler,
    )

import logging
from typing import Literal

from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from pydantic import BaseModel, ValidationError
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError

from app.db.session import get_engine


logger = logging.getLogger(__name__)


class HealthResponse(BaseModel):
    status: Literal["ok"]


class DatabaseUnavailableResponse(BaseModel):
    status: Literal["unavailable"]


router = APIRouter(prefix="/api/v1")


@router.get("/health", response_model=HealthResponse, tags=["Salud"])
async def health() -> HealthResponse:
    return HealthResponse(status="ok")


@router.get(
    "/health/database",
    response_model=HealthResponse,
    responses={
        status.HTTP_503_SERVICE_UNAVAILABLE: {
            "model": DatabaseUnavailableResponse,
            "description": "Base de datos no disponible.",
        },
    },
    tags=["Salud"],
)
def database_health() -> HealthResponse | JSONResponse:
    try:
        with get_engine().connect() as connection:
            connection.execute(text("SELECT 1")).scalar_one()
    except (ValidationError, SQLAlchemyError) as error:
        logger.warning("Database health check failed (%s)", type(error).__name__)
        return JSONResponse(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            content=DatabaseUnavailableResponse(status="unavailable").model_dump(),
        )

    return HealthResponse(status="ok")

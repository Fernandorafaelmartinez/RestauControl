from pathlib import Path
from typing import Literal

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class DatabaseSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_prefix="SQLSERVER_",
        env_file=Path(__file__).resolve().parents[2] / ".env",
        env_file_encoding="utf-8",
        extra="ignore",
        hide_input_in_errors=True,
    )

    host: str
    port: int | None = Field(default=None, ge=1, le=65535)
    database: str = "RestauControlDB"
    driver: str = "ODBC Driver 18 for SQL Server"
    environment: Literal["local", "production"] = "production"

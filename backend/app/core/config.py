from pathlib import Path

from pydantic import Field, SecretStr
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
    port: int = Field(default=1433, ge=1, le=65535)
    database: str = "RestauControlDB"
    username: str
    password: SecretStr
    driver: str = "ODBC Driver 18 for SQL Server"

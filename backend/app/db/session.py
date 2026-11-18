from functools import lru_cache

from sqlalchemy import URL, create_engine
from sqlalchemy.orm import Session, sessionmaker

from app.core.config import DatabaseSettings


@lru_cache
def get_session_factory() -> sessionmaker[Session]:
    settings = DatabaseSettings()
    url = URL.create(
        "mssql+pyodbc",
        username=settings.username,
        password=settings.password.get_secret_value(),
        host=settings.host,
        port=settings.port,
        database=settings.database,
        query={
            "driver": settings.driver,
            "Encrypt": "yes",
            "TrustServerCertificate": "no",
        },
    )
    return sessionmaker(bind=create_engine(url, pool_pre_ping=True))

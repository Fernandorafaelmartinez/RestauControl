from functools import lru_cache

from sqlalchemy import URL, Engine, create_engine
from sqlalchemy.orm import Session, sessionmaker

from app.core.config import DatabaseSettings


@lru_cache
def get_engine() -> Engine:
    settings = DatabaseSettings()
    trust_server_certificate = "yes" if settings.environment == "local" else "no"
    url = URL.create(
        "mssql+pyodbc",
        host=settings.host,
        port=settings.port,
        database=settings.database,
        query={
            "driver": settings.driver,
            "Encrypt": "yes",
            "TrustServerCertificate": trust_server_certificate,
        },
    )
    # The pyodbc dialect adds Trusted_Connection=yes for a URL without credentials.
    return create_engine(url, pool_pre_ping=True, connect_args={"timeout": 5})


@lru_cache
def get_session_factory() -> sessionmaker[Session]:
    return sessionmaker(bind=get_engine())

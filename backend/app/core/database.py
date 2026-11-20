from collections.abc import AsyncIterator
from typing import Annotated, Final

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from core.settings import settings
from schemas.core.database import DatabaseSettings


class DatabaseConfig:
    """Create an async engine and sessions from database or application settings."""

    def __init__(self, settings: DatabaseSettings) -> None:
        self.engine = create_async_engine(settings.connection_url)
        self.session_factory = async_sessionmaker(self.engine, expire_on_commit=False)

    async def get_session(self) -> AsyncIterator[AsyncSession]:
        """Yield a request session; callers explicitly commit writes."""
        async with self.session_factory() as session:
            yield session

    async def dispose(self) -> None:
        """Release pooled connections during application shutdown."""
        await self.engine.dispose()


database: Final[DatabaseConfig] = DatabaseConfig(settings)

DatabaseSession = Annotated[AsyncSession, Depends(database.get_session)]

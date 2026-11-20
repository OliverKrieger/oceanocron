from typing import Literal

from schemas.core.database import DatabaseSettings


class Settings(DatabaseSettings):
    """Immutable application configuration schema."""

    environment: Literal["local", "test", "uat", "prod"] = "local"
    debug: bool = False

    app_name: str
    app_version: str = "0.0.1"

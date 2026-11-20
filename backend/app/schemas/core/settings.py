from typing import Literal

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Immutable application configuration schema."""

    model_config = SettingsConfigDict(
        frozen=True,
        env_file=".backend.env",
        env_file_encoding="utf-8",
        env_nested_delimiter="__",
        extra="ignore",
    )

    environment: Literal["local", "test", "uat", "prod"] = "local"
    debug: bool = False

    app_name: str
    app_version: str = "0.0.1"
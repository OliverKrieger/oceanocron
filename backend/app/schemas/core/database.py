from pydantic_settings import BaseSettings, SettingsConfigDict


class DatabaseSettings(BaseSettings):
    """Immutable database configuration, usable without application settings."""

    model_config = SettingsConfigDict(
        frozen=True,
        env_file=".backend.env",
        env_file_encoding="utf-8",
        env_nested_delimiter="__",
        extra="ignore",
    )

    connection_url: str = "sqlite+aiosqlite:///./oceanocron.db"

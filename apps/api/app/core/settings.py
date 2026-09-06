from functools import lru_cache
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

APP_ROOT = Path(__file__).resolve().parents[1]


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=APP_ROOT / ".env",
        extra="ignore",
    )

    database_url: str


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()

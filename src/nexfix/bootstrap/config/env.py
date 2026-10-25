from pydantic_settings import BaseSettings, SettingsConfigDict

from nexfix.bootstrap.config.settings import AppSettings


class BaseEnvSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


class AppEnvConfig(BaseEnvSettings, AppSettings):
    model_config = SettingsConfigDict(env_prefix="APP_")

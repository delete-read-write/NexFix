from nexfix.bootstrap.config.env import AppEnvConfig, BaseEnvSettings, LoggingEnvConfig
from nexfix.bootstrap.config.settings import AppSettings, LoggingSettings


def _load_env[E: BaseEnvSettings](env_cls: type[E]) -> E:
    return env_cls()


def load_app_settings() -> AppSettings:
    return _load_env(AppEnvConfig)


def load_logging_settings() -> LoggingSettings:
    return _load_env(LoggingEnvConfig)

from nexfix.bootstrap.config.env import AppEnvConfig, BaseEnvSettings
from nexfix.bootstrap.config.settings import AppSettings


def _load_env[E: BaseEnvSettings](env_cls: type[E]) -> E:
    return env_cls()


def load_app_settings() -> AppSettings:
    return _load_env(AppEnvConfig)

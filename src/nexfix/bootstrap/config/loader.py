from nexfix.bootstrap.config.env import BaseEnvSettings


def _load_env[E: BaseEnvSettings](env_cls: type[E]) -> E:
    return env_cls()

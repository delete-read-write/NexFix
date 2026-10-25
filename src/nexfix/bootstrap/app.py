from fastapi import FastAPI

from nexfix.bootstrap.config.loader import load_app_settings, load_logging_settings
from nexfix.bootstrap.config.settings import AppSettings, LoggingSettings
from nexfix.bootstrap.setup import setup_logging


def create_app(
    *,
    app_settings: AppSettings | None = None,
    logging_settings: LoggingSettings | None = None,
) -> FastAPI:
    if logging_settings is None:
        logging_settings = load_logging_settings()
    setup_logging(settings=logging_settings)

    if app_settings is None:
        app_settings = load_app_settings()

    app = FastAPI(
        debug=app_settings.debug_mode,
        title=app_settings.service_name,
        version=app_settings.service_version,
    )

    return app

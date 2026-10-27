from collections.abc import AsyncIterator, Callable
from contextlib import AbstractAsyncContextManager, asynccontextmanager

from dishka import AsyncContainer, make_async_container
from dishka.integrations.fastapi import setup_dishka
from fastapi import FastAPI

from nexfix.bootstrap.config.loader import load_app_settings, load_logging_settings
from nexfix.bootstrap.config.settings import AppSettings, LoggingSettings
from nexfix.bootstrap.setup import setup_logging


def make_lifespan(
    dishka_container: AsyncContainer,
) -> Callable[[FastAPI], AbstractAsyncContextManager[None]]:
    @asynccontextmanager
    async def lifespan(_: FastAPI) -> AsyncIterator[None]:
        try:
            yield
        finally:
            await dishka_container.close()

    return lifespan


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

    dishka_async_container = make_async_container(
        context={
            AppSettings: app_settings,
            LoggingSettings: logging_settings,
        }
    )

    app = FastAPI(
        debug=app_settings.debug_mode,
        title=app_settings.service_name,
        version=app_settings.service_version,
        lifespan=make_lifespan(dishka_async_container),
    )

    setup_dishka(dishka_async_container, app)

    return app

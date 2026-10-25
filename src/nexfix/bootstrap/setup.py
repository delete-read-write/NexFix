import logging

from nexfix.bootstrap.config.settings import LoggingSettings

logger = logging.getLogger(__name__)


def setup_logging(*, settings: LoggingSettings) -> None:
    logging.basicConfig(
        format=settings.fmt,
        datefmt=settings.datefmt,
        level=settings.level,
        force=True,
    )
    logger.info("Logging is set up!")

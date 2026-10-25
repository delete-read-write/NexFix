from typing import Literal

from pydantic import BaseModel

type LoggingLevel = Literal[
    "INFO",
    "DEBUG",
    "WARNING",
    "ERROR",
    "CRITICAL",
]


class AppSettings(BaseModel):
    service_name: str = "NexFix"
    service_version: str = "1.0.0"
    debug_mode: bool = False
    root_path: str = "/"


class LoggingSettings(BaseModel):
    level: LoggingLevel = "INFO"
    fmt: str = (
        "[%(asctime)s.%(msecs)03d] [%(threadName)s] %(funcName)20s %(module)s:%(lineno)d %(levelname)-8s - %(message)s"
    )
    datefmt: str = "%Y-%m-%d %H:%M:%S"

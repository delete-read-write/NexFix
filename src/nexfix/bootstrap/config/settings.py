from pydantic import BaseModel


class AppSettings(BaseModel):
    service_name: str = "NexFix"
    service_version: str = "1.0.0"
    debug_mode: bool = False
    root_path: str = "/"

#!/usr/local/bin/python3 -I
import os
import sys

APP = "nexfix.bootstrap.app:create_app"


def start() -> None:
    os.execvp(
        "granian",
        [
            "granian",
            "--interface", "asgi",
            "--host", os.getenv("GRANIAN_HOST", "0.0.0.0"),
            "--port", os.getenv("GRANIAN_PORT", "8000"),
            "--workers", os.getenv("GRANIAN_WORKERS", "1"),
            "--loop", os.getenv("GRANIAN_LOOP", "uvloop"),
            "--factory",
            APP,
        ],
    )

def main() -> None:
    match sys.argv[1:]:
        case [] | ["start"]:
            start()
        case [command, *args]:
            os.execvp(command, [command, *args])

if __name__ == "__main__":
    main()

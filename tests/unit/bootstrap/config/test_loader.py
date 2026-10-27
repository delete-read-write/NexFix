import pytest

from nexfix.bootstrap.config.loader import load_app_settings, load_logging_settings


def test_load_app_settings_reads_env_vars(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("APP_SERVICE_NAME", "test-service")
    monkeypatch.setenv("APP_SERVICE_VERSION", "test-version")
    monkeypatch.setenv("APP_DEBUG_MODE", "1")

    sut = load_app_settings()

    assert sut.service_name == "test-service"
    assert sut.service_version == "test-version"
    assert sut.debug_mode is True


@pytest.mark.parametrize("logging_level", ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"])
def test_load_logging_settings_reads_env_vars(monkeypatch: pytest.MonkeyPatch, logging_level: str) -> None:
    monkeypatch.setenv("LOGGING_LEVEL", logging_level)
    monkeypatch.setenv("LOGGING_FMT", "test-format")
    monkeypatch.setenv("LOGGING_DATEFMT", "test-date-format")

    sut = load_logging_settings()

    assert sut.level == logging_level
    assert sut.fmt == "test-format"
    assert sut.datefmt == "test-date-format"

from __future__ import annotations

from pathlib import Path

import pytest

from aura.config import REPO_ROOT, Settings


@pytest.mark.parametrize(
    "raw,expected",
    [
        ("*", ["*"]),  # what docker-compose.yml and .env.example set
        ("https://a.example, https://b.example", ["https://a.example", "https://b.example"]),
        ('["https://a.example"]', ["https://a.example"]),
    ],
)
def test_cors_origins_from_env(monkeypatch: pytest.MonkeyPatch, raw: str, expected: list[str]) -> None:
    monkeypatch.setenv("AURA_CORS_ORIGINS", raw)
    assert Settings(_env_file=None).cors_origins == expected


def test_env_example_loads() -> None:
    env_example = Path(REPO_ROOT) / ".env.example"
    settings = Settings(_env_file=env_example)
    assert settings.cors_origins == ["*"]

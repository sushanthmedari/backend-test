from __future__ import annotations

import os
from pathlib import Path

import pytest

from catalog.db import connect, init_schema


@pytest.fixture()
def db_path(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Path:
    path = tmp_path / "exercise.db"
    # SQLAlchemy-style URL; connect() must resolve this correctly.
    monkeypatch.setenv("CATALOG_DATABASE_URL", f"sqlite:///{path}")
    return path


@pytest.fixture()
def conn(db_path: Path):
    connection = connect()
    init_schema(connection)
    yield connection
    connection.close()
    if db_path.exists():
        # Ensure env isolation across tests.
        os.environ.pop("CATALOG_DATABASE_URL", None)

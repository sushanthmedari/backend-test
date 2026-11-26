"""SQLite access for the exercise store.

Task 1 focuses here: the database layer does not work correctly yet.

Quick orientation (prior SQLite experience not required):
  - SQLite is a local file database. Python talks to it with the built-in
    `sqlite3` module — no server to install.
  - `sqlite3.connect(...)` expects a **filesystem path** (or ":memory:"),
    e.g. Path("catalog.db") or "/tmp/exercise.db".
  - Config here may look like a URL: `sqlite:///some/path.db`. That is a
    common app style, but it is **not** a raw path. Use
    `database_path_from_url(...)` (already implemented below) to turn the
    URL into a Path, then connect to that path.
  - After INSERT/UPDATE, call `conn.commit()` or the change can disappear
    when the connection closes (even if it looked fine on the same connection).

Fix `connect()` (and durable writes in catalog/repository.py). Do not change tests.
"""

from __future__ import annotations

import os
import sqlite3
from pathlib import Path

DEFAULT_URL = "sqlite:///catalog.db"


def database_path_from_url(url: str) -> Path:
    """
    Convert a sqlite URL or bare path into a filesystem Path.

    Accepted examples:
      - sqlite:///relative/path.db
      - sqlite:////absolute/path.db
      - /tmp/catalog.db
      - catalog.db
    """
    raw = (url or "").strip()
    if not raw:
        raise ValueError("database url is empty")

    if raw.startswith("sqlite:////"):
        return Path("/" + raw[len("sqlite:////") :])
    if raw.startswith("sqlite:///"):
        return Path(raw[len("sqlite:///") :])
    if "://" in raw:
        raise ValueError(f"unsupported database url scheme: {raw!r}")
    return Path(raw)


def get_database_url() -> str:
    return os.environ.get("CATALOG_DATABASE_URL", DEFAULT_URL)


def connect() -> sqlite3.Connection:
    """Open a SQLite connection for the configured database."""
    url = get_database_url()
    # Starter code is wrong — fix connect() so callers get a usable DB handle.
    conn = sqlite3.connect(url)
    conn.row_factory = sqlite3.Row
    return conn


def init_schema(conn: sqlite3.Connection) -> None:
    conn.executescript(
        """
        CREATE TABLE IF NOT EXISTS items (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          item_id TEXT NOT NULL UNIQUE,
          title TEXT NOT NULL,
          kind TEXT NOT NULL,
          tag TEXT,
          note TEXT
        );
        """
    )
    conn.commit()

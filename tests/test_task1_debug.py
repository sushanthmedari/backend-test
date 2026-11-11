"""Task 1 — debug the database layer until these tests pass."""

from __future__ import annotations

from catalog.db import connect, database_path_from_url, init_schema
from catalog.repository import Item, get_item, upsert_item


def test_database_path_from_url_relative_and_absolute(tmp_path):
    relative = database_path_from_url("sqlite:///catalog.db")
    assert str(relative) == "catalog.db"

    absolute = database_path_from_url(f"sqlite:////{tmp_path / 'abs.db'}")
    assert absolute.is_absolute()
    assert absolute.name == "abs.db"


def test_connect_uses_catalog_database_url(db_path, monkeypatch):
    monkeypatch.setenv("CATALOG_DATABASE_URL", f"sqlite:///{db_path}")
    conn = connect()
    try:
        init_schema(conn)
        conn.execute(
            "INSERT INTO items (item_id, title, kind) VALUES ('a', 'A', 'text')"
        )
        conn.commit()
    finally:
        conn.close()

    conn2 = connect()
    try:
        row = conn2.execute(
            "SELECT title FROM items WHERE item_id = 'a'"
        ).fetchone()
        assert row is not None
        assert row["title"] == "A"
    finally:
        conn2.close()


def test_upsert_item_persists_across_connections(conn):
    upsert_item(
        conn,
        Item(
            item_id="item-1",
            title="First",
            kind="text",
            tag=None,
            note="hello",
        ),
    )
    # Simulate a worker exiting without an extra manual commit in the caller.
    conn.close()

    conn2 = connect()
    try:
        found = get_item(conn2, "item-1")
        assert found is not None
        assert found.title == "First"
        assert found.kind == "text"
    finally:
        conn2.close()

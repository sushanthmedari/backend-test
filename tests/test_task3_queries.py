"""Task 3 — implement small SQL helpers in catalog/queries.py.

`kind` is a column on table `items` (text per row), not a table or SQL type.
"""

from __future__ import annotations

from catalog.db import connect
from catalog.queries import clear_note, count_by_kind, list_item_ids_for_kind


def _seed(conn) -> None:
    # Seed with raw SQL + commit so this task only needs a working connect().
    conn.executescript(
        """
        DELETE FROM items;
        INSERT INTO items (item_id, title, kind, tag, note) VALUES
          ('a', 'A', 'text', NULL, 'keep'),
          ('b', 'B', 'system', 'heartbeat', 'drop-me'),
          ('c', 'C', 'system', 'manual', 'also'),
          ('d', 'D', 'text', NULL, NULL);
        """
    )
    conn.commit()


def test_count_by_kind(conn):
    _seed(conn)
    assert count_by_kind(conn) == {"system": 2, "text": 2}


def test_list_item_ids_for_kind(conn):
    _seed(conn)
    assert list_item_ids_for_kind(conn, "system") == ["b", "c"]
    assert list_item_ids_for_kind(conn, "text") == ["a", "d"]
    assert list_item_ids_for_kind(conn, "missing") == []


def test_clear_note_persists(conn):
    _seed(conn)
    clear_note(conn, "b")
    conn.close()

    conn2 = connect()
    try:
        row = conn2.execute(
            "SELECT note FROM items WHERE item_id = 'b'"
        ).fetchone()
        assert row is not None
        assert row["note"] is None

        other = conn2.execute(
            "SELECT note FROM items WHERE item_id = 'a'"
        ).fetchone()
        assert other["note"] == "keep"
    finally:
        conn2.close()

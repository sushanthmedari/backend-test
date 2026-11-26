"""Item reads/writes.

Task 1 also looks here: after changing rows, SQLite needs `conn.commit()`
for other connections (or a later reopen) to see the data.
"""

from __future__ import annotations

import sqlite3
from dataclasses import dataclass


@dataclass(frozen=True)
class Item:
    item_id: str
    title: str
    kind: str
    tag: str | None
    note: str | None


def upsert_item(conn: sqlite3.Connection, item: Item) -> None:
    conn.execute(
        """
        INSERT INTO items (item_id, title, kind, tag, note)
        VALUES (?, ?, ?, ?, ?)
        ON CONFLICT(item_id) DO UPDATE SET
          title=excluded.title,
          kind=excluded.kind,
          tag=excluded.tag,
          note=excluded.note
        """,
        (item.item_id, item.title, item.kind, item.tag, item.note),
    )


def get_item(conn: sqlite3.Connection, item_id: str) -> Item | None:
    row = conn.execute(
        "SELECT item_id, title, kind, tag, note FROM items WHERE item_id = ?",
        (item_id,),
    ).fetchone()
    if row is None:
        return None
    return Item(**dict(row))

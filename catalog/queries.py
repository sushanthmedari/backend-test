"""Simple SQL helpers (Task 3).

You do not need prior SQLite experience. SQLite here is just SQL against a local
file database, using Python's built-in `sqlite3` module (same ideas as MySQL /
Postgres SELECT/UPDATE/GROUP BY).

Schema (created in catalog/db.py → init_schema):

    TABLE items
      id       INTEGER  primary key (auto)
      item_id  TEXT     unique business id for a row
      title    TEXT
      kind     TEXT     (string label per row)
      tag      TEXT     nullable
      note     TEXT     nullable

Example rows:
  item_id='a', kind='text',   tag=NULL,        note='keep'
  item_id='b', kind='system', tag='heartbeat', note='drop-me'

So "kind" means: the value in the `kind` column of the `items` table
(e.g. 'text' or 'system').

---------------------------------------------------------------------------
How to run SQL with the `conn` you are given (copy this pattern):

    # Read many rows
    rows = conn.execute(
        "SELECT kind, COUNT(*) AS n FROM items GROUP BY kind"
    ).fetchall()
    # each row acts like a dict because connect() sets row_factory = sqlite3.Row
    value = rows[0]["kind"]
    count = rows[0]["n"]

    # Read with a bound value
    rows = conn.execute(
        "SELECT item_id FROM items WHERE kind = ? ORDER BY item_id",
        ("system",),   # second argument: values for each ? (see below)
    ).fetchall()

    # Write, then save
    conn.execute(
        "UPDATE items SET note = NULL WHERE item_id = ?",
        ("b",),        # fills the single ? with "b"
    )
    conn.commit()

`execute(...)` takes:
  1) the SQL string
  2) optional: a tuple of values that replace each `?` in order

Why `?` + a tuple instead of putting "system" into the SQL string?
  Safer and normal practice — values are bound separately from the query text.

Why `("system",)` with a trailing comma?
  In Python that is a one-element tuple. `("system")` without the comma is just
  a string in parentheses, which is the wrong type for this second argument.

  One `?`  →  one value:   ("system",)
  Two `?`  →  two values:  ("system", "heartbeat")

`fetchall()` returns all result rows from a SELECT (use after execute).
`commit()` saves INSERT/UPDATE/DELETE so other connections can see them.
---------------------------------------------------------------------------
"""

from __future__ import annotations

import sqlite3


def count_by_kind(conn: sqlite3.Connection) -> dict[str, int]:
    """
    Count rows in `items`, grouped by the `kind` column.

    Return a dict: kind value -> number of rows with that kind.
    Example: {"system": 2, "text": 2}
    Omit kinds that have zero rows.
    """
    raise NotImplementedError("Task 3: implement count_by_kind")


def list_item_ids_for_kind(conn: sqlite3.Connection, kind: str) -> list[str]:
    """
    From table `items`, return the `item_id` column for every row whose
    `kind` column equals the given kind string.

    Sort item_id ascending. Return [] if none match.
    """
    raise NotImplementedError("Task 3: implement list_item_ids_for_kind")


def clear_note(conn: sqlite3.Connection, item_id: str) -> None:
    """
    On table `items`, set the `note` column to NULL for the row with this item_id.
    Commit so another connection can see the change.
    If no such row exists, doing nothing is fine.
    """
    raise NotImplementedError("Task 3: implement clear_note")

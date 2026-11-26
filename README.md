# Python exercise

Backend interview: Python + local SQL database + policy function.

**SQLite note:** Prior SQLite experience is not required. Here it just means “SQL against a local file,” using Python’s built-in `sqlite3` module. Normal `SELECT` / `UPDATE` / `GROUP BY` knowledge transfers from MySQL or Postgres.


## Run

macOS / Linux:

```bash
./run_tests.sh
```

Windows:

```bat
run_tests.bat
```

That creates a venv, installs `requirements.txt`, and runs pytest.

At the start, unfinished tasks fail. That is expected.

Run one task’s tests:

```bash
./run_tests.sh tests/test_task1_debug.py
./run_tests.sh tests/test_task2_feature.py
./run_tests.sh tests/test_task3_queries.py
```

## Task 1 — Debug (~10 minutes)

Something is wrong in the database layer under `catalog/`.

- Fix the SQLite connection and durable writes.
- Stay on stdlib `sqlite3` (no Postgres, no ORM required).
- Do not change the tests.

Short SQLite primer is at the top of `catalog/db.py` (path vs URL, `commit`).
No prior SQLite experience expected.

Success: `tests/test_task1_debug.py` green.

## Task 2 — Policy (~5–10 minutes)

Implement `should_skip_note` in `catalog/policy.py`.

Rules are in the docstring and in `tests/test_task2_feature.py`.

Prefer a design where adding another skip tag later is a small localized change.

Does **not** depend on Task 1.

Success: `tests/test_task2_feature.py` green.

## Task 3 — Queries (~5–10 minutes)

Implement the stubs in `catalog/queries.py`. Full wording is in that file’s docstrings.

There is one table, `items`. Relevant columns:

| Column | Meaning |
| --- | --- |
| `item_id` | unique id for a row |
| `kind` | (text label on each row, e.g. `"text"` or `"system"`) |
| `tag` | optional text |
| `note` | optional text |

- `count_by_kind` — count rows grouped by the `kind` column
- `list_item_ids_for_kind` — `item_id`s where `kind` equals a given string
- `clear_note` — set `note` to NULL for one `item_id`, and commit

`catalog/queries.py` includes a short cheatsheet for `conn.execute(...)`, `.fetchall()`, and `.commit()` — use that if `sqlite3` is new.

Needs a working `connect()` from Task 1. Does not require Task 2.

Success: `tests/test_task3_queries.py` green.

## Afterward

Be ready to explain (briefly) whatever was completed:

1. Task 1: what was broken and how they confirmed the fix.
2. Task 2: how they encoded the rules and why.
3. Task 3: the SQL they chose (especially commits on writes).

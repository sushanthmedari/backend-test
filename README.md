# Python exercise

SQLite + policy exercise for backend interview.

## Run

macOS / Linux:

```bash
./run_tests.sh
```

Windows:

```bat
run_tests.bat
```

That creates a venv, installs `requirements.txt`, and runs pytest. Works the same on Windows (stdlib SQLite; no Postgres install).

Expected at start: **both tasks fail**. Make them pass.

## Task 1 — Debug (~10 minutes)

Something is wrong in the database layer under `catalog/`.

- Fix the SQLite connection and durable writes.
- Stay on stdlib `sqlite3` (no Postgres, no ORM required).
- Do not change the tests.

Success: Task 1 tests green (`./run_tests.sh tests/test_task1_debug.py` or `run_tests.bat tests/test_task1_debug.py`).

## Task 2 — Implement (~10 minutes)

Implement `should_skip_note` in `catalog/policy.py`.

Rules are in the docstring and in `tests/test_task2_feature.py`.

Prefer a design where adding another skip tag later is a small localized change.

Success: full suite green (`./run_tests.sh` or `run_tests.bat`).

## Afterward

Be ready to explain (2 minutes):

1. What was broken in Task 1 and how you confirmed the fix.
2. How you encoded the Task 2 rules and why.

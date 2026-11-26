"""Small policy helper (Task 2)."""

from __future__ import annotations


def should_skip_note(kind: str | None, tag: str | None) -> tuple[bool, str | None]:
    """
    Decide whether an item should skip getting a note.

    Rules:
    - kind == "system" and tag in {"heartbeat", "metrics"} → skip
    - everything else → do not skip

    Return (skip, reason). reason must be a non-empty string when skip is True.

    Prefer a design where adding another skip tag later is one localized change.
    """
    raise NotImplementedError("Task 2: implement should_skip_note")

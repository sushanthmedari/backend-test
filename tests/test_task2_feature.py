"""Task 2 — implement a small skip policy."""

from __future__ import annotations

from catalog.policy import should_skip_note


def test_should_skip_note_for_system_tags():
    skip, reason = should_skip_note("system", "heartbeat")
    assert skip is True
    assert reason

    skip, reason = should_skip_note("system", "metrics")
    assert skip is True
    assert reason


def test_should_not_skip_other_cases():
    skip, reason = should_skip_note("system", "manual")
    assert skip is False
    assert reason is None

    skip, reason = should_skip_note("text", "heartbeat")
    assert skip is False
    assert reason is None

    skip, reason = should_skip_note(None, None)
    assert skip is False
    assert reason is None

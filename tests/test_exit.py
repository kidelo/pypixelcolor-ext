# -*- coding: utf-8 -*-
"""Tests for the exit command prototype.

Exit / leave the current screen -> return to the saved-slot playlist.
Protocol §6: `[4, 0, 1, 1]`.
"""

from pypixelcolor.commands.exit import exit_cmd


def test_exit_command_bytes():
    """Exit must emit exactly [4, 0, 1, 1]."""
    plan = exit_cmd()
    assert plan.id == "exit"
    windows = list(plan.windows)
    assert len(windows) == 1
    assert list(windows[0].data) == [4, 0, 1, 1]

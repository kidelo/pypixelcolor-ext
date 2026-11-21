# -*- coding: utf-8 -*-
"""Deeper tests for the exit command.

Exit / leave the current screen -> return to the saved-slot playlist.
Protocol §6.1: `sendExitCmd`, bytes `[4, 0, 1, 1]`.
Format: `[len_lo, len_hi, cmd, subcmd]` (no header/CRC framing, sent via sendCompat).
"""

from pypixelcolor.commands import COMMANDS
from pypixelcolor.commands.exit import exit_cmd


def test_exit_command_bytes():
    """Exit must emit exactly [4, 0, 1, 1]."""
    plan = exit_cmd()
    assert plan.id == "exit"
    windows = list(plan.windows)
    assert len(windows) == 1
    assert list(windows[0].data) == [4, 0, 1, 1]


def test_exit_is_registered_in_commands():
    """`exit` must be a registered command in the COMMANDS dict."""
    assert "exit" in COMMANDS
    assert COMMANDS["exit"] is exit_cmd


def test_exit_byte_layout():
    """Verify the byte layout semantics: [len_lo, len_hi, cmd, subcmd]."""
    data = bytes(exit_cmd().windows[0].data)
    assert len(data) == 4
    assert data[0] == 4        # length (4 bytes total)
    assert data[1] == 0        # len_hi (length < 256, so 0)
    assert data[2] == 1        # command ID 0x0001 = exit/leave
    assert data[3] == 1        # subcommand 1


def test_exit_bytes_are_immutable():
    """The plan data should be a frozen bytes object."""
    data = exit_cmd().windows[0].data
    assert isinstance(data, bytes)
    assert data == b"\x04\x00\x01\x01"


def test_exit_matches_protocol_catalog():
    """Exit bytes must match the protocol §6.1 catalog exactly."""
    # Protocol §6.1: | Exit / leave | `[4,0,1,1]` | sendExitCmd |
    expected = [4, 0, 1, 1]
    assert list(exit_cmd().windows[0].data) == expected

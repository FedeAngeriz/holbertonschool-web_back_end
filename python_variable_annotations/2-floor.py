#!/usr/bin/env python3
"""Add float n and return floor of the float."""


def floor(n: float) -> int:
    """Return the floor of a number."""
    return int(n) if n > 0 else int(n) - 1

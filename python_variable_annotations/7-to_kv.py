#!/usr/bin/env python3
"""Function defining a tuple with a string and the square of a float."""


def to_kv(k: str, v: float) -> tuple:
    """Returns a tuple with the first element being the string k and the second element being the square of v."""
    return (k, v ** 2)

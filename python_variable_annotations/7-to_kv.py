#!/usr/bin/env python3
"""Function defining a tuple with a string and the square of a float."""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Returns a tuple with the first element being the string k and the second element being the square of v."""
    return (k, float(v ** 2))

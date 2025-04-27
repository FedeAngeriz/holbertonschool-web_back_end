#!/usr/bin/env python3
"""Function defining a tuple with a string and the square of a float."""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Returns a tuple with the k string and the v float."""
    return (k, float(v ** 2))

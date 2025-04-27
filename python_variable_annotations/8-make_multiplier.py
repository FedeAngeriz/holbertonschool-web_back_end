#!/usr/bin/env python3
"""Create a function that multiplies a float by a given multiplier."""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    
    def multiply(number: float) -> float:
        """Multiply the input number by the multiplier."""
        return number * multiplier

    return multiply

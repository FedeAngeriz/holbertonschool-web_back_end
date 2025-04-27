#!/usr/bin/env python3
"""Create a function that multiplies a float by a given multiplier."""


def make_multiplier(multiplier: float) -> callable:
    
    def multiply(number: float) -> float:
        """Multiply the input number by the multiplier."""
        return number * multiplier

    return multiply

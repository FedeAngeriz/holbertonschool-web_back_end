#!/usr/bin/env python3
def make_multiplier(multiplier: float) -> callable:
    """Create a function that multiplies a number by a given multiplier.

    Args:
        multiplier (float): The multiplier to use.

    Returns:
        callable: A function that takes a number and returns the product.
    """
    def multiply(number: float) -> float:
        """Multiply the input number by the multiplier."""
        return number * multiplier

    return multiply

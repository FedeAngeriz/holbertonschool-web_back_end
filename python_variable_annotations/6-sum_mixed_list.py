#!/usr/bin/env python3
"""Function sum a list of floats and integers, return their sum as a float."""
from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """Returns the sum of a list of floats and integers."""
    return sum(mxd_list)

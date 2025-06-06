#!/usr/bin/env python3
"""Async comprehension that yields 10 random numbers"""
from typing import List
import random
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Async comprehension that yields 10 random numbers"""
    result = [i async for i in async_generator()]
    return result

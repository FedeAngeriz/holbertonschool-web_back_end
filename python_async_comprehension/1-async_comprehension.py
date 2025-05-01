#!/usr/bin/env python3
from typing import async_generator


async def async_comprehension():
    """Async comprehension that yields 10 random numbers"""
    result = [i async for i in async_generator()]
    return result

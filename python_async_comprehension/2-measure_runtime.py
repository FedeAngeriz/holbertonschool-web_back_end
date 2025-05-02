#!/usr/bin/env python3
"""Measure the total runtime of 4 parallel comprehensions"""
from typing import List
import random
async_comprehension = __import__('1-async_comprehension').async_comprehension
import time
import asyncio


async def measure_runtime() -> float:
    """Measure the total runtime of 4 parallel comprehensions"""
    start_time = time.time()
    await asyncio.gather(async_comprehension(), 
                         async_comprehension(),
                         async_comprehension(), 
                         async_comprehension()
                        )
    end = time.time()
    total_time = end - start_time
    return total_time

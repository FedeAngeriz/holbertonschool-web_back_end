#!/usr/bin/env python3
import asyncio
from 0-basic_async_syntax import wait_random
"""Import wait_random from 0-basic_async_syntax.py and run it in a loop"""

async def wait_n(n: int, max_delay: int) -> list[float]:
    """wait_n that takes in 2 int arguments (n, max_delay) and returns a list of all the delays (float values)"""
    
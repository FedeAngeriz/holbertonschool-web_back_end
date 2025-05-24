#!/usr/bin/env python3
""" Import wait_random from 0-basic_async_syntax.py and run it in a loop """
import asyncio
from typing import List
import importlib
wait_random = importlib.import_module("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> list[float]:
    """ should return the list of all the delays """
    delay = []
    for i in range(n):
        delay.append(wait_random(max_delay))

    return delay
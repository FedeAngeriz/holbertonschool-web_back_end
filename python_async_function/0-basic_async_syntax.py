#!/usr/bin/env python3
""" Function async argument wait 10 seconds the returns it """
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """ Function async argument wait 10 seconds the returns it """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay

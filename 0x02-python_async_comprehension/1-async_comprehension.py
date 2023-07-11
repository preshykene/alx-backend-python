#!/usr/bin/env python3

"""
Task one
"""
import asyncio
from typing import List
from importlib import import_module as find


async_generator = find('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    The coroutine will collect 10 random numbers using an async comprehensing
    """
    random_numbers = [num async for num in async_generator()]
    return random_numbers[:10]

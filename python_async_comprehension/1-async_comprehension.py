#!/usr/bin/env python3
"""Module for the function async_comprehension"""
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Collects 10 random numbers using an async comprehensing
    over async_generator and return the 10 random numbers"""
    randoms = [i async for i in async_generator()]
    return randoms

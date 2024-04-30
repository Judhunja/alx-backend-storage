#!/usr/bin/env python3
"""This module contains a class Cache"""

import redis
from typing import Union
from uuid import uuid4


class Cache:
    """Implements a class Cache"""

    def __init__(self) -> None:
        """Initializes class Cache"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """generates a random key and stores the input data using the key and
        return the key"""
        key = uuid4()
        key = str(key)
        self._redis.set(key, data)
        return key

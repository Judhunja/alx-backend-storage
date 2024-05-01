#!/usr/bin/env python3
"""This module contains a class Cache"""

import redis
from typing import Union, Callable
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

    def get(self, key: str, fn: Callable[Union[str, bytes, int, float], Union[str, bytes, int, float]] = None) -> Union[str, bytes, int, float]:
        """Returns data belonging to a key in the desired format or None if the data doesn't exist"""
        data = self._redis.get(key)

        try:
            return fn(data)
        except Exception:
            return data

    def get_str(self, key: str):
        """Parametrizes get for strings"""
        return self.get(key, lambda d: d.decode('utf-8'))

    def get_int(self, key: str):
        """Parametrizes get for ints"""
        return self.get(key, int(key))

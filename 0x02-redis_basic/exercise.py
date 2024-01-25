#!/usr/bin/env python3
"""This module contains a class Cache."""
import redis
import uuid
from typing import Union


class Cache:
    """Implement a class Cache."""

    def __init__(self):
        """Set private instance variable _redis."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Generate a random key and stores input data in
        Redis using random key and returns the key.
        """
        key: str = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

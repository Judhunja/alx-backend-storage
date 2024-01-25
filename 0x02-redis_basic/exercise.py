#!/usr/bin/env python3
"""This module contains a class Cache."""
import redis
import uuid
from typing import Union, Callable


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

    def get(self, key: str, fn: Callable[[Union[str, bytes, int, float]], Union[str, bytes, float, int]] = None) -> Union[str, int, bytes, float]:
        """
        Take key as str and optional callable to
        convert the key to a specific data type.
        """
        data = self._redis.get(key)
        try:
            return fn(data)
        except Exception:
            return data

    def get_str(self, key: str):
        """Return the value as a string."""
        return self.get(key, lambda y: y.decode("utf-8"))

    def get_int(self, key: str):
        """Return the value as int."""
        return self.get(key, int)


cache = Cache()

TEST_CASES = {
    b"foo": None,
    123: int,
    "bar": lambda d: d.decode("utf-8")
}

for value, fn in TEST_CASES.items():
    key = cache.store(value)
    assert cache.get(key, fn=fn) == value

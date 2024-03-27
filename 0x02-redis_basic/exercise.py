#!/usr/bin/env python3
"""redis basic"""
import redis
import uuid
from typing import Union

types = Union[str, float, int, bytes]


class Cache:
    """Cache Class"""

    def __init__(self) -> None:
        """init method"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: types) -> str:
        """
        generate a random key using uuid, store the input data in Redis
        using the random key and return the key
        """
        key = str(uuid.uuid4())
        self._redis.mset({key: data})
        return key

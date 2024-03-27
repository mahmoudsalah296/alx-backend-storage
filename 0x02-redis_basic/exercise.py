#!/usr/bin/env python3
"""redis basic"""
import redis
import uuid
from typing import Union

types = Union[str, float, int, bytes]


class Cache:
    """
    Cache redis class
    """

    def __init__(self):
        """
        constructor of the redis model
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: types) -> str:
        """
        generate a random key (e.g. using uuid),
        store the input data in Redis using the
        random key and return the key.
        :param data:
        :return:
        """
        key = str(uuid.uuid4())
        self._redis.mset({key: data})
        return key

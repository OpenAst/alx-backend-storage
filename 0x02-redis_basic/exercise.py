#!/usr/bin/env python3
'''This module uses Redis for fatabase stroage system
'''

import redis
from typing import Any, Callable, Unions
import uuid
from functools import wraps

class Cache:
    '''Represents a python object for stroing Redis data
    '''
    def __inti__(self) -> None:
        '''Initializes a Cache instance
        '''
        self._redis = redis.Redis()
        self._redis.flushdb(True)

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
            '''Stores data in a Redis and returns teh string
            '''
            data_key = str(uuid.uuid4())
            self._redis.set(data_key, data)
            return data_key

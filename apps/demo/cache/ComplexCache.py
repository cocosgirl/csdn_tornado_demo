#!/usr/bin/env python
# -*- coding: utf-8 -*-
from databases.dbfactory.dbfactory import dbfactory
import json


class ComplexCache(object):
    def __init__(self, *args, **kwargs):
        self.key = kwargs.get("key")
        self.conf_name = kwargs.get("conf_name")
        self.ttl_time = kwargs.get("ttl_time", 0)
        self.redis_conn = dbfactory.create_db(conf_name=self.conf_name, db_type="db_redis")

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            cache_result = self.pull_cache(key=self.key)

            if cache_result:
                return json.loads(str(cache_result[0], encoding="utf-8"))
            else:
                result = func(*args, **kwargs)
                self.push_cache(key=self.key, result=json.dumps(result))
                return result
        return wrapper

    # 添加缓存
    def push_cache(self, key, result):
        self.redis_conn.lpush(key, result)
        if self.ttl_time:
            self.redis_conn.expire(key, self.ttl_time)

    # 获取缓存
    def pull_cache(self, key):
        return self.redis_conn.lrange(key, 0, 0)


class ClearCache(object):
    def __init__(self, *args, **kwargs):
        self.key = kwargs.get("key")
        self.conf_name = kwargs.get("conf_name")
        self.redis_conn = dbfactory.create_db(conf_name=self.conf_name, db_type="db_redis")

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            self.clear_cache(key=self.key)
            return result
        return wrapper

    # 清空缓存
    def clear_cache(self, key):
        return self.redis_conn.delete(key)

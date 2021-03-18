#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-1-13 上午11:28
# @Author  : 
# @Desc    : dao 缓存装饰器

from databases.dbfactory.dbfactory import dbfactory
import json


class Scache(object):
    def __init__(self, *args, **kwargs):
        self.conf_name = kwargs.get("conf_name")  # 缓存地址
        self.name = kwargs.get("name")            # 缓存key
        self.update = kwargs.get("update", [])    # 更新数据清空缓存
        self.time = kwargs.get("time")            # 缓存失效时间

    def __call__(self, func):
        """
        :param func:
        :return:
        """
        # 线下查询mysql和redis相比较   在mysql新增图片的时候很有用
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            result_set = set(result)
            cache_name = kwargs.get(self.name)
            cache_result = self.pull_cache(name=cache_name)    # 查询缓存
            for i in cache_result:
                cache_result.remove(i)
                i = i.decode()
                cache_result.add(i)
            diff = result_set.difference(cache_result)         # 计算差集
            print(diff)
            if cache_result and not diff:
                return list(cache_result)
            else:
                # result = func(*args, **kwargs)
                if result:
                    self.push_cache(name=cache_name, value=diff)  # 添加缓存
                return result
        return wrapper

        # 线上只取redis里面的数据
        # def wrapper(*args, **kwargs):
        #
        #     cache_name = kwargs.get(self.name)
        #     cache_result = self.pull_cache(name=cache_name)    # 查询缓存
        #     if cache_result:
        #         for i in cache_result:
        #             cache_result.remove(i)
        #             i = i.decode()
        #             cache_result.add(i)
        #         print("目前redis里面有", len(cache_result), "张黑名单图片")
        #         return list(cache_result)
        #     else:
        #         result = func(*args, **kwargs)
        #         if result:
        #             self.push_cache(name=cache_name, value=result)  # 添加缓存
        #         return result
        # return wrapper

    def push_cache(self, name, value):
        """
        :param name:
        :param key:
        :param value:
        :desc 添加缓存
        :return:
        """
        try:
            redis_search = dbfactory.db_redis(conf_name=self.conf_name, db_type="db_redis")
            # print(name, redis_search)
            for v in value:
                print(v, type(v))
                redis_search.sadd(name, v)

            if redis_search.ttl(name=name) < 0 and self.time:
                redis_search.expire(name=name, time=self.time)

        except Exception as e:
            return None

    def pull_cache(self, name):
        """
        :param name:
        :param key:
        :desc 获取缓存
        :return:
        """
        try:
            redis_search = dbfactory.db_redis(conf_name=self.conf_name, db_type="db_redis")
            return redis_search.smembers(name=name)
        except Exception as e:
            return None

    def del_cache(self, name, keys):
        """
        :param name:
        :param keys:
        :param 删除缓存
        :return:
        """
        try:
            redis_search = dbfactory.db_redis(conf_name=self.conf_name, db_type="db_redis")
            return redis_search.hdel(name, keys)
        except Exception as e:
            return None


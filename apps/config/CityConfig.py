# -*- coding: utf-8 -*-
import requests
import json

def city_list(city_lists=[]):
    def decorator(origin_func):
        def wrapper(*args, **kwargs):
            try:
                for i in city_lists:
                    kwargs["city"] = i
                    origin_func(*args, **kwargs)
            except Exception as e:
                print(e)
        return wrapper
    return decorator


def generate_city_list(city_lists=[]):
    def decorator(origin_func):
        def wrapper(*args, **kwargs):
            try:
                for i in city_lists:
                    kwargs["city"] = i
                    yield origin_func(*args, **kwargs)
            except Exception as e:
                print(e)
        return wrapper
    return decorator


class CityConfig(object):
    @staticmethod
    def get_city(**kwargs):
        return CityApi(**kwargs)

    @staticmethod
    def get_city_interval(**kwargs):
        return CityInterval(**kwargs)

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    : CitySouceMapping.py
# @Software: PyCharm

city_mapping = {
    'bj': {
        'id': '1',
        'fpy': 'beijing'
    },
    'sh': {
        'id': '2',
        'fpy': 'shanghai'
    },
    'sz': {
        'id': '3',
        'fpy': 'shenzhen'
    },
    'wh': {
        'id': '4',
        'fpy': 'wuhan'
    },
}


def get_db(type, city):
    not_bj = {
              "sell": "spider", "new_sell": "spider",
              }
    bj = {"complex": "demo", }
    mag = {"brokers": "brokers", }
    if type in bj:
        db = bj.get(type) + "_" + city
        return db
    elif type in not_bj:
        db = not_bj.get(type) if city == "bj" else not_bj.get(type) + "_" + city
        return db
    elif type in mag:
        return mag.get(type)


sell_old = ['bj', ]

sell_new = ['fs', 'jx']


def getConfigName(city, type):
    if "sell" == type:
        if city in sell_old:
            return "sell"
        else:
            return "new_sell"
    elif "plathouse" == type:
        if city in sell_old:
            return "plathouse"
        else:
            return "new_plathouse"
    elif "plathouse" == type:
        if city in sell_old:
            return "plathouse"
        else:
            return "new_plathouse"
    return type

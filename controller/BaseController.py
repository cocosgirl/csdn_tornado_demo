#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Desc    :

import tornado.ioloop
import time
import tornado.web
from utils.BaseUtils import BaseUtils
import json


class BaseController(tornado.web.RequestHandler):

    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')


def catch_exception(origin_func):

    def wrapper(*args, **kwargs):
        try:
            st = time.time()
            u = origin_func(*args, **kwargs)
            et = time.time() - st
            return u
        except Exception as e:
            print(e)
    return wrapper


def catch(*dargs, **dkwargs):
    """
    # @Desc    : 异常处理装饰器
    """
    def wrapper(func):
        def _wrapper(*args, **kargs):
            request = args[0]
            try:
                st = time.time()
                result = {"message": "success", "code": 200}
                fun = func(*args, **kargs)
                et = time.time() - st
                result["time"] = et
                result["page"] = fun.get("page", {})
                result["data"] = fun.get("data", [])
                if fun.get("total") or 0:
                    result["total"] = fun.get("total", 0)
                result["code"] = fun.get("code", 200)
                if fun.get("message"):
                    result["message"] = fun.get("message")
                request.write(json.dumps(result))
            except Exception as e:
                result = {"message": str(e), "code": 500}
                request.write(json.dumps(result))
        return _wrapper
    return wrapper


def encrypt(*dargs, **dkwargs):
    """
    加密装饰器
    :param dargs:
    :param dkwargs:
    :return:
    """
    def wrapper(func):
        def _wrapper(*args, **kargs):
            signatures = {"JD": 'acb34c2b9da033dd38e946d313449068'}
            request = args[0]
            user = request.get_argument("user")
            signature = request.get_argument("signature")
            key = signatures.get(user)
            pms = dkwargs.get('pms', [])
            pm = [f"{key}={request.get_argument(key)}" for key in pms]
            pm = "&".join(pm) + key
            my_signature = BaseUtils.getMd5(pm)
            print(my_signature)
            if my_signature == signature:
                fun = func(*args, **kargs)
                return fun
            else:
                result = {
                    "message": "您的Token无效,请联系demo找房,多次尝试会被记录黑名单,谢谢配合！！！",
                    "code": 200,
                    "data": []}
                request.write(json.dumps(result))
        return _wrapper
    return wrapper


class Route(object):
    """ 把每个URL与Handler的关系保存到一个元组中，然后追加到列表内，列表内包含了所有的Handler """

    def __init__(self):
        self.urls = list()  # 路由列表

    def __call__(self, url, *args, **kwargs):
        def register(cls):
            self.urls.append((url, cls))  # 把路由的对应关系表添加到路由列表中
            return cls

        return register




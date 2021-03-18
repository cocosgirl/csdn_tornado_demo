#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Desc    :
from controller.BaseController import Route
route = Route()
from controller.BaseController import BaseController

@route("/hello")
class Hello(BaseController):
    """
    desc： [对外接口] 根据价格区间查询同城区 ，同商圈下的楼盘
    @:param city:城市
    @:param cityarea_id [必传字段]
    @:param cityarea2_id [可选字段]
    @:param filter :{"cityarea_id":1, "cityarea2_id":3, "price":"200"}
    annotation：依旧按search_api
    """

    def get(self, *args, **kwargs):
        result = {"message": "success", "code": 200}
        result["data"] = '欢迎使用后台管理api接口业务！！！'
        self.write(result)

@route('/.*')
class ErrorHandel(BaseController):
    def get(self, *args, **kwargs):
        try:
            self.write({"message": "请求资源路径不存在！！！", "code": 400})
        except Exception as e:
            print(e)

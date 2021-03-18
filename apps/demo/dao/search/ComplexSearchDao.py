#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-3-5 下午2:30
# @Author  : 
# @Desc    :
from dao.BaseDao.BaseEs import BaseES
from apps.demo.model.search.ComplexSearchMapping import ComplexSearchMapping
class ComplexSearchDao(BaseES):
    def __init__(self, *args, **kwargs):
        super().__init__(conf_name=kwargs.get("conf_name", "sell"), model=kwargs.get("model", ComplexSearchMapping))



#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-10-10 下午2:36
# @Author  : 
# @desc   :  业务ES业务访问层
from service.BaseService.BaseEsService import BaseEsService
from apps.demo.service.search.ComplexSearchDSL import ComplexSearchDSL
from apps.demo.dao.search.ComplexSearchDao import ComplexSearchDao
class ComplexSearchService(BaseEsService):
    def __init__(self):
        self.dsl = ComplexSearchDSL()
        self.online_keyword_alias = 'online_keyword'
        super(ComplexSearchService, self).__init__(dao=ComplexSearchDao())


    def get_alias_es(self,alias):
        return self.alias_es(alias_name=alias)
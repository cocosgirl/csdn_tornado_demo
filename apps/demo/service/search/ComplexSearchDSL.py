#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-10-10 下午8:29
# @Author  : 
# @Desc    :
import json
import datetime
from service.BaseService.BaseSearchDSL import BaseSearchDSL
class ComplexSearchDSL(BaseSearchDSL):
    pass
    # def get_search_dsl(self, *args, **kwargs):
    #     # @Time    : 17-10-10 下午8:29
    #     # @Author  : 
    #     # @Desc    : 根据参数 转换成dsl条件
    #
    #     """
    #     :param cityarea_id [等值查询] 城区
    #     :param room->house_room [等值查询] 室
    #
    #     :param subwayline->lid [模糊查询] 地铁线id
    #     :param subway->sid [模糊查询] 地铁站id
    #     :param source->company_id [模糊查询]  经纪公司id
    #     :param cityarea2_id->cityarea2_id [模糊查询]  商圈id
    #     :param guolv->not-tag  [模糊查询] 过滤标签
    #
    #     :param price->min_price [范围查询]  价格
    #
    #     :param args:
    #     :param kwargs:
    #     :return:
    #     """
    #     pms = kwargs.get("pms", {})
    #
    #     filter = pms.get("filter", {})
    #
    #     # 等值查询字段列表
    #     equal = ['borough_id', 'building_number', 'building_unit', 'house_number', 'cityarea_id', 'cityarea2_id',
    #              'house_toward', 'company_id', 'house_source', 'house_status',
    #              'is_open',  'house_fitment', 'tag', 'property_type']
    #     # 模糊查询字段列表
    #     like = ['borough_name', 'borough_address', 'house_id']
    #     # 范围查询字段列表
    #     region = ['house_price', 'house_room', 'house_area', 'ctime', 'house_floor']
    #     should = ['record_id', 'surveyor_id', 'client_id', 'maintenance_id', 'keyor_id']
    #
    #     bool_must = []
    #     # 判断实勘、钥匙
    #     if filter.get("key", {}):
    #         if filter.get("key", {}).get('content') == "1":
    #             bool_must += [{"bool": {"must_not": [{"term":{"keyor_id":0}}]}}]
    #         else:
    #             bool_must += [{"bool": {"must": [{"term": {"keyor_id": 0}}]}}]
    #     if filter.get("survey", {}):
    #         if filter.get("survey", {}).get('content') == "1":
    #             bool_must += [{"bool": {"must_not": [{"term": {"surveyor_id": 0}}]}}]
    #         else:
    #             bool_must += [{"bool": {"must": [{"term": {"surveyor_id": 0}}]}}]
    #
    #     #判断顶层
    #     if filter.get("dingceng", {}).get('content') == "1":
    #         bool_must += [{"script": {"script": {"inline": "doc['house_floor'].value - doc['house_topfloor'].value == 0","lang": "painless"}}}]
    #
    #     # 拼或者查询
    #     role_type = filter.get('role_type', {})
    #     role_id = filter.get('role_id', {})
    #     if role_type:
    #         value = role_id.get('content').split(",")
    #         bool_must += [{"bool": {"should": [{"term": {role_type.get('content'): v}} for v in value ]}}]
    #     elif not role_type and role_id:
    #         value = role_id.get('content').split(",")
    #         bool_must += [{"bool": {"should": [{"term": {i: v}} for v in value for i in should]}}]
    #
    #     for key, value in filter.items():
    #         key = key.strip()
    #         if not value or not value.get("content"):
    #             continue
    #         value = value.get("content", "").strip(" ").strip(",").split(",")
    #         # 拼数等值查询
    #         if (key in equal) or (key[4:] in equal):
    #             if not key.startswith("not-"):
    #                 bool_must += [{"term": {key: v}} for v in value]
    #             else:
    #                 bool_must += [{"bool": {"must_not": [{"term": {key[4:]: v}} for v in value]}}]
    #
    #         # 拼数值范围
    #         if (key in region) or (key[4:] in region):
    #             if not key.startswith("not-"):
    #                 bool_must += [{"range": {key: {"gte": str(v).split("-")[0].replace('f','-'), "lte":str(v).split("-")[1].replace('f','-')}}} for v in value]
    #             else:
    #                 bool_must += [{"bool": {"must_not": [{"range": {key[4:]: {"gte": str(v).split("-")[0].replace('f','-'), "lte": str(v).split("-")[1].replace('f','-')}}} for v in value]}}]
    #
    #         # 拼装关键词搜索
    #         if key in like:
    #             bool_must += [{"bool": {"should": [{"wildcard": {key: "*" + str(v) + "*"}} for v in value]}}]
    #
    #     #==============排序方式================
    #     sort = pms.get("sort", [])
    #     sort = [{s.get("field"): {"order": s.get("type")}} for s in sort if s.get("field")] if sort else [{"cnt": {"order":"desc"}}]
    #     # ==============排序方式================
    #
    #     #===============限制size最大30=============
    #     if pms.get("size") > 30:
    #         pms["size"] = 30
    #
    #     query = {"query": {"bool": {"must": bool_must}}, "from": pms.get("from", 0), "size": pms.get("size", 10), "sort": sort, "aggs": {}}
    #
    #     return json.dumps(query)


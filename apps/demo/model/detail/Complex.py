# -*- coding: utf-8 -*-

"""
@author lucas
@email lutaixiang@demofang.com
@desc 二手GOV表实体类
@class_name HouseSellGov
"""
from model.BaseModel.Base import Base
from decimal import Decimal

class Complex(Base):
    __tablename__ = 'complex'
    fields = {
        'id': 0,
        'complex_pinyin': '',
        'city_id': 0,
        'complex_id': 0,
        'utime': 0,
        'base_id': 0,
        'subway_info': '',
        'complex_name': '',
        'complex_alias': '',
        'complex_address': '',
        'source_id': '',
        'source_url': '',
        'cityarea2_name': '',
        'cityarea_name': '',
        'cityarea2_id': '',
        'cityarea_id': 0,
        'complex_tag': '',
        'complex_building_type': '',
        'complex_loopline': 0,
        'developer_name': '',
        'hot_line': '',
        'developer_offer_expiry': '',
        'developer_offer': '',
        'sale_status': '',
        'preferential_status': '',
        'property_company': '',
        'property_type': '',
        'property_costs': '',
        'hydropower_gas': '',
        'heating_mode': '',
        'greening_rate': '',
        'parking_rate': '',
        'parking_count': '',
        'volume_rate': '',
        'renovation': '',
        'first_saletime': 0,
        'first_delivertime': '',
        'license': '',
        'lng': Decimal(1),
        'lat': Decimal(1),
        'priority': '',
        'property_year': '',
        'take_land_time': '',
        'ctime': 0,
        'sortweight': 0,
        'first_logic_saletime': 0,
        'merge_total': 0,
        'firstnew_saletime': 0,
        'complex_desc': '',
        'cityarea_pinyin': '',
        'cityarea2_pinyin': '',
        'sale_weight': 0,
        'sale_phone': '',
        'status': 0,
        'human_modified': '',
        'architectural': '',
        'salesoffice_address': '',
        'building_totalarea': '',
        'building_area': '',
        'building_total': '',
        'house_total': '',
        'property_desc': '',
        'floor_desc': '',
        'property_id': 0,
        'developer_id': 0,
        'location_type': 0,
        'developer_price': 0,
        'checked': 0,
        'developer_price_unit': '',
        'around_average_price': '',
    }
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-3-5 下午2:30
# @Author  : 
# @Desc    :
from model.BaseModel.Base import Base
class ComplexSearchMapping(Base):
    __tablename__ = ''
    fields = {
        "properties": {
            "id": {
                "type": "long"
            },
            "ctime": {
                "type": "long"
            },
            "utime": {
                "type": "long"
            },
            "base_id": {
                "type": "long"
            },
            "complex_name": {
                "index": "not_analyzed",
                "type": "string"
            },
            "alias_list": {
                "type": "nested",
                "properties": {
                    "complex_alias": {
                        "index": "not_analyzed",
                        "type": "string"
                    }
                }
            },
            "complex_address": {
                "index": "not_analyzed",
                "type": "string"
            },
            "source_list": {
                "type": "nested",
                "properties": {
                    "source_id": {
                        "type": "long"
                    },
                    "source_url": {
                        "index": "not_analyzed",
                        "type": "string"
                    }
                }
            },
            "merge_total": {
                "type": "long"
            },
            "sortweight": {
                "type": "long"
            },
            "sale_weight": {
                "type": "long"
            },
            "first_logic_saletime": {
                "type": "long"
            },
            "cityarea_id": {
                "type": "long"
            },
            "cityarea_py": {
                "index": "not_analyzed",
                "type": "string"
            },
            "cityarea2": {
                "type": "nested",
                "properties": {
                    "cityarea2_id": {
                        "type": "long"
                    },
                    "cityarea2_name": {
                        "index": "not_analyzed",
                        "type": "string"
                    },
                    "cityarea2_py": {
                        "index": "not_analyzed",
                        "type": "string"
                    },
                }
            },
            "complex_tag": {
                "index": "not_analyzed",
                "type": "string"
            },
            "building_type_list": {
                "type": "nested",
                "properties": {
                    "complex_building_type": {
                        "type": "long"
                    }
                }
            },
            "complex_loopline": {
                "type": "long"
            },
            "developer_name": {
                "index": "not_analyzed",
                "type": "string"
            },
            "developer_offer": {
                "index": "not_analyzed",
                "type": "string"
            },
            "developer_offer_expiry": {
                "index": "not_analyzed",
                "type": "string"
            },
            "sale_status": {
                "index": "not_analyzed",
                "type": "string"
            },
            "preferential_status": {
                "index": "not_analyzed",
                "type": "string"
            },
            "property_company": {
                "index": "not_analyzed",
                "type": "string"
            },
            "property_type": {
                "index": "not_analyzed",
                "type": "string"
            },
            "property_costs": {
                "index": "not_analyzed",
                "type": "string"
            },
            "hydropower_gas": {
                "index": "not_analyzed",
                "type": "string"
            },
            "heating_mode": {
                "index": "not_analyzed",
                "type": "string"
            },
            "greening_rate": {
                "index": "not_analyzed",
                "type": "string"
            },
            "parking_rate": {
                "index": "not_analyzed",
                "type": "string"
            },
            "parking_count": {
                "index": "not_analyzed",
                "type": "string"
            },
            "property_year": {
                "index": "not_analyzed",
                "type": "string"
            },
            "volume_rate": {
                "index": "not_analyzed",
                "type": "string"
            },
            "renovation": {
                "index": "not_analyzed",
                "type": "string"
            },
            "first_saletime": {
                "type": "long",
            },
            "firstnew_saletime": {
                "type": "long",
            },
            "first_delivertime": {
                "index": "not_analyzed",
                "type": "string"
            },
            "license_list": {
                "type": "nested",
                "properties": {
                    "license": {
                        "index": "not_analyzed",
                        "type": "string"
                    }
                }
            },
            "pos": {
                "type": "geo_point",
            },
            "full_text": {
                "index": "not_analyzed",
                "type": "string"
            },
            "house_subway": {
                "type": "nested",
                "properties": {
                    "station_name": {
                        "index": "not_analyzed",
                        "type": "string"
                    },
                    "lid": {
                        "type": "long"
                    },
                    "line_name": {
                        "index": "not_analyzed",
                        "type": "string"
                    },
                    "sid": {
                        "type": "long"
                    }
                }
            },
            "house_gov": {
                "type": "nested",
                "properties": {
                    "complex_id": {
                        "type": "long"
                    },
                    "hot_line": {
                        "index": "not_analyzed",
                        "type": "string"
                    },
                    "developer_offer": {
                        "index": "not_analyzed",
                        "type": "string"
                    },
                    "developer_offer_expiry": {
                        "index": "not_analyzed",
                        "type": "string"
                    },
                    "sale_status": {
                        "index": "not_analyzed",
                        "type": "string"
                    },
                    "preferential": {
                        "index": "not_analyzed",
                        "type": "string"
                    },
                    "source_id": {
                        "type": "long"
                    },
                    "source_url": {
                        "index": "not_analyzed",
                        "type": "string"
                    },
                    "complex_desc": {
                        "index": "not_analyzed",
                        "type": "string"
                    },
                    "firstnew_saletime": {
                        "type": "long"
                    },
                    "first_saletime": {
                        "type": "long"
                    },
                }
            },
            "house_license": {
                "type": "nested",
                "properties": {
                    "id": {
                        "type": "long"
                    },
                    "complex_id": {
                        "type": "long"
                    },
                    "source_id": {
                        "type": "long"
                    },
                    "pubtime": {
                        "index": "not_analyzed",
                        "type": "string"
                    },
                    "building_info": {
                        "index": "not_analyzed",
                        "type": "string"
                    },
                    "license": {
                        "index": "not_analyzed",
                        "type": "string"
                    }
                }
            },
            "house_type": {
                "type": "nested",
                "properties": {
                    "complex_id": {
                        "type": "long"
                    },
                    "source_id": {
                        "type": "long"
                    },
                    "source_url": {
                        "index": "not_analyzed",
                        "type": "string"
                    },
                    "housetype_tag": {
                        "index": "not_analyzed",
                        "type": "string"
                    },
                    "house_room": {
                        "type": "long"
                    },
                    "house_hall": {
                        "type": "long"
                    },
                    "house_toilet": {
                        "type": "long"
                    },
                    "house_kitchen": {
                        "type": "long"
                    },
                    "housetype_toward": {
                        "type": "long"
                    },
                    "house_totalarea": {
                        "type": "double"
                    },
                    "house_topfloor": {
                        "index": "not_analyzed",
                        "type": "string"
                    },
                    "housetype_saletype": {
                        "index": "not_analyzed",
                        "type": "string"
                    },
                    "house_layout": {
                        "index": "not_analyzed",
                        "type": "string"
                    },
                    "reference_totalprice": {
                        "type": "long"
                    },
                    "reference_price": {
                        "type": "long"
                    },
                    "reference_down_payment": {
                        "index": "not_analyzed",
                        "type": "string"
                    },
                    "reference_month_payment": {
                        "index": "not_analyzed",
                        "type": "string"
                    },
                    "sortweight": {
                        "type": "long"
                    },
                }
            }
        }
    }
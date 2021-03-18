# -*- coding: utf-8 -*-
from dao.BaseDao.BaseMysql import BaseMysql
from apps.demo.model.detail.Complex import Complex
from cache.LocalCache import LocalCache


class ComplexDao(BaseMysql):
    def __init__(self, *args, **kwargs):
        self.model=Complex()
        super().__init__(conf_name=kwargs.get("conf_name", "complex"),
                         model=kwargs.get("model", self.model))

    def get_complex_id(self, city, complex_name):
        sql = f"SELECT complex_id FROM {self.table} WHERE complex_name='%s'" % (complex_name)
        data = self.exe_s_sql(city=city, sql={'sql': sql})
        return data
        
    @LocalCache(conf_name='complex_api', key="cache_key",time=86400)
    def get_id(self, *args, **kwargs):
        return self.select_by_filter(self, *args, **kwargs)

    def get_around_price(self, *args, **kwargs):
        return self.select_by_filter(self, *args, **kwargs)

from decimal import Decimal
if __name__ == '__main__':
    v= Decimal('0E-10')

    print(type(v))

from service.BaseService.BaseMysqlService import BaseMysqlService
from apps.demo.service.detail.ComplexMergeService import ComplexMergeService
from apps.demo.service.detail.ComplexGovService import ComplexGovService
from apps.demo.service.detail.ComplexCommentService import ComplexCommentService
from apps.demo.service.detail.ComplexHousetypeService import ComplexHousetypeService
from apps.demo.service.detail.ComplexLicenseService import ComplexLicenseService
from apps.demo.service.detail.ComplexInformationService import ComplexInformationService
from apps.demo.service.detail.ComplexIdsService import ComplexIdsService
from apps.demo.service.detail.ComplexCityareaService import ComplexCityareaService
from apps.demo.service.detail.ComplexCityarea2Service import ComplexCityarea2Service
from apps.demo.service.detail.ComplexConfigService import ComplexConfigService
from apps.demo.dao.detail.ComplexGovDao import ComplexGovDao # 
from apps.demo.dao.detail.ComplexDao import ComplexDao #
from utils.processor import Processor
from databases.dbfactory.dbfactory import dbfactory
from utils.BaseUtils import BaseUtils
import json
import re


class ComplexService(BaseMysqlService):
    def __init__(self, *args, **kwargs):
        """
        :param city_ab: 城市缩写
               redis_conn: 初始化redis链接
               mysql_rw: 初始化mysql链接
               developer_offer_key:　redis缓存key
        """

        self.dao = ComplexDao(*args, **kwargs)
        self.govdao = ComplexGovDao(*args, **kwargs)
        self.govservice = ComplexGovService()
        self.commentservice = ComplexCommentService()
        self.housetypeservice = ComplexHousetypeService()
        self.licenseservice = ComplexLicenseService()
        self.informationservice = ComplexInformationService()
        self.idsservice = ComplexIdsService()
        self.complex_config_service = ComplexConfigService()
        self.city = kwargs.get('city')
        self.developer_offer_key = '%s_developer' % self.city
        self.redis_conn = dbfactory.db_redis(conf_name=kwargs.get("conf_name", "complex"))
        self.redis_cache = dbfactory.db_redis(conf_name=kwargs.get("conf_name", "complex_api"))

    def split_complex(self, *args, **kwargs):
        city = kwargs.get('city')
        complex_id = kwargs.get("complex_id")
        split_complex = kwargs.get("split_complex")
        split_source = ",".join([str(i) for i in split_complex.get("source")])
        md5_cache_key = f"{city}_complexids"

        # 判断要拆分的渠道是否存在
        filter = {
            "field": ["id"],
            "filter": f"complex_id={complex_id} AND source_id in ({split_source})",
            "city": city
        }
        data = self.govservice.select_by_filter(**filter)
        if not data:
            return "要拆分的楼盘渠道不存在"

        # 生成拆分楼盘md5 重新生成
        split_md5 = self.gtmd5(split_complex.get("name"))
        self.idsservice.delete_by_filter(city=city, filter=f"complex_id='{split_md5}' AND id={complex_id}")
        self.redis_cache.hdel(md5_cache_key, split_md5)
        split_id = self.set_cache(split_md5, md5_cache_key, city)

        # 更新gov表的complex_id 更新其他表的数据
        split_filter = {
            "data": {
                "complex_name": split_complex.get("name"),
                "complex_id": split_id
            },
            "filter": f"complex_id={complex_id} AND source_id in ({split_source})",
            "city": city
        }
        self.govservice.update(**split_filter)
        self.commentservice.update(**split_filter)
        self.housetypeservice.update(**split_filter)
        self.licenseservice.update(**split_filter)
        self.informationservice.update(**split_filter)

        # 重新合并两个渠道id
        cc = ComplexMergeService()
        cc.service(complex_id=complex_id, city=city)
        cc.service(complex_id=split_id, city=city)
        return f"拆分{split_complex.get('name')}成功"

    def gtmd5(self, complex_name):
        if len(complex_name[complex_name.find('('):-1]) > 13:
            complex_name = re.sub(r'\(.*', '', complex_name)
        elif not (
                re.search(r'期', complex_name) or re.search(r'别墅', complex_name) or re.search(r'商铺', complex_name)):
            complex_name = re.sub(r'\(.*', '', complex_name)

        pinyin_cm = BaseUtils.getPiyin(complex_name)
        complex_id = BaseUtils.getMd5(pinyin_cm)
        return complex_id

   
if __name__ == '__main__':
    CS = ComplexService()
    # res = CS.get_complex_config(city='bj', type= 1)
    res = CS.merge_complex(city='bj', type= 1)
    print(res)
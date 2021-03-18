# -*- coding: UTF-8 -*-

import pymysql
# from apps.config.Config import mysql_conf, get_db
from apps.config.CitySouceMapping import get_db, getConfigName
from apps.config.Config import mysql_conf
import contextlib
import logging
class MysqlDB_Rent(object):
    def __init__(self, *args, **kwargs):
        self.conf_name = kwargs.get("conf_name")
        self.db_type = kwargs.get("db_type")
        self.conf = mysql_conf.get(self.conf_name)

    @contextlib.contextmanager
    def get_conn(self, *args, **kwargs):
        city = kwargs.get("city")
        self.conf_name = getConfigName(city=city, type=self.conf_name)
        conf = self.conf.get(kwargs.get("link_type", 'default'))
        # 获取主从连接
        host = conf.get("host")
        port = conf.get("port")
        user = conf.get("user")
        passwd = conf.get("passwd")
        db_name = get_db(type=self.conf_name, city=city)
        conn = pymysql.connect(host=host, port=port, user=user, password=passwd, db=db_name, charset="utf8")
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        try:
            yield cursor
            logging.info(cursor._last_executed)
        except Exception as e:
            logging.error(e)
        finally:
            conn.commit()
            cursor.close()
            conn.close()


# -*- coding: utf-8 -*-s
import redis
from apps.config.Config import pika_conf
class PikaDB(object):
    def __init__(self, *args, **kwargs):
        pass

    pool = {}

    @staticmethod
    def getPikaConn(**kwargs):
        conf_name = kwargs.get("conf_name")
        link_type = kwargs.get("link_type", 'default')
        server = PikaDB.pool.get(conf_name+link_type,None)
        if server:
            return server
        conf = pika_conf.get(conf_name, {}).get(link_type,None)
        if not conf:
            print ("pika配置未找到")
            return
        db_url = conf.get("db_url", "")
        host = conf.get("host", "127.0.0.1")
        port = conf.get("port", 6379)
        db = conf.get("db", 0)
        max_connections = conf.get("max_connections", 10)
        if db_url:
            pool = redis.StrictRedis.from_url(url=db_url)
        else:
            pool = redis.ConnectionPool(host=host, port=port, db=db,max_connections=max_connections)
            # pool = redis.StrictRedis(connection_pool=rdp)
        server = redis.StrictRedis(connection_pool=pool)
        PikaDB.pool.setdefault(conf_name, server)
        return server


# -*- coding: utf-8 -*-s
import redis
from apps.config.Config import redis_conf
class RedisDB(object):
    def __init__(self, *args, **kwargs):
        pass

    pool = {}

    @staticmethod
    def getRedisConn(**kwargs):
        conf_name = kwargs.get("conf_name")
        server = RedisDB.pool.get(conf_name,None)
        if not server:
            conf = redis_conf.get(conf_name, {})
            db_url = conf.get("db_url", "")
            host = conf.get("host", "127.0.0.1")
            port = conf.get("port", 6379)
            db = conf.get("db", 0)
            max_connections = conf.get("max_connections", 2)
            if db_url:
                pool = redis.ConnectionPool.from_url(url=db_url)
            else:
                pool = redis.ConnectionPool(host=host, port=port, db=db,max_connections=max_connections)
            server = redis.StrictRedis(connection_pool=pool)
            RedisDB.pool.setdefault(conf_name, server)
        return server


if __name__ == '__main__':

    RB = RedisDB(conf_name="plathouse")
    con = RB.getRedisConn()
    con.set("name","888")


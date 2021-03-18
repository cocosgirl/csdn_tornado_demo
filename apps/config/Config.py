#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Desc    : 数据库配置文件,在此仅展示配置的格式

log_config = {
    "path": "/Users/logs/",
    "level": "DEBUG"  # INFO ERROR DEBUG
}

mongo_conf = {
    "borough": {
        "default": {
            # 主库
            'host': 'test',
            'port': 3606,
            'username': 'test',
            'password': 'test',
        },
        "slave_1": {
            'host': '',
            'port': 9603,
            'username': '',
            'password': '',
        },
    }
}

redis_conf = {
    "plathouse": {
        "db_url": "redis://:test:9431/0",
    },

}

pika_conf = {
    "sell_api": {
        "host": "",
        "port": 9221,
        "pre": ""
    },
    "plat_api": {
        "host": "",
        "port": 9221,
        "pre": "D-plat-"
    }
}

rabbitmq_conf = {
    "rent": {
        "default": {
            # "host": "",
            "host": "",
            "user": "",
            "passwd": "data",
            "port": 5672
        },
        "slave_1": {
            "host": "",
            "user": "",
            "passwd": "",
            "port": 5672
        }
    }
}

mysql_conf = {
    "sell": {
        "default": {
            "max_connections": 20,
            "wait_connection_timeout": 3,
            "host": "",
            "user": "",
            "passwd": "",
            "port": 3306,
            "charset": "utf8",
        },
        "slave_1": {
            "max_connections": 20,
            "wait_connection_timeout": 3,
            "host": "",
            "user": "afe-rw",
            "passwd": "",
            "port": 3306,
            "charset": "utf8"
        },
        "sell_online": {
            "max_connections": 20,
            "wait_connection_timeout": 3,
            "host": "",
            "user": "data_rw",
            "passwd": "",
            "port": 9521,
            # "port": 3306,
            "charset": "utf8"
        },
    },
    "rent": {
        "default": {
            "max_connections": 20,
            "wait_connection_timeout": 3,
            "host": "",
            "user": "",
            "passwd": "",
            "port": 9532,
            "charset": "utf8",
        },
        "slave_1": {
            "max_connections": 20,
            "wait_connection_timeout": 3,
            "host": "127.0.0.1",
            "user": "",
            "passwd": "",
            "port": 3306,
            "charset": "utf8"
        },
    }
}

tidb_conf = {
    "sell_api": {
        "default": {
            "max_connections": 20,
            "wait_connection_timeout": 3,
            "host": "",
            "user": "",
            "passwd": "",
            "port": 9902,
            "charset": "utf8",
        },
    },

}
es_config = {
    "sell": {
        "host": [
            # ":9200"
            ":9200"
        ],
        "maxsize": 25
    },
    "rent": {
        "host": [
            ":9200"
        ],
        "maxsize": 25
    }
}

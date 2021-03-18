#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/2 下午1:39
# @Author  : 
# @Site    : 
# @File    : BaseLogs.py
# @Software: PyCharm
import logging.handlers
from apps.demo.config.Config import log_config
class Logger(logging.Logger):
    def __init__(self, *args, **kwargs):
        super(Logger, self).__init__(self)
        self.name = kwargs.get("name")
        self.path = log_config.get('path')
        self.le = log_config.get("level")
        self.fname = self.path+"/"+self.name+".log"
        # 创建一个handler，用于写入日志文件 (每天生成1个，保留30天的日志)
        fh = logging.handlers.TimedRotatingFileHandler(filename=self.fname, when='D', interval=3, backupCount=3)
        fh.suffix = "%Y-%m-%d.log"
        le_conf= {"INFO": 20, "DEBUG": 10, "WARNING": 30, "ERROR": 40}
        # 再创建一个handler，用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(le_conf.get(self.le))
        # 定义handler的输出格式
        formatter = logging.Formatter('[%(asctime)s]-%(filename)s [Line:%(lineno)d]-[%(levelname)s]-[thread:%(thread)s]-[process:%(process)s]-%(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # 给logger添加handler
        self.addHandler(fh)
        self.addHandler(ch)
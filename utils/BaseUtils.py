#!/usr/bin/env python
# -*- coding: utf-8 -*-
import hashlib
import time
import json
import requests
# import pinyin
import re
from threading import Thread


class BaseUtils(object):

    #异步装饰器
    # @staticmethod
    # def async(f):
    #     def wrapper(*args, **kwargs):
    #         thr = Thread(target=f, args=args, kwargs=kwargs)
    #         thr.start()
    #     return wrapper

    #计算排序权重
    @staticmethod
    def countSortWeight(priority, cnt, updated, pic_sign):
        return int(priority * 7 * 86400 + cnt * 5 * 86400 + updated - pic_sign * 90 * 86400)

    @staticmethod
    def getMd5(value):
        m = hashlib.md5()
        m.update(value.encode("utf8"))
        return m.hexdigest()

    @staticmethod
    def getIntTime():
        return int(time.time())

    @staticmethod
    def getPiyin(value):
        py = pinyin.get(value, format="strip")
        return BaseUtils.extract_str(py)

    @staticmethod
    def extract_str(string):
        string = string.lower()
        regEx = "\W+"
        pattern = re.compile(regEx)
        mt = re.sub(pattern, '', string=string)
        return mt

    @staticmethod
    def extract(*args, **kwargs):
        data_list = re.findall(kwargs.get("regex"), str(kwargs.get("data")))
        return len(data_list) > 0 and data_list.pop()

    @staticmethod
    def replace(*args, **kwargs):
        return re.sub(kwargs.get("regex"), kwargs.get("value"), kwargs.get("data"))

    @staticmethod
    def getFpy(value, delimiter=""):
        py = pinyin.get(value, format="strip", delimiter=delimiter)
        return py

    @staticmethod
    def getSpy(value, delimiter=""):
        py = pinyin.get_initial(value, delimiter=delimiter)
        return py

    @staticmethod
    def getSignature(data):
        key = ''

        return key

    @staticmethod
    def list_to_dict(data, key, value):
        result = dict()
        for i in data:
            result.setdefault(i[key], i[value])
        return result

    
    @staticmethod
    def stamp_to_time(timestamp, fromdata="%Y-%m-%d %H:%M:%S"):
        if timestamp and re.search('^\d{9,}$', str(timestamp)):
            time_local = time.localtime(int(timestamp))
            dt = time.strftime(fromdata, time_local)
            return dt
        else:
            return timestamp

    @staticmethod
    def time_to_stamp(time_data, fm=[]):
        if re.search('^\d{9,}$', time_data):
            return int(time_data)
        time_data = BaseUtils.replace(data=time_data.strip(), regex="（.*|\(.*", value="")
        for_dic = {"上旬": "10日", "中旬": "20日", "下旬": "28日"}
        for k, v in for_dic.items():
            time_data = BaseUtils.replace(data=time_data, regex=k, value=v)
        formats = [
            "%Y.%m.%d %H:%M:%S",
            "%Y.%m.%d",
            "%Y.%m",
            "%y.%m",

            "%Y-%m-%d %H:%M:%S",
            "%Y-%m-%d %H:%M",
            "%Y-%m-%d",
            "%Y-%m",
            "%y-%m",
            "%Y",

            "%y/%m/%d",

            "%y",
            "%Y年",
            "%y年",
            "%Y年%m月",
            "%y年%m月",
            "%Y年%m月%d日",
            "%y年%m月%d日",
        ]
        formats += fm
        time_stamp = 0
        for form in formats:
            try:
                time_stamp = time.mktime(time.strptime(time_data, form))
                if time_stamp:
                    return int(time_stamp)
            except Exception as e:
                pass
        return int(time_stamp)

    @staticmethod
    def mkdir(path):
        # 引入模块
        import os

        # 去除首位空格
        path = path.strip()
        # 去除尾部 \ 符号
        path = path.rstrip("\\")

        # 判断路径是否存在
        # 存在     True
        # 不存在   False
        isExists = os.path.exists(path)

        # 判断结果
        if not isExists:
            # 如果不存在则创建目录
            # 创建目录操作函数
            os.makedirs(path)

            print(path + ' 创建成功')
            return True
        else:
            # 如果目录存在则不创建，并提示目录已存在
            print(path + ' 目录已存在')
            return False


class Prpcrypt():

    def __init__(self, key, texts):
        self.AES = None
        if not self.AES:
            from Crypto.Cipher import AES
            from binascii import b2a_hex, a2b_hex
            self.AES = AES
            self.b2a_hex = b2a_hex
            self.a2b_hex = a2b_hex
        self.key = key
        self.mode = self.AES.MODE_CBC
        self.texts = texts

        # 加密函数，如果text不是16的倍数【加密文本text必须为16的倍数！】，那就补足为16的倍数
    def encrypt(self, text):
        cryptor = self.AES.new(self.key, self.mode, self.key)
        # 这里密钥key 长度必须为16（AES-128）、24（AES-192）、或32（AES-256）Bytes 长度.目前AES-128足够用
        length = 32
        count = len(text)
        if (count % length != 0):
            add = length - (count % length)
        else:
            add = 0
        text = text + ('\0' * add)
        self.ciphertext = cryptor.encrypt(text)
        # 因为AES加密时候得到的字符串不一定是ascii字符集的，输出到终端或者保存时候可能存在问题
        # 所以这里统一把加密后的字符串转化为16进制字符串
        print('encrypt', self.ciphertext)
        return self.b2a_hex(self.ciphertext)

        # 解密后，去掉补足的空格用strip() 去掉
    def decrypt(self, text):
        cryptor = self.AES.new(self.key, self.mode, self.key)
        plain_text = cryptor.decrypt(self.a2b_hex(text)).decode()
        return plain_text.rstrip('\0')

    def get_encrypt(self):
        aes_text = self.encrypt(self.texts)
        return str(aes_text).replace("b'", '').replace("'", '')

    def get_decrypt(self):
        return self.decrypt(self.texts)


if __name__ == '__main__':
    #print(BaseUtils.getMd5('borough_id=1&cityarea_id=2’135a69cbfe5edeab9a4a83551992572e'))
    key = "keyskeyskeyskeys"
    str1 = "0123456789ABCDEF"
    p1 = Prpcrypt(key, str1)
    r1 = p1.get_encrypt()
    print(r1)
    p2 = Prpcrypt(key, r1)
    print(p2.get_decrypt())




#135a69cbfe5edeab9a4a83551992572e
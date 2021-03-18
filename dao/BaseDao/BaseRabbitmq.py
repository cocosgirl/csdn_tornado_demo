#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-3-26 下午 18:19
# @Author  : tanghan@demofang.com
# @Desc    :
from databases.dbfactory.dbfactory import dbfactory
from dao.Base import Base
import pika


class BaseRabbitmq(Base):
    def __init__(self, *args, **kwargs):
        self.conf_name = kwargs.get("conf_name")
        self.conn = dbfactory.create_db(conf_name=self.conf_name, db_type="db_rabbitmq")

    # 生产者关键字模式
    # def basic_publish(self, *args, **kwargs):
    #     try:
    #         with self.conn.get_conn() as mq:
    #             mq.exchange_declare(exchange=kwargs.get("exchange"), durable=True, exchange_type='direct')
    #             mq.basic_publish(exchange=kwargs.get("exchange"),  routing_key=kwargs.get("routing_key"), body=kwargs.get("body"))
    #             # 声明queue
    #             # mq.queue_declare(queue=kwargs.get("queue"))
    #             # mq.queue_bind(exchange='testapi_relase_house', queue=kwargs.get("queue"))
    #             # mq.basic_publish(exchange='', routing_key=kwargs.get("queue"), body=kwargs.get("body"))
    #
    #     except Exception as e:
    #         print("basic_publish", e)
    #         return False

    # 竞争模式，直接指定queue
    def basic_publish(self, *args, **kwargs):
        try:
            with self.conn.get_conn() as channel:
                channel.queue_declare(queue=kwargs.get("queue"), durable=True)
                channel.basic_publish(exchange='',
                                      routing_key=kwargs.get("queue"),
                                      body=kwargs.get("body"),
                                      properties=pika.BasicProperties(delivery_mode=2)
                                      )
                return True

        except Exception as e:
            print("basic_publish", e)
            return False

    # 消费者关键字模式（暂时没有地方调用）
    def basic_consume(self, *args, **kwargs):
        try:
            with self.conn.get_conn() as mq:
                # mq.exchange_declare(exchange='testapi_relase_house', exchange_type='direct')
                result = mq.queue_declare(exclusive=True)#创建随机队列，当消费者与rabbitmq断开连接时，这个队列将自动删除。
                queue_name = result.method.queue#分配随机队列的名字。
                severities = [kwargs.get("direct")]#可以接收绑定关键字info或err的消息，列表中也可以只有一个
                for severity in severities:
                    # 将交换机、队列、关键字绑定在一起，使消费者只能根据关键字从不同队列中取消息
                    mq.queue_bind(exchange=kwargs.get("exchange"), queue=queue_name, routing_key=severity)
                #开始消费消息
                mq.basic_consume(self.callback, queue=queue_name, no_ack=True)
                return mq.start_consuming()

        except Exception as e:
            print("basic_consume", e)
            return False

    def callback(self, ch, method, properties, body):  # 定义回调函数，接收消息
        print(" [消费者] %r:%r" % (method.routing_key, body))


if __name__ == '__main__':
    BRQ = BaseRabbitmq(conf_name='sell').basic_publish(queue='chinas', body='666')
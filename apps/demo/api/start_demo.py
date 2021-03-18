#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Desc    :
import platform

# 这是python3.8做出的设计,否则不能使用,
if platform.system() == "Windows":
    import asyncio
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

import os
import sys
import inspect
common_dir = os.path.realpath(os.path.abspath(os.path.join(
    os.path.split(inspect.getfile(inspect.currentframe()))[0],
    "../../../")))
print(common_dir)
if common_dir not in sys.path:
    sys.path.insert(0, common_dir)
import tornado.ioloop

 
from apps.demo.controller.detail.demoController import route as route1

if __name__ == '__main__':
    port = 3331
    if len(sys.argv) > 1:
        port = sys.argv[1]
    routes = route1.urls
    application = tornado.web.Application(routes)
    application.listen(port)
    tornado.ioloop.IOLoop.instance().start()




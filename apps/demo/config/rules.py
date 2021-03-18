
local_path = "/Users/hbd/Documents/file"

monit_conf = """check process %(city)s-%(channel)s-complex matching "%(city)s-%(channel)s-complex"

    start program = "/home/demo/project/demo-blackwidow/blackwidow/bin/run.sh %(city)s-%(channel)s-complex details"

    stop program = "/home/demo/project/demo-blackwidow/blackwidow/bin/stop.sh %(city)s-%(channel)s-complex details"

    group %(city)s
    group %(channel)s
    group 0514

"""

super_conf = """
[program:%(city)s-complex-etl1]
directory = /home/demo/hbd/demo_etl/demo_etl/bin
command = python start_new.py complex %(city)s
autostart = false
autorestart = true
startretries = 3
user = demo
stdout_logfile = /home/demo/log/complex_etl/%(city)s-etl.log
"""

table_conf = """CREATE TABLE `building` (
  `id` int(11) NOT NULL COMMENT '自增id',
  `building_id` int(11) DEFAULT '0' COMMENT '楼栋id',
  `complex_id` int(11) DEFAULT '0' COMMENT '楼盘id',
  `building_name` varchar(0) DEFAULT '' COMMENT '楼栋名称',
  `building_stages` int(2) DEFAULT '0' COMMENT '楼栋分期',
  `building_year` int(11) DEFAULT '0' COMMENT '建筑年代',
  `unit_total` int(2) DEFAULT '0' COMMENT '单元数',
  `hosue_total` int(10) DEFAULT '0' COMMENT '户数',
  `house_pic_id` int(11) DEFAULT '0' COMMENT '户型图id 多个按，分割',
  `floor_total` int(4) DEFAULT '0' COMMENT '总楼层',
  `building_toward` int(2) DEFAULT '0' COMMENT '楼栋朝向 1''东'', 2''西'', 3 ''南'', 4 ''北'', 5 ''东南'', 6  ''东北'', 7''西南'', 8  ''西北'', 9  ''南北'', 10''东西'', 11 ''东西南'', 12  ''东南北'', 13 ''西南北'', 14''东西北'', 15  ''东西南北''',
  `building_location` int(2) DEFAULT '0' COMMENT '楼栋位置 临街 1''东'', 2''西'', 3 ''南'', 4 ''北'', 5 ''东南'', 6  ''东北'', 7''西南'', 8  ''西北'', 9  ''南北'', 10''东西'', 11 ''东西南'', 12  ''东南北'', 13 ''西南北'', 14''东西北'', 15  ''东西南北''   16不临街 17居中 18其他',
  `property_type` int(2) DEFAULT '0' COMMENT '物业类别 板楼、塔楼、板塔结合、砖楼',
  `lose_floor` int(2) DEFAULT '0' COMMENT '丢失楼层 ',
  `provide_elevator` varchar(100) DEFAULT '' COMMENT '电梯情况',
  `complex_building_type` int(3) DEFAULT '0' COMMENT '建筑类型',
  `sale_status` int(2) DEFAULT '0' COMMENT '销售状态',
  `pic_xy` varchar(100) DEFAULT '' COMMENT '沙盘图显示坐标',
  PRIMARY KEY (`id`),
  KEY `complex_id` (`complex_id`),
  KEY `building_stages` (`building_stages`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;
"""
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 00:52:49 2020

@author: zmddzf
"""

# ============================================================================
# ==========================服务配置文件=======================================
#                      1. 配置数据库连接
#                      2. 配置服务ip与端口
#                      3. 配置推荐算法参数
# ============================================================================


"""
数据库连接配置
"""
# ***********连接配置***********
db_ip = "gz-cynosdbmysql-grp-dlns7hud.sql.tencentcdb.com"  # ip地址
db_port = "27124"  # 端口号
username = "user001"  # 用户名
password = "SGG@15sys!DB7"  # 密码
database = "recommender"  # 数据库
connection = "mysql+mysqlconnector://{}:{}@{}:{}/{}".format(username, password, db_ip, db_port, database)

# ***********连接池配置***********
echo = False  # 是否打印sql
pool_recycle = 21600  # 连接回收时长
pool_size = 5  # 连接池大小

"""
服务配置
"""
service_ip = "127.0.0.1:5000"

"""
推荐算法配置
"""
second_k = 500  # 二次筛选邻近用户个数
indicator_k = 8  # 指标筛选返回学校个数



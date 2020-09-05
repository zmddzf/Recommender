# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 00:04:27 2020

@author: zmddzf
"""

import grpc
from sqlalchemy import create_engine
import time
import recommend_pb2 as pb2
import recommend_pb2_grpc as pb2_grpc
from concurrent import futures
from data_filter_layer.filt_data import DataFilter
from feature_extraction_layer.extract_feature import *
from feature_extraction_layer.evaluate_feature import FeatureEvaluating
from nueral_network_layer.compute_similarity import SimComputing
from config import *
import numpy as np

class Recommender(pb2_grpc.RecommenderServicer):
    """
    推荐类
    包含对外暴露接口
    """
    engine = create_engine(connection, echo=echo, pool_recycle=pool_recycle, pool_size=pool_size)  # 数据库引擎
    dataFilter = DataFilter(engine)  # 数据筛选层
    featureEvaluating = FeatureEvaluating()  # 特征评估实例
    simComputing = SimComputing()  # 神经网络层
    
    
    def recommend(self, request, context):
        """
        推荐函数
        """
        # 获取参数
        ug_level = request.ug_level  # 学校档次
        ug_major = request.ug_major  # 本科专业
        intended_country = request.intended_country  # 意向国家
        ug_gpa = request.ug_gpa  # 本科gpa
        gre = request.gre  # gre成绩
        gmat = request.gmat  # gmat成绩
        toefl = request.toefl  # 托福成绩
        ielts = request.ielts  # 雅思成绩
        marker = request.marker  # 个人说明
        
        # 参数校验
        if ug_level == '' or intended_country == '' or ug_gpa == 0 or ug_major == '':
            data = {"key":pb2.ratio(partly_ratio=None, total_ratio=None)}
            return pb2.sysReponse(code=3, msg="请检查传入参数是否正确！", data=data)        
        
        # 特征处理
        feature = []
        try:
            feature = process_feature(ug_gpa, gre, gmat, ug_level, ielts, toefl, marker, ug_major)
            print(feature)
        except Exception as e:
            print(e)
            data = {"key":pb2.ratio(partly_ratio=None, total_ratio=None)}
            return pb2.sysReponse(code=3, msg="特征处理过程中发生异常, 请检查传入参数是否正确！", data=data)
        
        # 特征评价
        score = 0
        try:
            score = self.featureEvaluating.evaluate([feature[3], feature[0], feature[4], feature[5], feature[6], feature[7], feature[8]])
        except Exception as e:
            print(e)
            data = {"key":pb2.ratio(partly_ratio=None, total_ratio=None)}
            return pb2.sysReponse(code=2, msg="特征评价过程中发生异常, 错误未知！", data=data)
        print(2)
        
        # 初次筛选
        aid_score_list = []
        try:
            aid_score_list = self.dataFilter.first_filter([intended_country])
        except Exception as e:
            print(e)
            data = {"key":pb2.ratio(partly_ratio=None, total_ratio=None)}
            return pb2.sysReponse(code=4, msg="一次筛选发生异常, 请检查数据库连接是否超时！", data=data)
        print(3)
        
        # 二次筛选
        aid_vector_dict = {}
        try:
            aid_vector_dict = self.dataFilter.second_filter(score, aid_score_list, second_k)
        except Exception as e:
            print(e)
            data = {"key":pb2.ratio(partly_ratio=None, total_ratio=None)}
            return pb2.sysReponse(code=4, msg="二次筛选发生异常, 请检查数据库连接是否超时！", data=data)
        
        
        # 神经网络三次筛选
        aid_list = []
        try:
            aid_list = self.simComputing.compute_sim(feature, aid_vector_dict)
        except Exception as e:
            print(e)
            data = {"key":pb2.ratio(partly_ratio=None, total_ratio=None)}
            return pb2.sysReponse(code=2, msg="神经网络计算时出现异常, 错误未知！", data=data)

        
        # 指标四次筛选
        school_ratio_dict = {}
        try:
            school_ratio_dict = self.dataFilter.indicator_filter(aid_list, intended_country, 8)
        except Exception as e:
            print(e)
            data = {"key":pb2.ratio(partly_ratio=None, total_ratio=None)}
            return pb2.sysReponse(code=4, msg="二次筛选发生异常, 请检查数据库连接是否超时！", data=data)
        
        # 构建返回data字段
        data = {}
        for key in school_ratio_dict:
            data[key] = pb2.ratio(partly_ratio=school_ratio_dict[key][0], total_ratio=school_ratio_dict[key][1])
        print(data)
        
        return pb2.sysReponse(code=0, msg="ok", data=data)
        

def run():
    grpc_server = grpc.server(
        futures.ThreadPoolExecutor(max_workers=4)
    )
    
    pb2_grpc.add_RecommenderServicer_to_server(Recommender(), grpc_server)
    grpc_server.add_insecure_port('127.0.0.1:5000')
    print("service will start at 127.0.0.1:5000")
    grpc_server.start()
    
    try:
        while 1:
            time.sleep(3600)
    except KeyboardInterrupt:
        grpc_server.stop(0)
        print("service has been stopped")
        
        
        
run()

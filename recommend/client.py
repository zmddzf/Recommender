# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 00:19:11 2020

@author: zmddzf
"""

import grpc
import recommend_pb2 as pb2
import recommend_pb2_grpc as pb2_grpc


def run():
    conn = grpc.insecure_channel("127.0.0.1:5000")
    client = pb2_grpc.RecommenderStub(channel=conn)
    response = client.recommend(pb2.userReq(
            ug_level = "双非一本",
            ug_major = "信息管理与信息系统",
            intended_country = "英国",
            ug_gpa = 86.8,
            gre = 0,
            gmat = 0,
            toefl = 0,
            ielts = 6.5,
            marker = "实习科研竞赛奖学金"
    ))
    
    return response
    
x = run()

print(x)
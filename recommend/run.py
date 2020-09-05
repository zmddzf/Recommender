# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 11:09:33 2020

@author: zmddzf
"""

from concurrent import futures
import time
import grpc
import recommend_pb2 as pb2
import recommend_pb2_grpc as pb2_grpc
from service import Recommender

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

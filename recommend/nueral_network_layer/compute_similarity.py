# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 14:07:35 2020

@author: zmddzf
"""

from .siamese_network import build_model
import numpy as np

class SimComputing:
    """
    相似度计算类
    使用孪生神经网络计算相似度
    """
    model = build_model(input_shape=109)
    model.load_weights("./utils/siamese_network.h5")
    
    def sim(self, v1, v2):
        """
        :param v1: 输入数组1 109个特征
        :param v2: 同输入数组1
        :return score: 相似度评分
        """
        v1_arr = np.array(v1).reshape(1,109)
        v2_arr = np.array(v2).reshape(1,109)
        
        score = self.model.predict([v1_arr, v2_arr])[0][0]
        return score
    
    def compute_sim(self, v1, vector_dict):
        """
        寻找出相似的申请人
        相似度大于50%的申请人即为相似申请人
        :param v1: 输入用户数组109个特征
        :param vector_dict: {aid: vector}
        :return result: aid列表
        """
        aid_list = []
        sim_list = []
        for key, val in vector_dict.items():
            aid_list.append(key)
            sim_list.append(self.sim(val, v1))
        
        result = []
        for i in range(len(sim_list)):
            if sim_list[i] >= 0.5:
                result.append(aid_list[i])
        return result
        
    
    
    
    


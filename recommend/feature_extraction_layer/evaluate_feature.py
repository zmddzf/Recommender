# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 00:03:56 2020

@author: zmddzf
"""

import json
import numpy as np

class FeatureEvaluating:
    """
    特征评估类
    使用综合评价模型评价申请人背景得分
    """
    # 读取评价模型评分
    with open("./utils/evaluation_model_weight.json",'r') as load_f:
        weight = json.load(load_f)
        
    def __init__(self):
        self.tier1 = np.array([self.weight['tier1']['hard']]*3 + [self.weight['tier1']['soft']]*4) # 第一层权重向量
        self.tier2 = np.array(list(self.weight['tier2'].values())) # 第二层权重向量
        
    def evaluate(self, v):
        """
        :param v: 经过特征提取的背景数据列表 [school_level, gpa, eng, research, job, honor, exchange]
        :return score: 背景数据评分
        """
        v_arr = np.array(v)
        score = self.tier1.dot(v_arr * self.tier2)
        return score
        
        
        
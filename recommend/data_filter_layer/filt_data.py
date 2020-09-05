# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 14:56:49 2020

@author: zmddzf
"""

from database_layer.tables import *
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import numpy as np
from sqlalchemy import func

class DataFilter:
    """
    数据筛选类
    初次筛选找出对应区域申请人
    二次筛选找出得分邻近申请人
    指标筛选找出最可能录取的学校
    """
    def __init__(self, engine):
        Session = sessionmaker(bind=engine)
        self.session = Session()
        
    def close_session(self):
        """
        断开数据库连接
        """
        self.session.close()
        
    def first_filter(self, area):
        """
        初次筛选
        :param area: 目标区域, list形式
        :return result: 初次筛选结果, 为用户记录列表, [(aid, score),(aid, score),(aid, score),...,(aid, score)]
        """
        
        # 从school表查符合区域的学校编码
        school_codes = self.session.query(School_t.code).filter(School_t.country.in_(area)).all()
        school_codes = [i[0] for i in school_codes]
        
        # 从offer表查符合指定区域学校的录取用户aid
        aid_list = self.session.query(Offer_t.aid).filter(Offer_t.school_code.in_(school_codes)).all()
        aid_list = set([i[0] for i in aid_list])
        
        # 从application表查询相应的aid与score
        result = self.session.query(Application_t.aid, Application_t.score).filter(Application_t.aid.in_(aid_list)).all()
        
        return result
    
    def second_filter(self, score, first_List, k):
        """
        二次筛选
        :param score: 对应得分score
        :param first_List: 待筛选score列表[(aid, score),(aid, score),(aid, score),...,(aid, score)]
        :param k: 邻近的用户个数
        :return result: 二次筛选结果, 返回用户向量字典 {aid: vectore}
        """
        # 选择得分临近的前k个用户
        score_list = np.array(list(dict(first_List).values()))
        score_list = np.abs(np.array(score_list) - score).tolist()
        
        aid_list = list(dict(first_List).keys())
        neighbors = [x for _,x in sorted(zip(score_list,aid_list))][:k]
        
        # 查询邻近用户数据
        applicants_list = self.session.query(Application_t).filter(Application_t.aid.in_(neighbors)).all()
        result = dict()
        
        # 构建返回结果
        for apc in applicants_list:
            vector = [apc.gpa,apc.gre,apc.gmat,apc.bschool,apc.language_score,
                      apc.research,apc.jobs,apc.honor,apc.exchange] + eval(apc.major_vector.replace(" ",","))
            result[apc.aid] = vector
        
        return result
        
    def indicator_filter(self, aid_list, area, k):
        """
        指标筛选
        :param aid_list: 三次筛选的用户列表
        :param area: 选校区域
        :param k: 待推荐的学校个数
        :return result: 推荐的学校, 形如{school_name: [partly_ratio, total_ratio]}
        """
        # 案例库总offer数量
        offer_count = self.session.query(func.count(Offer_t.offer_id)).all()[0][0]
        print(offer_count)
        
        # 查询对应区域的学校code
        area_code_list = self.session.query(School_t.code).filter(School_t.country.in_([area])).all()
        area_code_list = [i[0] for i in area_code_list]
        
        # 查询对应offer的学校编码
        school_code_list = self.session.query(Offer_t.school_code).filter(Offer_t.aid.in_(aid_list), Offer_t.school_code != None, Offer_t.school_code.in_(area_code_list)).all()
        school_code_list = [i[0] for i in school_code_list]
        print(school_code_list)
        
        # 对应offer的所有不重复学校编码
        school_code_set = list(set(school_code_list))

        # 将学校编码列表转为学校名称列表
        school_name_list = self.session.query(School_t.cn_name).filter(School_t.code.in_(school_code_list)).all()
        school_name_list = [i[0] for i in school_name_list]
        print(school_name_list)
        
        code_name_dict = dict(self.session.query(School_t.code, School_t.cn_name).filter(School_t.code.in_(school_code_set)).all())
        code_count_dict = dict(self.session.query(Offer_t.school_code, func.count(Offer_t.offer_id)).group_by(Offer_t.school_code).filter(Offer_t.school_code.in_(school_code_set)).all())
        print(code_count_dict)

        # 邻近样本中各个学校的个数
        partly_ratio_temp = dict()
        for key in school_code_list:
            partly_ratio_temp[key] = partly_ratio_temp.get(key, 0) + 1
        partly_ratio = dict()
        for key in partly_ratio_temp:
            partly_ratio[code_name_dict[key]] = partly_ratio_temp[key] / len(school_code_list)
        

        
        # 查询对应学校编码的学校名称与该校在总案例库的占比
        total_ratio = dict()
        for key in school_code_set:
            total_ratio[code_name_dict[key]] =  code_count_dict[key] / offer_count
        
        # 构建全部{school_name, [partly_ratio, total_ratio]}
        school_partly_total = dict()
        for key in total_ratio:
            school_partly_total[key] = [partly_ratio[key], total_ratio[key]]
            
        # 构建指标字典
        school_indicator = dict()
        for key in school_partly_total:
            school_indicator[key] = school_partly_total[key][0] / (school_partly_total[key][1]+1)
            
        # 寻找前k个最可能的学校 构建result
        temp = sorted(school_indicator.items(), key=lambda x: x[1], reverse=True)[:k]
        result = dict([(i[0], school_partly_total[i[0]]) for i in temp])
            
        return result
        
        
        
        
        
        
        
        
    
    
    
    

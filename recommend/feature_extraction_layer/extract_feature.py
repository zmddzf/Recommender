# -*- coding: utf-8 -*-
"""
Created on Mon May 18 15:07:07 2020

@author: zmddzf
"""

from gensim.models import Word2Vec

# ====================================
# =========定义部分全局变量=============
# ====================================
w2v = Word2Vec.load('./utils/w2v-model-100')  # 读取word2vec模型
school_level_dict = {'211': 0.67, '211 & 985': 1, '二本': 0, '双非一本': 0.33}  # 定义学校档次映射
language_score = {0:4, 31:4.5, 34:5, 45:5.5, 59:6, 78:6.5, 93:7, 101:7.5, 109:8, 114:8.5, 117:9}  # 语言转换规则
keys = sorted(language_score.keys(), reverse=True)

# ====================================
# =========定义函数部分================
# ====================================


def process_language(ielts, toefl):
    # 处理语言成绩
    for i in range(len(keys)):
        if  toefl > keys[i]:
            toefl = language_score[keys[i]]
            break
    score = max(ielts, toefl)
    return [score / 9]

def process_school(school):
    # 处理学校
    return [school_level_dict[school]]

def process_major(major):
    # 处理专业
    count = 0
    vector = 0
    for w in major:
        if w in w2v.wv:
            vector += w2v.wv.get_vector(w)
            count += 1
    return (vector / count).tolist()
            
def process_gpa(gpa):
    # 处理学术成绩
    return [gpa / 100]

def process_gmat(gmat):
    # 处理gmat
    return [gmat / 346]

def process_gre(gre):
    # 处理gre
    return [gre / 800]


def process_marker(s):
    # 处理其他说明
    research = ['论文', '文章', '会议', '一作', '二作', '三作', '项目', '科研', '课题', '实验室','竞赛', '获奖', '奖项', '大创', '期刊']
    jobs = ['工作', '实习']
    honor = ['奖学金', '国奖', '校奖', '院奖']
    exchange = ['交换']
    
    if type(s) == str:
        research_result = int(sum([(i in s) for i in research])>0)
        jobs_result = int(sum([(i in s) for i in jobs])>0)
        honor_result = int(sum([(i in s) for i in honor])>0)
        exchange_result = int(sum([(i in s) for i in exchange])>0)
        
        return [research_result, jobs_result, honor_result, exchange_result]
    
    return [0,0,0,0]


def process_feature(gpa, gre, gmat, school, ielts, toefl, marker, major):
    """
    提供提取全部特征的函数接口
    """
    feature_list = []
    feature_list += process_gpa(gpa)
    feature_list += process_gre(gre)
    feature_list += process_gmat(gmat)
    feature_list += process_school(school)
    feature_list += process_language(ielts, toefl)
    feature_list += process_marker(marker)
    feature_list += process_major(major)
    
    return feature_list


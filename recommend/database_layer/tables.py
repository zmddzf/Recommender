# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 00:42:35 2020

@author: zmddzf
"""
from . import db

class School_t(db.Model):
    """
    学校表格映射
    """
    __tablename__ = 'school_t'
    __table_args__ = {"extend_existing": True}
    
    code = db.Column(db.INTEGER, primary_key = True)
    cn_name = db.Column(db.String(256))
    en_name = db.Column(db.String(256))
    country = db.Column(db.String(256), index = True)
    
    
class Application_t(db.Model):
    """
    申请人表格映射
    """
    __tablename__ = 'application_t'
    __table_args__ = {"extend_existing": True}
    
    aid = db.Column(db.String(256), primary_key = True)
    bschool = db.Column(db.Float)
    gpa = db.Column(db.Float)
    language_score = db.Column(db.Float)
    gre = db.Column(db.Float)
    gmat = db.Column(db.Float)
    research = db.Column(db.Float)
    jobs = db.Column(db.Float)
    honor = db.Column(db.Float)
    exchange = db.Column(db.Float)
    major_vector = db.Column(db.TEXT)
    score = db.Column(db.Float)

class Offer_t(db.Model):
    """
    offer表格映射
    """
    __tablename__ = 'offer_t'
    __table_args__ = {"extend_existing": True}
    
    offer_id = db.Column(db.INTEGER, primary_key = True)
    aid = db.Column(db.String(256))
    major = db.Column(db.String(256))
    result = db.Column(db.String(128))
    tschool = db.Column(db.String(256))
    school_code = db.Column(db.INTEGER)
    
    
    
    
    
    
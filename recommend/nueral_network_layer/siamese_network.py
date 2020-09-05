# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 14:14:37 2020

@author: zmddzf
"""

import numpy as np
from keras import backend as K
from keras.preprocessing.sequence import pad_sequences
from keras.models import Model
from keras.layers import Input, Dropout, Lambda, Dense
import matplotlib.pyplot as plt
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

def exponent_neg_manhattan_distance(sent_left, sent_right):
    """
    定义Manhattan距离
    :param sent_left: 句子1
    :param sent_right: 句子2
    :return: 曼哈顿距离 
    """
    return K.exp(-K.sum(K.abs(sent_left - sent_right), axis=1, keepdims=True))

def create_manhattan_layer():
    """
    定义Manhattan层
    """
    distance = Lambda(lambda x: exponent_neg_manhattan_distance(x[0], x[1]),
                  output_shape=lambda x: (x[0][0], 1))
    return distance

def create_shared_NN(input_shape):
    """
    定义共享全连接神经网络层
    :param input_shape: 输入形状
    :return: 共享NN
    """
    inputs = Input(shape=input_shape)
    dense1 = Dense(300, activation='tanh')(inputs)
    dense2 = Dense(300, activation='tanh')(dense1)
    dense3 = Dense(128, activation='tanh')(dense2)
    return Model(inputs, dense3)


def build_model(input_shape=109):
    """
    定义Siamese模型
    :param input_shape: 输入的形状
    :return model: 编译好的模型
    """
    left_input = Input(shape=(input_shape,), dtype='float32', name="left_x")
    right_input = Input(shape=(input_shape, ), dtype='float32', name='right_x')
    
    shared_nn = create_shared_NN(input_shape=(input_shape, ))
    
    left_output = shared_nn(left_input)
    right_output = shared_nn(right_input)
    
    distance = Lambda(lambda x: exponent_neg_manhattan_distance(x[0], x[1]),
                      output_shape=lambda x: (x[0][0], 1))([left_output, right_output])
    
    model = Model([left_input, right_input], distance)
    
    model.summary()
    
    model.compile(loss='binary_crossentropy', optimizer='nadam', metrics=['accuracy'])
    return model





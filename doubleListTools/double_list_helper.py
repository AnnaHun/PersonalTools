#!/usr/bin/python
# -*- encoding: utf-8 -*-
"""
    @Author      : 朱昭明 -- apple
    @Project     : PersonalTools
    @File        : double_list_helper.py
    @Software    : PyCharm
    @Create Time : 2020/5/12 4:50 下午    
    @Contact     : 18327510516@163.com
    @License     : (C)Copyright 2020-2022, ZhuGroup-ZB-CASIA
    @version     :  v1.0
    
    @Descriptions: 
  
"""


class Vector2:
    """
        向量
    """
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    # 将函数转移到类中，就是静态方法．
    @staticmethod
    def right():
        return Vector2(0, 1)
    @staticmethod
    def up():
        return Vector2(-1, 0)
    @staticmethod
    def left():
        return Vector2(0, -1)
    @staticmethod
    def down():
        return Vector2(1, 0)
    @staticmethod
    def right_up():
        return Vector2(-1, 1)

class DoubleListHelper:
    """
        二维列表助手类
        定义：在开发过程中，所有对二维列表的常用操作．
    """
    @staticmethod
    def get_elements(list_target, v_pos, v_dir, count):
        result = []
        for i in range(count):
            v_pos.x += v_dir.x
            v_pos.y += v_dir.y
            result.append(list_target[v_pos.x][v_pos.y])
        return result

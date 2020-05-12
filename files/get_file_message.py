#!/usr/bin/python
# -*- encoding: utf-8 -*-
"""
    @Author      : 朱昭明 -- apple
    @Project     : uploadSzoa
    @File        : get_file_message.py
    @Software    : PyCharm
    @Create Time : 2020/5/12 3:15 下午    
    @Contact     : 18327510516@163.com
    @License     : (C)Copyright 2020-2022, ZhuGroup-ZB-CASIA
    @version     :  v1.0
    
    @Descriptions: 此python文件用于日常需求，可以实现对文件相关信息的查询，返回指定格式的文件信息
  
"""

import os

import time
import datetime


def get_all_files_url(url):
    """
    获取指定文件夹下的所有文件路径（递归查询）
    :param url: 指定文件夹
    :return: 所有文件路径
    """
    all_urls = []
    for root, dirs, files in os.walk(url):
        if files is not None:
            for file in files:
                if file is not None:
                    all_urls.append(os.path.join(root, file))
    return all_urls


def time_stamp_to_time(time_stamp):
    """
    时间转换
    :param time_stamp:
    :return:
    """
    time_struct = time.localtime(time_stamp)
    return time.strftime('%Y-%m-%d %H:%M:%S', time_struct)


def get_file_size(file_path):
    """
    获取文件大小
    :param file_path:文件路径
    :return:文件大小---kb
    """
    file_size = os.path.getsize(file_path)
    file_size = file_size / 1024
    return round(file_size, 2)


def get_watch_file_time(file_url):
    """
    获取文件查看时间
    :param file_url:文件路径
    :return:转格式后的时间
    """
    return time_stamp_to_time(os.path.getatime(file_url))


def get_create_file_time(file_url):
    """
    获取文件创建时间
    :param file_url:
    :return:
    """
    return time_stamp_to_time(os.path.getctime(file_url))


def get_change_file_time(file_url):
    """
    获取文件更改时间
    :param file_url:
    :return:
    """
    return time_stamp_to_time(os.path.getmtime(file_url))


if __name__ == '__main__':
    print(get_file_size('/Users/apple/Downloads/test/haha.txt'))
    print(get_create_file_time('/Users/apple/Downloads/test/haha.txt'))
    print(get_change_file_time('/Users/apple/Downloads/test/haha.txt'))

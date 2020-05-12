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
    all_urls = []
    for root, dirs, files in os.walk(url):
        if files is not None:
            for file in files:
                if file is not None:
                    all_urls.append(os.path.join(root, file))
    return all_urls


def time_stamp_to_time(timestamp):
    timeStruct = time.localtime(timestamp)
    return time.strftime('%Y-%m-%d %H:%M:%S', timeStruct)


def get_file_size(filePath):
    fsize = os.path.getsize(filePath)
    fsize = fsize / 1024
    return round(fsize, 2)

def get_watch_file_time(file_url):
    return time_stamp_to_time(os.path.getatime(file_url))


def get_create_file_time(file_url):
    return time_stamp_to_time(os.path.getctime(file_url))


def get_change_file_time(file_url):
    return time_stamp_to_time(os.path.getmtime(file_url))


if __name__ == '__main__':
    print(get_file_size('/Users/apple/Downloads/test/haha.txt'))
    print(get_create_file_time('/Users/apple/Downloads/test/haha.txt'))
    print(get_change_file_time('/Users/apple/Downloads/test/haha.txt'))


#!/usr/bin/python
# -*- encoding: utf-8 -*-
"""
    @Author      : 朱昭明 -- apple
    @Project     : PersonalTools
    @File        : make_socket.py
    @Software    : PyCharm
    @Create Time : 2020/5/12 9:49 下午    
    @Contact     : 18327510516@163.com
    @License     : (C)Copyright 2020-2022, ZhuGroup-ZB-CASIA
    @version     :  v1.0
    
    @Descriptions: 
  
"""

from socket import *


def make_udp_socket():
    """
    创建UDP套接字
        因为UDP套接字无绑定，所以服务端客户端都创建个套接字就可以互相通讯
    :return:
    """

    return socket(AF_INET, SOCK_DGRAM)


def make_tcp_socket():
    """
    创建TCP套接字
        TCP套接字需要绑定ip,所以只需要service创建此套接字就可以
    :return:
    """
    import socket
    return socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def make_broadcast_socket():
    """
    让套接字可以接受广播
    :return:
    """
    return socket(AF_INET, SOCK_DGRAM).setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

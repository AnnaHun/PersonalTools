#!/usr/bin/python
# -*- encoding: utf-8 -*-
"""
@Author      : 朱昭明 -- apple
@Project     : uploadSzoa
@File        : send_or_move_file.py
@Software    : PyCharm
@Create Time : 2020/5/8 9:59 上午
@Contact     : 18327510516@163.com
@License     : (C)Copyright 2020-2022, ZhuGroup-ZB-CASIA
@version     :  v1.0

@Desciption  :

"""

import os
import time
import socket
import paramiko
from scp import SCPClient
import glob
import shutil
import sys


def get_host(url):
    """
    获取host配置文件的相关信息
    :param url: host配置文件位置
    :return: 将host配置文件分解成一个个的集合
    """
    hosts = []
    with open(url, 'r') as f:
        hosts_str = f.readlines()
        for host in hosts_str:
            # 检查配置文件中是否有备注，有备注就跳过
            if host.find("#") != -1:
                continue
            host = host.strip('\n')
            host = host.split(":")
            hosts.append(host)
    return hosts


def get_send_url(url):
    """
    获取发送的jar包信息
    :param url: jar包配置文件
    :return: jar包位置的数组
    """
    jar_urls = []
    with open(url, 'r') as f:
        jar_urls_str = f.readlines()
        for jar_url in jar_urls_str:
            # 检查配置文件中是否有备注，有备注就跳过
            if jar_url.find("#") != -1:
                continue
            jar_url = jar_url.strip('\n')
            jar_urls.append(jar_url)
    return jar_urls


def make_folder(path):
    """
    检查是否存在路径，若不存在则新增
    :param path:检验的路径
    :return:返回路径
    """
    if not os.path.exists(path):
        os.makedirs(path)
    return path


def date_str():
    """
    创建时间str
    :return:返回时间str
    """
    return time.strftime("%Y%m%d%-H%M", time.localtime())


class Host:
    """
    定义基本的host类，一个host代表一个服务器对象
    """

    def __init__(self, ip, user, password):
        """
        :param ip: 对应的ip
        :param user:用户
        :param password:密码
        """
        self.user = user
        self.ip = ip
        self.password = password

    def send_files(self, files, remote_url):
        """
        传送文件的方法
        :param files: 文件路径集合
        :param remote_url: 远程上的位置
        :return:
        """
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(self.ip, username=self.user, password=self.password)
            # sftp = ssh.open_sftp
            scpclient = SCPClient(ssh.get_transport(), socket_timeout=30.0)
            for file in files:
                if file is not None:
                    try:
                        print("start send file:" + file + " to " + self.ip)
                        scpclient.put(file, remote_url)
                        print("send file to " + self.ip + " success")
                    except FileNotFoundError as e:
                        print(e)
                        print("can not find file" + file)
            ssh.close()
        except:
            print("send file failure")


def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()
    return ip


def send_file(hosts):
    print("------------------------------------ start to send file ----------------------------------")
    for host in hosts:
        print("send file to ", host)
        host = Host(host[0], host[1], host[2])
        host.send_files(confs, remote_url)
        print("end to send file to ", host)
    print("************************************ end to send file ************************************")


def move_file():
    print("----------------------------------- start to move file ----------------------------------")
    jar_folder = make_folder('/opt/jenkins/workspace/szoa-cloud/')
    jar_bak_folder = make_folder('/opt/jenkins/workspace/szoa-cloud/bak/' + date_str() + "/")
    file_names = glob.glob('/opt/jenkins/workspace/szoa-cloud/*.jar')
    for file_url in file_names:
        file_name = file_url.split('/')[::-1][0]
        print("start move file:" + file_url + "to " + jar_bak_folder)
        try:
            shutil.move(file_url, jar_bak_folder)
        except:
            print("Failed to copy file: ", sys.exc_info())
        print("move successful:" + file_name)
    print("************************************ end to move file ************************************")


if __name__ == '__main__':
    # 获取本机ip
    local_ip = get_local_ip()
    print(local_ip)
    hosts = get_host("config/host.config")
    confs = get_send_url("config/jar_url.config")
    remote_url = "/opt/jenkins/workspace/szoa-cloud/"
    if local_ip == '192.168.1.35':  # 父服务器ip
        move_file()
        send_file(hosts)
    else:
        move_file()

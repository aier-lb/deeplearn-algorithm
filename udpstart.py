#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/22 上午10:02
# @Author  : Libei
# @Site    :
# @File    : run_start.py.py
# @Software: PyCharm

# 导入日志模块
from algorithm_platform.log.logger import Logger, now_time
# 导入xml模块
from algorithm_platform.config.xml_analysis import xml_analys
# 导入httpserver模块
from algorithm_platform.communicate.comm_server import udpserver
# 导入资源监控模块
from algorithm_platform.log.monitor import resources_monitor
import time
# 导入socket
from socket import *
# 导入json包
import json
# 定义算法模块，加载run文件
from algorithm_platform.alogrithm import run

class platform(udpserver):
    def __init__(self):
        # 加载http模块
        udpserver.__init__(self)
        # 初始化算法模型模块
        self.predict = run.predict()
        # 加载监控模块
        self.monitor_handle = resources_monitor()

    def request_predict(self, content):
        """
        处理请求的逻辑算法
        """
        try:
            # 通过算法模块得到结果
            result = self.predict.prediction(content)
        except EOFError as E:
            result = E
        # 将客户端信息追加在后面，返回给客户端
        for index in content:
            result[index] = content[index]
        # 判断返回值是否是字典
        if type(result) == dict:
            result["connect"] = "predict success"
        else:
            result = {"connect": "predict failed"}
        return result

    def request_resource(self, content):
        """
        获取主机资源监控信息
        """
        # 获取主机资源信息
        result = self.monitor_handle.obtain_computer_info()
        # 将客户端信息追加在后面，返回给客户端
        for index in content:
            result[index] = content[index]
        # 添加状态信息
        result["connect"] = "Test success"
        return result

    def request_test(self, content):
        """
        处理测试请求
        :param content:
        :return:
        """
        result = {}
        for index in content:
            result[index] = content[index]
        result["connect"] = "test success"
        return result

    def main(self, version):
        # 启动服务
        self.upd_server_start(version)

if __name__ == "__main__":
    p = platform()
    version = json.dumps({"日期": "20201023",
                          "版本号": "OCR.P20.S02R.001"})
    p.main(version)
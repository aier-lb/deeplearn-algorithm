#!/usr/bin/python
# -*- coding: utf-8 -*-
# 导入日志模块
# from algorithm_platform.log.logger import Logger, now_time
# # 导入xml模块
# from algorithm_platform.config.xml_analysis import xml_analys
# from algorithm_platform.communicate.comm_server import httpserver
# # 导入资源监控模块
# from algorithm_platform.log.monitor import resources_monitor
# import numpy as np
# import cv2
# import time
# import json
# import random
# import multiprocessing

import requests
import json
#
# class test(httpserver):
#     def __init__(self):
#         # 加载http模块
#         httpserver.__init__(self)
#         self.client_test = True
#         if self.client_test:
#             self.result_content = ["ocr12356", "ocr15623", "ocr25964", "ocr54862", "ocr54215", "ocr56249"]
#         self.monitor_handle = resources_monitor()
#
#     def algorithm_result(self, content):
#         """
#         处理请求的逻辑算法
#         """
#         if self.client_test:
#             index = random.randint(0, len(self.result_content)-1)
#             result_ = self.result_content[index]
#             result = {"state":"predict success",
#                     "recognize_result":str(result_),
#                     "confidence":str(0.7),
#                     "positive":str(0),
#                     }
#             for index in content:
#                 result[index] = content[index]
#         else:
#             result = {"state": "predict success"}
#         return result
#
#     def test_result(self):
#         # 获取主机资源信息
#         result = self.monitor_handle.obtain_computer_info()
#         # 添加状态信息
#         result["state"] = "OK"
#         return result
#
#     def main(self):
#         # 启动服务
#         self.serverstart()
#         # 使用其他进程开启资源监控，由于测试不执行，或会造成堵塞，这里改用调用的方式下发资源信息；
#         self.monitor = multiprocessing.Process(target=self.monitor_handle.run_monitor())
#         self.monitor.start()


if __name__ == "__main__":
    # p = test()
    # p.main()
    # data = {"connect": "predict" ,"img_path": "/home/fpi/algorithm-platform/algorithm_platform/alogrithm/20201013_test/20200928001823_4.png"}
    # data = {"connect": "test", "dsd":"dsads"}
    data = {"connect": "resource", "dsd":"dsads"}
    data = json.dumps(data)

    import socket

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    from socket import *

    udp_socket = socket(AF_INET, SOCK_DGRAM)
    udp_socket.sendto(data.encode(), ("127.0.0.1", 8000))
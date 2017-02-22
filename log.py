# coding: utf-8

"""
本模块的功能主要是输出日志文件信息
"""

import logging

def write(message, type):
    with open("log.txt", "w+") as File:
        File.write(type + ":" + " " + message)

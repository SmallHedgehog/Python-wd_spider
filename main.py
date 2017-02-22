# coding: utf-8

"""
程序入口函数, 支持命令行参数
"""

import argparse
import writing
import db
import sys
import parse
import parsing

# 设置utf-8编码
reload(sys)
sys.setdefaultencoding("utf-8")

arg_parser = argparse.ArgumentParser(usage="\n",
                                     description="this programming aims to grab data from "
                                                 "'http://shuju.wdzj.com/platdata-1.html'")
# 导入数据库
arg_parser.add_argument("-d", default="data", type=str, help="import data into database.")
# 写入文件
arg_parser.add_argument("-f", default="data", type=str, help="write data into file.")

args = arg_parser.parse_args()

# 获取解析数据
# datas = parse.Get()
datas = parsing.Parser_jsonData()

# 如果要求导入数据库
if args.d:
    db.add_data(args.d, datas)
# 如果要求写入文件
if args.f:
    writing.writing(args.f, datas)

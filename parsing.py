# coding: utf-8

"""
由于网贷数据网中的数据是通过JavaScript进行加载的，所以有两种途径来获取数据
1. 通过模拟浏览器来加载数据(Selenium+Phantomjs)，但是效率很低
2. 通过寻找API接口来获取数据
"""

# 本模块是采用通过寻找API接口来获取数据

# API接口url地址，需要构造POST请求
# Form Data:
#   type: 0
#   shujuDate: 2017-02-212017-02-21
# url = "http://shuju.wdzj.com/plat-data-custom.html"

import datetime
import calendar
import requests
import log

# print int(datetime.datetime.now().strftime("%Y-%m-%d").split("-")[-1]) - 1
url = "http://shuju.wdzj.com/plat-data-custom.html"

# 获取当前时间(年月日)的前一天
def get_beforeDay():
    date = datetime.datetime.now().strftime("%Y-%m-%d").split("-")
    # 将当前时间的天数减一
    beforeDay = str(int(date[-1]) - 1)
    # 返回前一天时间
    # 如果beforeDay等于0，则需要获取上个月最后一个的日期
    if beforeDay == "0":
        d = datetime.datetime.now()
        year = d.year
        month = d.month
        # 如果当前月份是一月，则年份减一
        if month == 1:
            month = 12
            year = year - 1
        else:
            month = month - 1
        # 获取上个月的最后一天
        days = calendar.monthrange(year, month)[1]
        return (datetime.datetime(year, month, 1) + datetime.timedelta(days=days)).strftime("%Y-%m-%d")
    return "-".join([date[0], date[1], beforeDay])

# 构造POST请求，获取JSON数据
def Request():
    # POST数据
    data = {
        'type': "0",
        'shujuDate': get_beforeDay() * 2
    }
    try:
        responseJson = requests.post(url, data=data).json()
        return responseJson
    except:
        log.write("Get json data error, requests error.", "Error")
        print "[Error]: Get json data error."
        return None

# 解析JSON数据
def Parser_jsonData():
    JsonData = Request()
    parse_data = []
    for item_dict in JsonData:
        data = {}
        data["platName"] = item_dict["platName"]
        data["amount"] = item_dict["amount"]
        data["bidderNum"] = item_dict["bidderNum"]
        data["borrowerNum"] = item_dict["borrowerNum"]
        data["incomeRate"] = item_dict["incomeRate"]
        data["loanPeriod"] = item_dict["loanPeriod"]
        data["totalLoanNum"] = item_dict["totalLoanNum"]
        data["regCapital"] = item_dict["regCapital"]
        data["fullloanTime"] = item_dict["fullloanTime"]
        data["stayStillOfTotal"] = item_dict["stayStillOfTotal"]
        data["netInflowOfThirty"] = item_dict["netInflowOfThirty"]
        data["top10DueInProportion"] = item_dict["top10DueInProportion"]
        data["avgBidMoney"] = item_dict["avgBidMoney"]
        data["top10StayStillProportion"] = item_dict["top10StayStillProportion"]
        data["avgBorrowMoney"] = item_dict["avgBorrowMoney"]
        data["timeOperation"] = item_dict["timeOperation"]
        data["developZhishu"] = item_dict["developZhishu"]
        parse_data.append(data)
    return parse_data

if __name__ == '__main__':
    parse_data = Parser_jsonData()
    for item_dict in parse_data:
        # noinspection PyTypeChecker
        print item_dict["platName"], item_dict["amount"], item_dict["bidderNum"], item_dict["borrowerNum"],\
            item_dict["incomeRate"], item_dict["loanPeriod"], item_dict["totalLoanNum"], item_dict["regCapital"],\
            item_dict["fullloanTime"], item_dict["stayStillOfTotal"], item_dict["netInflowOfThirty"],\
            item_dict["top10DueInProportion"], item_dict["avgBidMoney"], item_dict["top10StayStillProportion"],\
            item_dict["avgBorrowMoney"], item_dict["timeOperation"], item_dict["developZhishu"]

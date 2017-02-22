# coding: utf-8

"""
本db模块是将数据导入到数据库中, 使用的数据库为sqlite3
"""

import sqlite3

# 建立与数据库的连接
def Connect(database):
    conn = sqlite3.connect(database)
    # 创建表
    cur = conn.execute("""
    CREATE TABLE IF NOT EXISTS parser_data(
    id integer primary key autoincrement, platName text, amount text, bidderNum int, borrowerNum int,
    incomeRate real, loanPeriod real,
    totalLoanNum int, regCapital varchar(40), fullloanTime varchar(40), stayStillOfTotal varchar(40),
    netInflowOfThirty varchar(40), top10DueInProportion real, avgBidMoney varchar(40),
    top10StayStillProportion real, avgBorrowMoney varchar(40), timeOperation varchar(10), developZhishu varchar(10)
    )
    """)

    return cur, conn

# 向数据库中添加数据
def add_data(database, datas):
    if database == "":
        database = "data.sqlite"
    else:
        database = database + ".sqlite"
    result = Connect(database)
    for data in datas:
        result[1].execute("insert into parser_data(platName, amount, bidderNum, borrowerNum, incomeRate, loanPeriod,"
                          "totalLoanNum, regCapital, fullloanTime, stayStillOfTotal, netInflowOfThirty, top10DueInProportion,"
                          "avgBidMoney, top10StayStillProportion, avgBorrowMoney, timeOperation, developZhishu) "
                          "values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (data["platName"], data["amount"],
                                data["bidderNum"], data["borrowerNum"], data["incomeRate"], data["loanPeriod"],
                                data["totalLoanNum"], data["regCapital"], data["fullloanTime"], data["stayStillOfTotal"],
                                data["netInflowOfThirty"], data["top10DueInProportion"], data["avgBidMoney"],
                                data["top10StayStillProportion"], data["avgBorrowMoney"], data["timeOperation"],
                                data["developZhishu"]))
    result[1].commit()
    result[0].close()
    result[1].close()

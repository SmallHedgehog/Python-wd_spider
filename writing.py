# coding: utf-8

"""
将数据写入文件中
"""

def writing(filename, datas):
    """
    :param filename: str
    :param datas: list
    :return:
    """
    if filename == "":
       filename = "data.txt"
    else:
        filename = filename + ".txt"
    with open(filename, 'w') as File:
        File.write("platName" + "\t" + "amount" + "\t" + "bidderNum" + "\t" + "borrowerNum" + "\t" + "incomeRate" + "\t"
                   + "loanPeriod" + "\t" + "totalLoanNum" + "\t" + "regCapital" + "\t" + "fullloanTime" + "\t" +
                   "stayStillOfTotal" + "\t" + "netInflowOfThirty" + "\t" + "top10DueInProportion" + "\t" +
                   "avgBidMoney" + "\t" + "top10StayStillProportion" + "\t" + "avgBorrowMoney" + "\t" + "timeOperation"
                   + "\t" + "developZhishu" + "\n")
        for item_dict in datas:
                File.write(str(item_dict["platName"]) + "\t" + str(item_dict["amount"]) + "\t" + str(item_dict["bidderNum"]) + "\t" +
                           str(item_dict["borrowerNum"]) + "\t" + str(item_dict["incomeRate"]) + "\t" + str(item_dict["loanPeriod"])
                 + "\t" + str(item_dict["totalLoanNum"]) + "\t" + str(item_dict["regCapital"]) + "\t" + str(item_dict["fullloanTime"])
                 + "\t" + str(item_dict["stayStillOfTotal"]) + "\t" + str(item_dict["netInflowOfThirty"]) + "\t" +
                 str(item_dict["top10DueInProportion"]) + "\t" + str(item_dict["avgBidMoney"]) + "\t" + str(item_dict["top10StayStillProportion"])
                 + "\t" + str(item_dict["avgBorrowMoney"]) + "\t" + str(item_dict["timeOperation"]) + "\t" + str(item_dict["developZhishu"])
                 + "\n")

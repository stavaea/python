# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2023/8/2 17:41
# @Author : waxberry
# @File : 大数据收集至excel.py
# @Software : PyCharm

import requests, xlrd, os, sys, urllib3
from datetime import date, timedelta
from xlutils.copy import copy


basedir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(basedir)

from lib.mysqldb import mysqldb
from lib.public_methods import test_login


def collect_data():
    """test_rooms.test_kpi卡片下：adr指标值收集"""
    get_all_code_sql = 'select DISTINCT test_code from test_info WHERE open_flag = 1'
    test_code_all = mysqldb('test_data').selectsql(get_all_code_sql)
    test_code_list = []
    adr_insert_data_list = []
    yesterday = (date.today() + timedelta(days=-1)).strftime('%Y-%m-%d')
    adr_insert_data_list.append(yesterday)
    for j in range(len(test_code_all)):
        test_code_list.append(test_code_all[j]['test_code'])
    for m in range(len(test_code_list)):
        url = 'https://www.baidu.com/test/api/data/query.json'
        header = {
            "Content-Type": "application/json;charset=UTF-8",

            "Cookie": str(test_login())
        }
        param = {
            "code": "test_rooms.test_kpi",

            "page": 1,

            "pageSize": 1000,

            "params": {

                "start_date_year": "2019",

                "start_date_month": "9",

                "start_date_day": "16",

                "end_date_year": "2019",

                "currency_type": "usd",

                "end_date_day": "16",

                "end_date_month": "9",

                "tests": "test_001"

            }

        }

        """替换请求参数中的开始日期"""
        param['params']['start_date_year'] = str(yesterday).split('-')[0]
        param['params']['start_date_mouth'] = str(yesterday).split('-')[1]
        param['params']['start_date_day'] = str(yesterday).split('-')[2]
        """替换请求参数中的结束日期"""
        param["params"]["end_date_year"] = param['params']['start_date_year']
        param["params"]["end_date_mouth"] = param['params']['start_date_mouth']
        param["params"]["end_date_day"] = param['params']['start_date_day']
        param['params']['tests'] = test_code_list[m]
        urllib3.disable_warnings()
        result = requests.post(url=url, headers=header, json=param, verify=False).json()
        if str(result['data']['data']) != None:
            """adr指标值收集"""
            indicatorList = result["data"]["data"]['test_indicator_list']
            test_actualorLast_Forecast = result['data']['data']['test_actual']
            new_indicator_actualvalue = {}
            i = 0
            while i < len(indicatorList):
                dic = {indicatorList[i]: test_actualorLast_Forecast[i]}
                new_indicator_actualvalue.update(dic)
                i += 1
            if str(new_indicator_actualvalue['adr']) == '--':
                adr_value_result = 'NA'
                adr_insert_data_list.append(adr_value_result)
            else:
                adr_value_result = new_indicator_actualvalue['adr']
                adr_insert_data_list.append(adr_value_result)
        else:
            adr_value_result = 'NA'
            adr_insert_data_list.append(adr_value_result)
    """adr指标值数据收集入excel路径"""
    workbook = xlrd.open_workbook(basedir + '/collect_data_center.xls')#打开工作薄
    sheets = workbook.sheet_names()# 获取工作簿中的所有表格
    worksheet = workbook.sheet_by_name(sheets[0])# 获取工作簿中所有表格中的的第一个表格
    rows_old = worksheet.nrows# 获取表格中已存在的数据的行数
    new_workbook = copy(workbook)# 将xlrd对象拷贝转化为xlwt对象
    new_worksheet = new_workbook.get_sheet(0)# 获取转化后工作簿中的第一个表格
    for i in range(0, 1):
        for j in range(0, len(adr_insert_data_list[i])):
            new_worksheet.write(i + rows_old, j, [adr_insert_data_list][i][j])# 追加写入数据，注意是从i+rows_old行开始写入
    new_workbook.save(basedir + '/collect_data_center.xls')# 保存工作簿
    print('adr指标值---xls格式表格【追加】写入数据成功')
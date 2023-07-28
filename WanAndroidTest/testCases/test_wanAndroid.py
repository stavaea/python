# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2023/7/26 11:58
# @Author : waxberry
# @File : test_wanAndroid.py
# @Software : PyCharm

import json
import pytest
import allure
from base.base_requests import BaseRequests
from utils.handle_logger import logger
from utils.handle_excel import HandleExcel
from utils.param_replace import pr
from utils.handle_cookies import get_cookies

handler_excel = HandleExcel()
get_excel_data = HandleExcel().get_excel_data()
ID = ''
COOKIES = {}
PAGES = ''

class TestWanAndroid:

    @pytest.mark.parametrize('case', get_excel_data)
    def test_wanAndroid(self, case):
        global ID
        global COOKIES
        # 参数替换
        case['url'] = pr.relevant_parameter(case['url'], '${collect_id}', str(ID))

        if case['is_run'].lower() == 'yes':
            logger.info('------执行用例的id为：{0}，用例标题为：{1}------'.format(case['case_id'], case['title']))
            res = BaseRequests(case, cookies=COOKIES).get_response()
            res_json = res.json()

            # 获取登录后的cookies
            if case['case_id'] == 3:
                COOKIES = get_cookies.get_cookies(res)

            if case['is_depend']:
                try:
                    ID = res_json['data']['id']
                    # 将使用的参数化后的数据写入excel
                    handler_excel.rewrite_value('id={}'.format(ID), case['case_id'], 'depend_param')
                except Exception as e:
                    logger.error(f'获取id失败，错误信息为：{e}')
                    ID = 0

            # 制作allure报告
            allure.dynamic.title(case['title'])
            allure.dynamic.description('<font color="red">请求URL：</font>{}<br />'
                                        '<font color="red">期望值：</font>{}'.format(case['url'], case['excepted']))
            allure.dynamic.feature(case['module'])
            allure.dynamic.story(case['method'])

            result = ''
            try:
                assert eval(case['excepted'])['errorCode'] == res_json['errorCode']
                result = 'pass'
            except AssertionError as e:
                logger.error('Assert Error:{0}'.format(e))
                result = 'fail'
                raise e
            finally:
                # 将实际结果格式化写入excel
                handler_excel.rewrite_value(json.dumps(res_json, ensure_ascii=False, indent=2, sort_keys=True), case['case_id'], 'actual')
                # 将用例执行结果写入excel
                handler_excel.rewrite_value(result, case['case_id'], 'test_result')

    def test_get_articleList(self):
        '''翻页，将page参数化'''
        global PAGE
        pass

    def test_mock_demo(self):
        '''使用mock服务模拟服务器响应'''
        pass

if __name__ == '__main__':
    pytest.main(['-q', 'test_wanAndroid.py'])
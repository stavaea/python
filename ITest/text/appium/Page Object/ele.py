#coding:utf-8

import os
import select, time

class Page(object):

    def set_values_by_h5(self, html_dic, value_dic):
        '''给webview页面元素批量赋值
        Args:
            html_dic(dict):webview元素控件定位组成的字典
            value_dic(dict):输入的值组成的字典
        '''
        for key in html_dic:
            if key in value_dic:
                html_list = html_dic[key].split('|')
                html_type = html_list[1]
                html_value = html_list[0]
                ele = self.find_element(html_type, html_value)
                self.sendkeys_by_h5(ele, value_dic[key])
            else:
                self.logger.error('要输入的值字典中没有这个｛｝字段'.format(key))
                print ('要输入的值字典中没有这个｛｝字段'.format(key))

    def sendkeys_by_h5(self, ele, value):
        '''给webview页面根据控件元素标签类型输入值
        Args:
            ele(webElement):页面控件元素对象
            value(str):页面控件元素要输入的值
        '''
        tag_name = ele.tag_name
        if tag_name == 'input':
            input_type = ele.get_attribute('type')
            if input_type == 'text' or 'password':
                self._send_keys(ele, value)
            elif input_type == 'radio':
                self._select_radio(ele)
            elif input_type == 'checkbox':
                self._select_checkbox(ele)
        elif tag_name == 'select':
            self._select_select(ele, value)
        elif tag_name == 'textarea':
            self._send_keys(ele, value)
        elif tag_name == 'file':
            # 图片路径分隔符处理
            value = value.replace('/', os.path.sep)
            value = value.replace('\\', os.path.sep)
            # 相对路径处理
            if not os.path.exists(value):
                value = image_dir + value
            value = os.path.realpath(value)
        ele.send_keys(value)

    def _select_radio(self, ele):
        '''点击webview页面元素中的单选按钮
        Args:
            ele(webElement):单选按钮控件元素对象
        '''
        r = ele.is_selected()
        if not r:
            ele.click()

    def _select_checkbox(self, ele):
        '''点击webview页面元素中的多选按钮
        Args:
            ele(webElement):多选按钮控件元素中的单一选项对象
        '''
        r = ele.is_selected()
        if not r:
            ele.click()

    def _select_select(self, ele, value):
        '''点击webview页面元素中的选择框
        Args:
            ele(webElement):多选控件元素对象
            value(str):选择的文本值
        '''
        s = select(ele)
        s.select_by_visible_text(value)

    def test1(self):
        '''新建抽奖活动'''
        self._loginStatusPage('抽奖管理')
        time.sleep(1)
        f.clickByXpath(self.driver, cfg.getCaseHtmlValue('html', '新建奖品', self.caseDataPath))
        f.setValues(self.driver, cfg.getCaseValueDic('html', '新建奖品', self.caseDataPath),
                    cfg.getCaseValueDic('奖品设置1', self.caseDataPath))
        f.setValues(self.driver, cfg.getCaseValueDic('html', '新建奖品', self.caseDataPath),
                    cfg.getCaseValueDic('奖品设置2', self.caseDataPath))
        f.setValues(self.driver, cfg.getCaseValueDic('html', '新建奖品', self.caseDataPath),
                    cfg.getCaseValueDic('奖品设置3', self.caseDataPath))
        f.setValues(self.driver, cfg.getCaseValueDic('概率', self.caseDataPath),
                    cfg.getCaseValueDic('概率', self.caseDataPath))
        f.clickByXpath(self.driver, cfg.getCaseHtmlValue('html', '保存', self.caseDataPath))
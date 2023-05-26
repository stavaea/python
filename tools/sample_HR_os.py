# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2023/5/5 17:37
# @Author : waxberry
# @File : sample_HR_os.py
# @Software : PyCharm

import streamlit as st
import pandas as pd

# 创建员工类
class Employee:
    def __init__(self, name, age, position):
        self.name = name
        self.age = age
        self.position = position

# 创建员工列表
employee_list = []

# 添加员工函数
def add_employee(name, age, position):
    employee = Employee(name, age, position)
    employee_list.append(employee)

# 显示员工列表函数
def show_employee_list():
    if len(employee_list) == 0:
        st.write('员工列表为空')
    else:
        df = pd.DataFrame([[e.name, e.age, e.position] for e in employee_list], columns=['姓名', '年龄', '职位'])
        st.dataframe(df)

# 添加员工界面
def add_employee_page():
    st.write('添加新员工')
    name = st.text_input('姓名')
    age = st.number_input('年龄', min_value=0, max_value=100)
    position = st.text_input('职位')
    if st.button('添加'):
        add_employee(name, age, position)
        st.success('添加成功！')

# 显示员工列表界面
def show_employee_list_page():
    st.write('员工列表')
    show_employee_list()

# 主程序
def main():
    st.title('人事系统')
    menu = ['添加员工', '员工列表']
    choice = st.sidebar.selectbox('选择菜单', menu)
    if choice == '添加员工':
        add_employee_page()
    elif choice == '员工列表':
        show_employee_list_page()

if __name__ == '__main__':
    main()
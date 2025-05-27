# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2025/5/26 14:13
# @Author : waxberry
# @File : employee_tools.py
# @Software : PyCharm


# 存储所有的员工信息，空数据时
# employee_dict = {}

# 这是原本就有固定数据时的字典
employee_dict = {'1001': {'name':'张三','sex':'男','salary':'5000'},
                 '1002': {'name':'李四','sex':'男','salary':'7000'},
                 '1003': {'name':'小红','sex':'女','salary':'9000'},
                 }

def show_menu():
    """进入菜单页面"""
    print("*"*11+"员工管理系统 V_1.0"+"*"*11)
    # print("员工管理系统 V1.0")
    print("1、添加员工信息")
    print("2、修改员工信息")
    print("3、删除员工信息")
    print("4、显示所有员工信息")
    print("5、退出系统")
    print("*"*40)

def add_info():
    """添加员工信息"""
    # 实现步骤：1.输入员工的工号、姓名、性别、工资等等
    #           1.1判断员工编号是否存在，如果存在则拒绝添加，提示“编号已存在，不能重复添加”
    #           1.2如果不重复，则继续接下来的操作
    #         2.把这些信息保存在一个字典里
    #           2.1员工工号作为键，剩下的属性(姓名、性别、工资)作为值
    #           2.2类似： '1001' ｛'name':xxx, 'sex':xxx, 'salary':xxx｝
    #         3.提示添加成功
    print("添加员工===>")
    employ_id = input("请输入要添加员工的工号：")
    # 先找到所有的字典的键，再将这些键转化为列表的形式
    all_id = list(employee_dict.keys())
    if employ_id in all_id:
        print("员工工号已存在，不能重复添加！！！")
        return
    employ_name = input("请输入要添加员工的姓名：")
    employ_sex = input("请输入要添加员工的性别：")
    employ_salary = input("请输入要添加员工的工资：")
    # 把这些信息保存在一个字典里
    info_dict = {"name": employ_name,"sex": employ_sex,"salary": employ_salary}
    # 再放在大字典里，怎么放，根据id号相对应
    employee_dict[employ_id] = info_dict
    print("工号为 %s 的员工信息添加成功！！！" % employ_id)
    # 这里只是起到打印观察的作用，可注释掉下面这一行
    # 说明仅仅还是放在字典里面，毕竟输出是字典形式，怎么显示那是第四个功能该做的事
    # print(employee_dict)  # {'1001': {'name': '张三', 'sex': '男', 'salary': '5000'}｝


def update_info():
    """修改员工信息"""
    print("修改员工===>")
    # 实现步骤 1.拿到要修改员工的工号
    #           1.1如果工号不存在，则提示错误信息，终止函数执行，返回
    #           1.2如果存在，则修改对应的信息
    #               1.2.1 显示原来的信息再修改
    #         2.因为并不是所有的信息都需要修改，万一不需要修改的怎么办？如何简化使用操作？
    #           2.1判断修改时输入的是不是惟恐，为空就保持不变，不为空则说明修改了
    employ_id = input("请输入你要修改的员工的工号：")
    all_id = list(employee_dict.keys())
    if employ_id not in all_id:
        print("该员工工号不存在，不能进行修改!!!")
        return
    new_name = input("姓名是：%s   修改后的姓名：" % employee_dict[employ_id]['name'])
    new_sex = input("性别是：%s   修改后的性别：" % employee_dict[employ_id]['sex'])
    new_salary = input("工资是：%s   修改后的工资：" % employee_dict[employ_id]['salary'])
    # 因为并不是所有的信息都需要修改，万一不需要修改的怎么办？如何简化使用操作？
    if new_name !="":
        employee_dict[employ_id]['name'] = new_name
    if new_sex !="":
        employee_dict[employ_id]['sex'] = new_sex
    if new_salary !="":
        employee_dict[employ_id]['salary'] = new_salary
    print("工号为 %s 的员工信息修改成功！！！" % employ_id)

def delete_info():
    """删除员工信息"""
    print("删除员工===>")
    # 实现步骤：1.输入要删除员工的工号
    #         2.判断工号是否存在，不存在就给出提示信息，终止函数执行
    #         3.如果存在，则直接删除
    employ_id = input("请输入你要删除的员工的工号：")
    all_id = list(employee_dict.keys())
    if employ_id not in all_id:
        print("该员工工号不存在，不能进行删除!!!")
        return
    else:
        # 直接删除这个字典
        del employee_dict[employ_id]
    print("工号为 %s 的员工信息删除成功！！！" % employ_id)

def show_all_info():
    """显示员工信息"""
    print("显示所有员工信息===>")
    # 实现步骤：1.判断员工是否存在，如果不存在则提示返回
    #           1.1怎么判断？当列表长度为0时，则说明不存在
    #         2.如果存在，就打印表头
    #         3.打印分割线
    #         4.遍历员工信息，依次输出字典信息

    # 判断员工是否存在
    if len(list(employee_dict.keys())) == 0:
        print("当前没有任何的员工信息，请先选择操作 1，添加员工！！！")
        # return 下方的代码不会被执行
        return
    # 打印表头
    print("-" * 40)
    for people in["工号", "姓名", "性别", "工资"]:
        print(people, end="\t\t")
    # 打印分割线
    # 增加换行
    print("")
    print("-" * 40)
    # 遍历员工信息，依次输出字典信息
    # 这个items方法是把字典转换成列表的方法，须特别注意
    for jober in employee_dict.items():
        print("%s\t\t%s\t\t%s\t\t\t%s" % (jober[0],
                                          jober[1]['name'],
                                          jober[1]['sex'],
                                          jober[1]['salary']))
    print("-" * 40)
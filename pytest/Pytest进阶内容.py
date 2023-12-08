# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2023/12/8 11:37
# @Author : waxberry
# @File : Pytest进阶内容.py
# @Software : PyCharm


# 最后我们再来讲解一些pytest比较关键性的一些进阶内容
#
# Allure效果美化
# 我们在使用Pytest所生成的页面往往不够美观且展示信息杂乱不好分析，所以我们通常搭载allure来实现界面美化：
#     Allure框架是一个灵活轻量级多语言测试报告工具
#     它不仅可以以WEB的方式展示简介的测试结果，而且允许参与开发过程的每个人从日常执行的测试中最大限度的提取有用信息
#
# 下面我们就来学习如何安装使用allure：

# 首先我们需要去下载在电脑上下载allure并配置好环境变量
# 我们这里给出官网下载地址：https://github.com/allure-framework/allure2/releases
# 温馨提醒：下载链接在github上，如果无法打开可以刷新重试或者使用加速器梯子等辅助工具
# 环境变量的配置只需要将bin文件所在目录放在电脑的Path路径下即可，这里不再展示

# 第二步我们需要在pycharm上下载allure-pytest插件（如果之前pip了那个整体文件，这里应该是已经下载过了）
pip install allure - pytest

# 第三步我们就可以直接来生成allure的测试结果展示界面了

# 1.我们通常首先需要生成一个allure临时Json文件
# 我们通常会加上这么一串"‐‐alluredir=./temps ‐‐clean‐alluredir"
# ‐‐alluredir = 文件生成地址 ： 表示我们将allure临时文件生成在我们所指定的相对临时目录下
# ‐‐clean‐alluredir ： 由于每次都会生成大量文件，所以我们会在生成前清除当前目录下的allure文件，保证我们数据都是最新数据

# 2.我们需要依靠临时文件来生成allure.html网页
# 我们通常在main方法中执行
if __name__ == '__main__':
    # 正常运行
    pytest.main()
    # 休眠：主要为了JSON临时文件的生成
    time.sleep(3)
    # allure generate 固定语句 + allure临时JSON文件目录 + -o 输出指令 + allure.html生成文件目录 + --clean 清除旧数据
    os.system("allure generate ./temps ‐o ./reports ‐‐clean")


# Parametrize数据驱动
# 我们通常会采用Parametrize注解来进行数据驱动，下面我们来详细讲解一下：

# 格式：@pytest.mark.parametrize(参数名称，参数值)
# 意义：我们会将参数名称作为id，然后根据参数值的个数去依次调用，存在n个参数值，我们将会调用n次case

# 1.参数值为列表或元组时，参数名称可以为一个
# 首先我们这里因为使用单个元素的列表（元组），我们的参数名可以为一个
@pytest.mark.parametrize('caseinfo', ['胡桃', '胡桃宝宝', '芙芙'，'芙芙宝宝'])

# 在方法参数里，我们需要调用parametrize的参数名称caseinfo，需要保证一模一样
def test_01_get_token(self, caseinfo):
    # 在这里我们可以借助参数名称caseinfo来代替列表中的元素
    # 列表中存在几个，我们该方法将执行几次，例如现在列表是四个元素，那么我们方法将会重复执行四次并每次按顺序赋值不同的元素
    print("获取统一接口鉴权码：" + caseinfo)


# 2.参数值为列表的多个时，参数名称可以为多个
# 这里我们列表中嵌套了一个列表，如果我们是单参数名称，那么输出时就会将第一个列表['胡桃厨','胡桃宝宝']输出出去
# 但是如果我们是多参数名称，系统会自动将第一个列表的元素分开赋值给arg1，arg2便于我们分开使用，个人还是比较推荐的
@pytest.mark.parametrize('arg1,arg2', [['胡桃厨', '胡桃宝宝'], ['芙芙厨', '芙芙宝宝']])
# 注意：这里当然也需要和参数名称对应！！！
def test_01_get_token(self, arg1, arg2):
    print("获取统一接口鉴权码：" + str(arg1) + " " + str(arg2))


# 我们在进行数据驱动时通常会结合Yaml文件来进行数据获取，这里我们简单介绍一下Yaml文件：

# yaml是一种数据格式，扩展名可以是yaml,yml
# 支持#注释，通过缩进表示层级，区分大小写，且yaml文件最后获取的结果展示是一个字典列表格式
# yaml文件经常用于书写配置，例如Java的Spring中的配置文件，而我们也经常采用yaml编写自动化测试用例

# yaml文件通常会出现两种格式

# 字典格式：如果我们正常书写yaml文件，如下就是字典模式
# name: 胡桃

# 列表模式：如果我们采用yaml中的列表，那么我们在py获取时也将获得列表
msjy:
    # - name1: 胡桃
    # - name2: 芙芙
    # - ages1: 18
    # - ages2: 19
# 我们也可以利用这个特性，直接在yaml中做多个列表，来多次提取
-
        name: 'xxx'
    age: 18
-
        name: 'xxx'
    age: 20

# 我们这里首先给出一个解析yaml文件的示例函数：
import os.path
import yaml


# 这里是获取当前路径，因为我们需要找到对应的yaml文件，那么具体路径就需要我们进行拼接
def get_obj_path():
    # 这里我们使用了Python的os类来进行当前路径获取，最后返回结果其实是一个String字符串
    # 我们以'common'作为分界（common是当前文件夹的名称，我们将该Str进行划分，获取前面的部分），获取到前面的路径部分来进行拼接
    return os.path.dirname(__file__).split('common')[0]


# 然后我们这里定义一个方法来解析yaml文件
def read_yaml(yamlPath):
    with open(get_obj_path() + yamlPath, mode='r', encoding='utf-8') as f:
        # 这里需要我们pip install pyyaml
        value = yaml.load(steam=f, Loader=yaml.FullLoader)
        return value


# 然后我们这里采用一个main方法来执行上述用例（其实应该在其他测试类中执行）
if __name__ = '__main__':
    # 调用read_yaml方法并给出yaml路径
    print(read_yaml('testcase/user_manage/get_token.yaml'))


# 了解了所有东西之前我们就可以结合之前的Parametrize来进行操作：
# 我们这里将所需要的数据变为read_yaml读取的yaml文件内容
@pytest.mark.parametrize('caseinfo', read_yaml('testcase/user_manage/get_token.yaml'))
def test_01_get_token(self, caseinfo):
    # 这里我们就可以获取到yaml文件内容并输出了
    print("获取统一接口鉴权码：" + caseinfo)


# 当然如果我们了解我们的yaml中拥有什么元素，我们还可以采用[]的方式具体表达出来
@pytest.mark.parametrize('caseinfo', read_yaml('testcase/user_manage/get_token.yaml'))
def test_01_get_token(self, caseinfo):
    print("获取统一接口鉴权码：")
    # 这里我们可以直接获取namekey对应的value
    print("caseinfo[name]：" + caseinfo['name'])
    # 这里我们可以分别获取request层下的method，url，data分别对应的value
    print("caseinfo[name]：" + caseinfo['request']['method'])
    print("caseinfo[name]：" + caseinfo['request']['url'])
    print("caseinfo[name]：" + caseinfo['request']['data'])
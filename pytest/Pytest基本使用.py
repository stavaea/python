# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2023/12/8 11:29
# @Author : waxberry
# @File : Pytest基本使用.py
# @Software : PyCharm


# Pytest默认测试用例
# 下面我们首先讲解Pytest默认测试用例的格式：

# 首先我们的模块名（文件名）通常被统一存放在一个testcases文件夹中，然后需要保证模块名须以test_开头或者_test结尾
# 例如我们下面的模块名命名就是正确示例
# test_demo1
# demo2_test


# 然后我们需要注意我们模块中的测试类类名必须以Test开头，并且不能带有init方法
# 例如我们下面的类名命名就是正确示例
class TestDemo1:
class TestLogin:


# 最后我们需要注意我们测试类中的测试方法名（Case名）必须以test_开头
# 例如我们下面的模块名命名就是正确示例
# test_demo1(self)
# test_demo2(self)


# 我们给出一个测试用例例子：
# 文件名为test_demo1
class TestDemo:
    def test_demo1(self):
        print("测试用例1")

    def test_demo2(self):
        print("测试用例2")


# 当然我们上述的要求都不是必须相同的，在后续我们可以进行修改，我们将在下述讲解执行方法时讲解
# 然后我们再来讲解一下Pytest的测试用例该如何执行：

# 首先我们讲解一下全局配置文件pytest.ini
# 我们可以在pytest.ini中进行一些属性的配置来修改Pytest的默认属性，我们需要在项目的根目录下创建，名称必须是pytest.ini

# 1[pytest]
2  # 参数
# 3addopts = ‐vs  # 这里指当默认使用指令时的一些辅助参数，我们后面会讲解
# 4testpaths =./ testcases  # 这里指默认的执行路径，它会默认执行该文件夹下所有的满足条件的测试case
# 5python_files = test_ *.py  # 这里就是前面我们所说的文件命名规则
# 6python_classes = Test *  # 这里就是前面我们所说的类名命名规则
# 7python_functions = test_ *  # 这里就是前面我们所说的Case命名规则
# 8  # 标记
# 9markers =  # 这里是冒烟规则，我们后面会讲到
# 10smoke: 冒烟用例
# 11product_manage: 商品管理

# 然后我们首先来讲采用console命令行执行Pytest的方法
# 最简单的就是直接在console命令行输入pytest，如果存在pytest.ini，它会根据文件内容进行执行；如果没有就按照默认格式执行
# 但是我们可以通过一些参数来强化pytest参数指令

# -vs： -v输出详细信息 -s输出调试信息
# pytest - vs
#
# # -n： 多线程运行（前提安装插件：pytest-xdist）
# pytest - vs - n = 2
#
# # --reruns num: 失败重跑（前提安装插件：pytest-rerunfailres）
# pytest - vs - -reruns = 2
#
# # -x: 出现一个用例失败则停止测试
# pytest - vs - x
#
# # --maxfail: 出现几个失败才终止
# pytest - vs - -maxfail = 2
#
# # --html: 生成html的测试报告,后面 需要跟上所创建的文件位置及文件名称（前提安装插件：pytest-html）
# pytest - vs - -html. / reports / result.html

# -k： 运行测试用例名称中包含某个字符串的测试用例，我们可以采用or表示或者，采用and表示都
# 采用or就表示：我们的运行用例名称中包含or两侧的其中一个数据即可
# 采用and就表示：我们的运行用例名称中包含and两侧的所有数据才满足条件
# pytest - vs - k "qiuluo"
# pytest - vs - k "qiuluo or weiliang"
# pytest - vs - k "qiuluo and weiliang"


# -m：冒烟用例执行，后面需要跟一个冒烟名称
# 我们在这里简单介绍一下冒烟用例的执行方法，我们这里其实就是一个分组执行的方法
# 例如我们的用例划分为user_manage用户管理测试和product_manage商品管理测试，我们只希望执行其中一组测试

# 首先我们需要在他们的不同方法上进行@mark划分，具体操作如下：
class TestDemo:

    # 我们在Case上采用@pytest.mark. + 分组名称，就相当于该方法被划分为该分组中
    # 注意：一个分组可以有多个方法，一个方法也可以被划分到多个分组中
    @pytest.mark.user_manage
    def test_demo1(self):
        print("user_manage_test1")

    @pytest.mark.product_manage
    def test_demo2(self):
        print("product_manage_test1")

    @pytest.mark.user_manage
    @pytest.mark.product_manage
    def test_demo3(self):
        print("manage_test1")


# 我们在执行中只需要采用前面我们所说的-m + 分组名称即可
# pytest - vs - m user_manage

# 这里插一句，我们在运行过程中可以采用抛出异常的方式来模拟测试失败：raise Exception() 抛出异常


# 最后我们也可以采用main方法来执行pytest，同样我们也可以使用参数来进行调节
if __name__ == '__main__':
    pytest.main()

if __name__ == '__main__':
    pytest.main(["‐vs"])
# 最后我们插入一个简单的案例跳过方法：

# pytest的跳过案例方法其实和unittest是完全相同的
# 我们只需要采用skip或skipif方法来指定参数并贴在方法上即可跳过

# @pytest.mark.skip(跳过原因)

# @pytest.mark.skipif(跳过条件,跳过原因)

# 我们给出一个示例
class TestDemo:
    workage2 = 5
    workage3 = 20

    @pytest.mark.skip(reason="无理由跳过")
    def test_demo1(self):
        print("我被跳过了")

    @pytest.mark.skipif(workage2 < 10, reason="工作经验少于10年跳过")
    def test_demo2(self):
        print("由于经验不足，我被跳过了")

    @pytest.mark.skipif(workage3 < 10, reason="工作经验少于10年跳过")
    def test_demo3(self):
        print("由于经验过关，我被执行了")

    def test_demo3(self):
        print("我没有跳过条件，所以我被执行了")
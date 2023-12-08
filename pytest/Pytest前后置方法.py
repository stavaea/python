# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2023/12/8 11:32
# @Author : waxberry
# @File : Pytest前后置方法.py
# @Software : PyCharm


# 首先我们需要先了解前后置是什么：
#     前后置就是针对不同层级方法执行前和执行后所需要执行的步骤进行封装并执行
#     这个层级通常被划分为：文件层，类层，方法层

# 首先我们先来介绍Pytest通过固件来实现前后置的方法：

# 我们通常采用前后置来做一些方法前后的操作
# 如果我们采用方法层的前后置，那么它会在每个方法执行前后去执行该内容
# 如果我们采用类层的前后置，那么它会在调用这个类内所有方法的前后去执行该内容，但是无论该类的方法执行多少次，它只会调用一次
# 例如我们做login测试时，我们只需要在开始测试时打开一次浏览器，然后在测试结束时关闭一次浏览器，那么我们就采用类的前后置
# 我们做login测试时，为了保证前置操作不对后续Case有影响，所以我们在执行方法前打开该网页，执行方法后关闭该网页，采用方法的前后置

# Pytest的固件前后置其实和unittest是基本相同的
# 首先是方法级别的固件前后置
# 它是在每个测试方法(用例代码) 执行前后都会自动调用的结构
# 方法执行之前
def setUp(self):
    # 每个测试方法执行之前都会执行
    pass


# 方法执行之后
def tearDown(self):
    # 每个测试方法执行之后都会执行
    pass


# 然后是针对类级别的固件前后置
# 它是在每个测试类中所有方法执行前后 都会自动调用的结构(在整个类中执行之前或之后执行一次)
# 需要注意：类级别的固件前后置, 是一个类方法
# 类中所有方法之前
@classmethod
def setUpClass(cls):
    pass

    # 类中所有方法之后
    @classmethod
    def tearDownClass(cls):
        pass

    # 最后是针对模块级别的固件前后置
    # 在每个代码文件执行前后执行的代码结构
    # 需要注意：模块级别的需要写在类的外边直接定义函数即可
    # 代码文件之前
    def setUpModule():
        pass

    # 代码文件之后
    def tearDownModule():
        pass


# 下面我们采用一个用户账户登录的用例来简单展示一下固件前后置
import unittest

class TestLogin(unittest.TestCase):

    # 在执行该类前所需要调用的方法
    @classmethod
    def setUpClass(cls) -> None:
        print('------打开浏览器')

    # 在执行该类后所需要调用的方法
    @classmethod
    def tearDownClass(cls) -> None:
        print('------关闭浏览器')

    # 每个测试方法执行之前都会先调用的方法
    def setUp(self):
        print('输入网址......')

    # 每个测试方法执行之后都会调用的方法
    def tearDown(self) -> None:
        print('关闭当前页面......')

    # 测试Case1
    def test_1(self):
        print('输入正确用户名密码验证码,点击登录 1')

    # 测试Case2
    def test_2(self):
        print('输入错误用户名密码验证码,点击登录 2')


# 然后我们还需要讲解一下Fixtrue实现前后置的方法：

# 首先我们需要知道Fixtrue所实现的功能基本和固件所实现的功能是一样的，但是会更加方便
# 首先我们给出Fixture的完整格式，然后我们再分开介绍各个参数
@pytest.fixture(scope=None, autouse=False, params=None, ids=None, name=None)
# scope：作用范围
# 参数主要有三种：function函数，class类，package/session包

# function：在函数层面上执行前后置
# 我们通常采用yield进行前后置划分，yield前是前置，yield后是后置
@pytest.fixture(scope="function")
def exe_database_sql():
    print("执行SQL查询")
    yield
    print("关闭数据库连接")


# 我们还可以通过yield或return去返回一些参数在方法中使用
# 但是需要注意，yield返回参数后后置仍旧可以执行，但是return返回参数后后置操作无法执行
@pytest.fixture(scope="function")
def exe_database_sql():
    print("执行SQL查询")
    yield "success"
    # return "success" 执行后无法执行后置操作
    print("关闭数据库连接")


# 我们的方法在调用时，可以直接使用exe_database_sql表示返回信息进行输出
def test_2(self，exe_database_sql):
    print(exe_database_sql)


# class：在类之前和之后执行
@pytest.fixture(scope="class")
def exe_database_sql():
    print("执行SQL查询")
    yield
    print("关闭数据库连接")


# package/session：在整个项目会话之前和之后执行
@pytest.fixture(scope="session")
def exe_database_sql():
    print("执行SQL查询")
    yield
    print("关闭数据库连接")


# autouse:是否自动启动
# 该参数默认为False，我们可以将其修改为True
# 该参数的功能主要在判断该固件是否在自定义范围内可以自动启动
# 若自动启动，则所有方法在执行时都会自动执行该前后置；但若为False，则我们需要手动启动

# 首先如果是自动启动，则我们无需关心任何参数，我们的所有方法都会自动调用
@pytest.fixture(scope="function"，autoues = True)

def exe_database_sql():
    print("执行SQL查询")
    yield
    print("关闭数据库连接")


# 但若是关闭自动启动，我们在不同的scope下有不同的调用方法
@pytest.fixture(scope="function"，autoues = Flase)

def exe_database_sql():
    print("执行SQL查询")
    yield
    print("关闭数据库连接")


# scope = function：我们需要在方法后加上该Fixture方法名
def test_2(self，exe_database_sql):
print(exe_database_sql)


# scope = class：我们需要在对应的类上添加@pytest.mark.usefixtures("exe_database_sql")装饰器调用
@pytest.mark.usefixtures("exe_database_sql")
class TestDemo:
    pass


# scope = session:.一般会结合conftest.py文件来实现,我们后面再介绍

# 还需要注意autouse仅限于在自己的类中使用上述方法，如果要跨类使用，那么我们也需要在conftest.py中配置


# params:实现参数化配置
# 通常我们的脚本都是根据导出的yaml文件进行属性填充，针对参数化我们后面再讲，我们先将Fixture的参数化
# params通常后面跟上具体的数据(列表，元组等)，然后我们在调用时有固定的写法
# 首先我们需要在Fixture方法参数中定义一个request，然后使用request.param来使用我们传递的params数据
class TestDemo:
    def read_yaml():
        return ["胡桃", "胡桃宝宝", "胡桃厨"]

    # 首先我们的参数需要获取数据：params=read_yaml()
    @pytest.fixture(scope="function", autouse=False, params=read_yaml())
    # 然后我们的Fixture方法需要一个request参数
    def exe_database_sql(request):
        print("执行SQL查询")

    # 我们通过request.param获取数据，可以采用yield返回该数据
    yield request.param
    print("关闭数据库连接")


# ids：参数别名id
# 不能单独使用，必须和params一起使用，作用是对参数起别名
# 我们在采用pytest进行测试数据输出时会有对应的方法调用n次，该n次采用不同的params参数，这个ids就是修改了console控制台展示数据
class TestDemo:
    def read_yaml():
        return ["胡桃", "胡桃宝宝", "胡桃厨"]

    # 当我们书写了ids，我们的控制输出就不会再是上面的["胡桃","胡桃宝宝","胡桃厨"]，而是我们所书写的["1","2","3"]
    @pytest.fixture(scope="function", autouse=False, params=read_yaml()，ids = ["1", "2", "3"])

    def exe_database_sql(request):
        print("执行SQL查询")

    # 我们通过request.param获取数据，可以采用yield返回该数据
    yield request.param
    print("关闭数据库连接")


# name：Fixture别名
# 作用是给fixtrue起别名，一旦使用了别名，那么fixtrue的名称就不能再用了，只能用别名
class TestDemo:

    # 如果我们在这里使用到了别名
    @pytest.fixture(scope="function", name="exe_datebase_sql_name")
    def exe_database_sql(request):
        print("执行SQL查询")

    yield
    print("关闭数据库连接")

    # 我们这里就需要使用别名进行操作，之前的名称无法使用
    def test_2(self，exe_datebase_sql_name):
    print(exe_database_sql)


# 接下来我们就将会讲解到我们刚刚提到的conftest.py文件：

# 首先我们需要知道conftest.py文件的名字是固定形式，不可改变
# conftest.py文件主要就是用来存储我们的Fixture，然后我们会根据该文件的不同位置来判断可以使用的方法
# conftest可以在不同的目录级别下创建，如果我们在根目录下创建，那么所有case都会使用到该Fixture
# 但是如果我们在testcases文件夹下的某个模块文件下创建conftest.py，那么它的作用范围就只包含在该目录下

# 根目录创建的conftest.py
# 我们在该目录下的conftest文件里写的所有fixture可以在任意测试类下执行
import pytest

@pytest.fixture(scope="function", name="exe_datebase_sql_name")
def exe_database_sql():
    print("全部方法运行前均可以执行")
    yield
    print("全部方法运行后均可以执行")


# testcases文件下的所有测试类
# 这里需要注意：我们使用conftest下的Fixture时，不需要import导包就可以使用
import pytest

class TestDemo1:
    # 测试Case1
    def test_1(self, exe_datebase_sql_name):
        print('输入正确用户名密码验证码,点击登录 1' + exe_datebase_sql_name)


# testcases文件夹下的usercases文件夹下创建的conftest.py
# 我们在该目录下创建的conftest文件里写的所有fixture仅可以在该目录下的测试类中使用，在其他测试类中使用会出现报错
import pytest

@pytest.fixture(scope="function", name="usercases_fixture")
def exe_database_sql():
    print("usercases方法运行前均可以执行")
    yield
    print("usercases方法运行后均可以执行")


# testcases文件下的usercases文件夹下的测试类
import pytest

class TestUserCases1:
    # 测试Case1
    def test_1(self, usercases_fixture):
        print('输入正确用户名密码验证码,点击登录 1' + usercases_fixture)


# 最后我们简单给出一个前后置执行顺序优先级：
# fixture_session > fixture_class > setup_class > fixture_function > setup

# 然后最后我们给出前后置执行的一个总体逻辑顺序：
    # 查询当前目录下的conftest.py文件
    # 查询当前目录下的pytest.ini文件并找到测试用例的位置
    # 查询用例目录下的conftest.py文件
    # 查询测试用例的py文件中是否有setup, teardown, setup_class, teardown_class
    # 再根据pytest.ini文件的测试用例的规则去查找用例并执行
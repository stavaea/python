# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2024/1/12 18:03
# @Author : waxberry
# @File : pip 常用命令.py
# @Software : PyCharm



# 安装
py -m ensurepip --upgrade


# 如何使用
# 安装后，在命令行中输入pip，然后按下回车，就会出现下图所示的使用说明

升级
要是你觉得自己的pip版本有点低，想要升级一下的话，在命令行中输入以下命令
pip install --upgrade pip
或者是
pip install -U pip

安装某个版本的包
如果打算用pip来安装第三方的包，用的是以下的命令行
pip install package-name
例如我们想要安装指定版本的第三方的包，例如安装3.4.1版本的matplotlib，
pip install matplotlib==3.4.1

卸载或者是更新包
要是你打算想要卸载某个包，该要输入的命令行是
pip uninstall package_name
而如果打算更新某个包，对应的命令行是
pip install --upgrade package_name
# 或者是
pip install -U package_name

查看某个包的信息
可以通过以下的这个命令行来查看指定包的信息，
pip show -f requests

查看需要被升级的包
我们需要查看一下现有的这些包中，哪些是需要是被升级的，可以用下面这行命令行来查看，
pip list -o


查看兼容问题
在下载安装一些标准库的时候，
需要考虑到兼容问题，一些标准库的安装可能需要依赖其他的标准库，会存在版本相冲突等问题，我们先用下面这条命令行来检查一下是否会有冲突的问题存在
pip check package_name
当然要是我们不指定是哪个标准库的话，会检查现在已经安装的所有包中的是否存在版本冲突等问题
pip check


指定国内源来安装
我们要是感觉到安装的速度有点慢，可以指定国内的源来安装某个包，例如
pip install -i https://pypi.douban.com/simple/ package_name

国内源有
清华：https://pypi.tuna.tsinghua.edu.cn/simple
阿里云：http://mirrors.aliyun.com/pypi/simple/
中国科技大学 https://pypi.mirrors.ustc.edu.cn/simple/
华中理工大学：http://pypi.hustunique.com/
山东理工大学：http://pypi.sdutlinux.org/
豆瓣：http://pypi.douban.com/simple/

下载包但是不安装
要是我们想要下载某个包到指定的路径下，命令行如下
pip download package_name -d "某个路径"
例如
pip download requests -d "."


批量安装软件包
我们一般在看到别人的项目时，都会包含一个requirements.txt文件，里面包含了一些Python项目当中需要用到的第三方库
要生成这种txt文件，需要这么来做
pip freeze > requirements.txt
而如果我们需要来批量安装第三方库，在命令行中输入以下这个命令
pip install -r requirements.txt
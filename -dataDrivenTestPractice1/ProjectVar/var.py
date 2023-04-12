#coding:utf-8

import os

# 获取工程所在目录的绝对路径
project_path = os.path.dirname(os.path.dirname(__file__))

# 获取页面对象库文件的绝对路径
page_object_repository_path = project_path.decode("utf-8")+u"/conf/PageObjectRepository.ini"

if __name__ == '__main__':
    # 测试代码
    print ("project_path", project_path)
    print ("page_object_repository_path", page_object_repository_path)
    print (os.path.exists(project_path))
    print (os.path.exists(page_object_repository_path))
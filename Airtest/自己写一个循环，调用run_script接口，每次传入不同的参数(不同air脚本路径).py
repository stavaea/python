#coding:utf-8
import os, sys
import
from airtest.cli.runner import run_script
from airtest.cli.parser import runner_parser

def find_all_script(file_path):
    '''查找air脚本'''
    A = []
    files = os.listdir(file_path)
    for f1 in files:
        tmp_path = os.path.join(file_path, files)
        if not os.path.isdir((tmp_path)):
            pass
        else:
            if (tmp_path.endswith('.air')):
                A.append(tmp_path)
            else:
                sublist = find_all_script(tmp_path)
                A = A + sublist
    return A

def run_airtest(path, dev=''):
    '''运行air脚本'''
    log_path = os.path.join(path, 'log')
    # 组装参数
    args = Namespace(device=dev, log=log_path, recording=None, script=path)
    try:
        result = run_script(args, CustomLuancher)
    except:
        pass
    finally:
        if result and result.wasSuccessful():
            return True
        else:
            return False

if __name__ == '__main__':
    # 查找指定路径下的全部air脚本
    air_list = find_all_script(CustomLuancher.PROJECT_ROOT)

    for case in air_list:
        result = run_airtest(case)
        if not result:
            print ('test fail:'+ case)
        else:
            print ('test pass:'+ case)
    sys.exit(-1)
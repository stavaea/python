#coding:utf-8
from airtest.cli.runner import AirtestCase, run_script
from airtest.cli.parser import runner_parser

class CustomAirtestCase(AirtestCase):
    project_root = '子脚本存放公共路径'
    def setUp(self, ST=None):
        print ('custom setup')
        # add var/function/class/..to globals
        # 将自定义变量添加到self.scope里，脚本代码中就能够直接使用这些变量
        self.scope['hunter'] = 'i am hunter'
        self.scope['add'] = lambda x: x+1
        # 将默认配置的图像识别准确率阀值改为了0.75
        ST.THRESHOLD = 0.75

        # exec setup script
        # 假如该setup.air脚本存放在project_root目录下，调用时无需填写绝对路径，可以直接写相对路径
        self.exec_other_script('setup.air')
        super(CustomAirtestCase, self).setUp()

    def tearDown(self):
        print ('custom tearDown')
        # exec tearDown script
        self.exec_other_script('teardown.air')
        super(CustomAirtestCase, self).setUp()

if __name__ == '__main__':
    ap = runner_parser()
    args = ap.parse_args()
    run_script(args, CustomAirtestCase)
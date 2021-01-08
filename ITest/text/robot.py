#coding:utf-8
from wxpy import *

# 初始化机器人，扫码登录
bot = Bot()
api_key = '014ede422f8a4d0ea3af73aa78b306b9'
# 搜索自己的好友列表‘你想找的好友名称’
# my_friend = bot.friends().search('名字')[0]
my_friend = ensure_one(bot.search('名字'))
tuling = Tuling(api_key=api_key)

# 使用图灵机器人自动与指定好友聊天
@bot.register(my_friend, except_self=True)
def reply_my_friend(msg):
    tuling.do_reply(msg)


# @bot.register(my_friend)
# def print_msg(msg):
#     print msg.text

# embed()#进入交互式python命令行界面，并阻塞当前线程
bot.join()
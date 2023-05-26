# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2023/5/22 9:52
# @Author : waxberry
# @File : chat_robot.py
# @Software : PyCharm

import openai

def query(text):
    model_enginer = 'text-davinci-003'
    try:
        completion = openai.Completion.create(engine=model_enginer,
                                              prompt=text,
                                              max_tokens=1024,
                                              n=1,
                                              stop=None,
                                              temperature=0.5)
        return completion.choices[0].text
    except Exception as e:
        print('quert failed:', e)
        return None

prompt_role = '你是一个旅游达人'
messages = [
    {'role': 'system', 'content': prompt_role},
    {'role': 'user', 'content': '你好，chatGPT！请问你能帮我回答一些问题吗？'},
]
def get_response_from_gpt(message):
    try:
        response = openai.ChatCompletion.create(
            model='gpt-3.5-turbo', #对话模型的名称
            temperature=0.9, #控制回复的随机性
            top_p=1, #控制回复的令牌采样的策略
            messages=messages, #输入消息列表
        )

        return response.choices[0]['message']['content']
    except Exception as e:
        print('quert failed:', e)
        return None
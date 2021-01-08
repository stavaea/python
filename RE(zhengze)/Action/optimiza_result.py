#coding:utf-8
import re

def clear_th0(handled_str):
    if '<' in handled_str or '>' in handled_str:
        re_list = re.findall(r'<.+?>', handled_str)
        for ir in list(set(re_list)):
            handled_str = ''.join(handled_str.split(ir))
    return handled_str

def clear_th(handled_str):
    r_handled_str = clear_th0(handled_str)
    result_str = ''
    for ir in r_handled_str:
        if ir == '>' or ir == '<' or ir == '\"':
            continue
        result_str += ir
    return result_str
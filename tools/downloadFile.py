# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2022/8/18 9:34
# @Author : waxberry
# @File : downloadFile.py
# @Software : PyCharm

import requests


'''使用以下流式代码，无论下载文件的大小如何，Python 内存占用都不会增加'''
def download_file(url):
    local_filename = url.split('/')[-1]
    # 注意传入参数stream=True
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    return local_filename


'''如果你有对 chunk 编码的需求，那就不该传入 chunk_size 参数，且应该有 if 判断'''
def download_file(url):
    local_filename = url.split('/')[-1]
    # 注意传入参数stream=True
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content():
                '''iter_content[1] 函数本身也可以解码，只需要传入参数 decode_unicode = True 即可。
请注意，使用 iter_content 返回的字节数并不完全是 chunk_size，它是一个通常更大的随机数，并且预计在每次迭代中都会有所不同'''
                if chunk:
                    f.write(chunk.decode('utf-8'))
    return local_filename


# 方法二
import requests
import shutil

def download_file(url):
    local_filename = url.split('/')[-1]
    with requests.get(url, stream=True) as r :
        with open(local_filename, 'rb') as f:
            shutil.copyfileobj(r.raw, f)
    return local_filename

'''这将文件流式传输到磁盘而不使用过多的内存，并且代码更简单。

注意：根据文档，Response.raw 不会解码，因此如果需要可以手动替换 r.raw.read 方法'''

# response.raw.read = functools.partial(response.raw.read, decode_content=True)



'''方法二更快。方法一如果 2-3 MB/s 的话，方法二可以达到近 40 MB/s。'''
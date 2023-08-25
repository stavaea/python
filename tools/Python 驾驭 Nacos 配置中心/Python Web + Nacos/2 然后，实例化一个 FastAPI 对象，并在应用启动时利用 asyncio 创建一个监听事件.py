# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2023/8/9 11:01
# @Author : waxberry
# @File : 2 然后，实例化一个 FastAPI 对象，并在应用启动时利用 asyncio 创建一个监听事件.py
# @Software : PyCharm

from fastapi import FastAPI
import nacos
import uvicorn
import asyncio

app = FastAPI()

# 运行时触发
@app.on_event('startup')
async def startup_event():
    asyncio.create_task(event_listener())

if __name__ == '__main__':
    uvicorn.run('demo_fastapi:app', host='0.0.0.0', port=8000, reload=True)
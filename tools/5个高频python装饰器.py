# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2024/1/12 17:13
# @Author : waxberry
# @File : 5个高频python装饰器.py
# @Software : PyCharm




# 1. 日志记录
# 在执行函数前后记录日志是装饰器的一种常见用途。这在调试和监控应用程序时非常有用。
def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"{func.__name__} 函数正在执行...")
        result = func(*args, **kwargs)
        print(f"{func.__name__} 函数执行完成.")
        return result
    return wrapper
@log_decorator
def test_function(x):
    return x * x
test_function(5)


# 2.性能测试
# 使用装饰器记录函数的执行时间，有助于性能分析和优化。
import time
def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} 耗时 {end_time - start_time} 秒.")
        return result
    return wrapper
@timing_decorator
def long_running_function():
    time.sleep(2)
long_running_function()


# 3. 访问控制
# 装饰器可以用来增加访问控制逻辑，例如验证用户权限。
def admin_required(func):
    def wrapper(*args, **kwargs):
        if not user_is_admin():
            raise Exception('用户不是管理员，无法执行操作')
        return func(*args, **kwargs)
    return wrapper
@admin_required
def sensitive_function():
    print('执行敏感操作！')
def user_is_admin():
    # 这里应该是检查用户是否为管理员的逻辑
    return True
sensitive_function()



# 4. 缓存结果
# 装饰器可以用于缓存函数的结果，避免重复计算，特别是在处理昂贵的计算任务时。
def cache_decorator(func):
    cache = {}
    def wrapper(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result
    return wrapper
@cache_decorator
def expensive_computation(x):
    print('计算中...')
    time.sleep(2)#模拟耗时操作
    return x * x
print(expensive_computation(4))
print(expensive_computation(4))#这次将直接从缓存中获取结果

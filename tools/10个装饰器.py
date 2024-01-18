# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2024/1/18 9:41
# @Author : waxberry
# @File : 10个装饰器.py
# @Software : PyCharm




# 1、@timer:测量执行时间
import time
def timer(func):
    def warpper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time:.2f} seconds to execute.")
        return result
    return warpper
@timer
def my_data_processing_function():
    # Your data processing code here
    pass


# 2、@memoize:缓存结果
def memoize(func):
    cache = {}
    def wrapper(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result
    return wrapper
@memoize
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


# 3、@validate_input:数据验证
def validate_input(func):
    def wrapper(*args, **kwargs):
        # Your data validation logic here
        if valid_data:
            return func(*args, **kwargs)
        else:
            raise ValueError("Invalid data. Please check your inputs.")
    return wrapper
@validate_input
def analyze_data(data):
    # Your data analysis code here
    pass


# 4、@log_results:日志输出
def log_results(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        with open("results.log", "a") as log_file:
            log_file.write(f"{func.__name__} - Result: {result}\n")
        return result
    return wrapper
@log_results
def calculate_metrics(data):
    # Your metric calculation code here
    pass


# 5、@suppress_errors:优雅的错误处理
def suppress_errors(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Error in {func.__name__}: {e}")
            return None
    return wrapper
@suppress_errors
def preprocess_data(data):
    # Your data preprocessing code here
    pass


# 6、@validate_output:确保质量结果
def validate_output(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if valid_output(result):
            return result
        else:
            raise ValueError("Invalid output. Please check your function logic.")
    return wrapper
@validate_output
def clean_data(data):
    # Your data cleaning code here
    pass


# 7、@retry:重试执行
import time
def retry(max_attempts, delay):
    def decorator(func):
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Attempt {attempts + 1} failed. Retrying in {delay} seconds.")
                    attempts += 1
                    time.sleep(delay)
            raise Exception("Max retry attempts exceeded.")

        return wrapper

    return decorator
@retry(max_attempts=3, delay=2)
def fetch_data_from_api(api_url):
    # Your API data fetching code here
    pass


# 8、@visualize_results:漂亮的可视化
import matplotlib.pyplot as plt
def visualize_results(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        plt.figure()
        # Your visualization code here
        plt.show()
        return result
    return wrapper
@visualize_results
def analyze_and_visualize(data):
    # Your combined analysis and visualization code here
    pass


# 9、@debug:调试变得更容易
def debug(func):
    def wrapper(*args, **kwargs):
        print(f"Debugging {func.__name__} - args: {args}, kwargs: {kwargs}")
        return func(*args, **kwargs)
    return wrapper
@debug
def complex_data_processing(data, threshold=0.5):
    # Your complex data processing code here
    pass


10、@deprecated:处理废弃的函数
import warnings
def deprecated(func):
    def wrapper(*args, **kwargs):
        warnings.warn(f"{func.__name__} is deprecated and will be removed in future versions.", DeprecationWarning)
        return func(*args, **kwargs)
    return wrapper
@deprecated
def old_data_processing(data):
    # Your old data processing code here
    pass
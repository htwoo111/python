"""
装饰器是在原来函数不修改的前提下，对函数整体加功能

1.计算运行的时间
"""
import time
def set_func(func):
    def call_func():
        # print("-----这是权限验证1------")
        # print("-----这是权限验证2------")
        start_time = time.time()
        func()
        stop_time = time.time()
        print("spended time is {}".format(stop_time - start_time))
    return call_func

@set_func
def test():
    print("这是test函数")

test()


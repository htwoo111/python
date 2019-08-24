"""
装饰器是在原来函数不修改的前提下，对函数整体加功能
"""
def set_func(func):
    def call_func():
        print("-----这是权限验证1------")
        print("-----这是权限验证2------")
        func()
    return call_func


def test():
    print("这是test函数")


# 装饰器的原理与闭包类似
# ret = set_func(test)
# ret()

test = set_func(test)
test()
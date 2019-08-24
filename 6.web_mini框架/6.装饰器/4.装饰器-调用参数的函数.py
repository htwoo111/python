"""
装饰器是在原来函数不修改的前提下，对函数整体加功能
"""
def set_func(func):
    def call_func(a):  # 注意这里也需要传入参数
        print("-----这是权限验证1------")
        print("-----这是权限验证2------")
        func(a)  # 注意这里也需要传入参数
    return call_func

@set_func
def test1(num):
    print("这是test1函数 %d" % num)

@set_func
def test2(num):
    print("这是test2222函数 %d" % num)

test1(100)
test2(2000)
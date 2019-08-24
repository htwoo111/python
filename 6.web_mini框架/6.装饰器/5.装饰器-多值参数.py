"""
装饰器是在原来函数不修改的前提下，对函数整体加功能
传入不定长参数时，注意*args, **kwargs
"""
def set_func(func):
    def call_func(*args, **kwargs):  # 注意这里也需要传入参数
        print("-----这是权限验证1------")
        print("-----这是权限验证2------")
        func(*args, **kwargs)  # 注意这里也需要传入参数
    return call_func

@set_func
def test1(num, *args, **kwargs):
    # print("这是test1函数 %d" % num)
    print("--------test1------%d" %num)
    print("--------test1------" , args)
    print("--------test1------" , kwargs)
    print(kwargs['n1'])


# test1(100)
# test1(100, 200)
test1(100, 200, 300, n1=100, n2=200)
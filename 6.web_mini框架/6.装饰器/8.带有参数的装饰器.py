def decorator_with_argument(privilege_level):
    """装饰器外部再嵌套一个装饰器，可以实现传递参数的作用"""
    def decorator(func):
        """创建一个装饰器"""
        def call_func(*args, **kwargs):
            if privilege_level == 1:  # 设置权限等级1
                print("this is privilege 1, please enter your account")
            elif privilege_level == 2:  # 设置权限等级2
                print("this is privilege 2, please enter your account and password")
            else:
                pass
            return func()
        return call_func
    return decorator  # 注意要返回第二层函数的引用，才能实现装饰器传递参数

# 传递的参数必须在调用装饰器时传入
@decorator_with_argument(1)  # 等价于 decorator(func, privilege_level=1)，这样执行时，装饰器的参数可以由自己选择传入
def test1():
    print("this is a test 111")
    return "hello wolrd"

@decorator_with_argument(2)
def test2():
    print("this is a test 222")
    return "hello wolrd"


test1()
test2()
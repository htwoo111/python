"""多个装饰器对同一个函数进行装饰"""

def decorator_1(func):
    print("This is decorator one-----1111")
    def call_func():
        print("----promission 1-------")
        return func()
    return call_func

def decorator_2(func):
    print("This is decorator two-----2222")
    def call_func():
        print("----promission 2-------")
        func()
        # print("----promission 2-------")
    return call_func

def test2():
    print("this is test2222")

test2 = decorator_2(test2)
test2 = decorator_1(test2)
test2()



print("-" * 50)

@decorator_1 
@decorator_2
def test1():
    print("This is test 1 test 1 test 1")

# test1()
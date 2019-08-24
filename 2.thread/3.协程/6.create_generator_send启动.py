# 生成器是特殊的迭代器
# 生成器可以让一个函数暂停，想执行的时候执行

def fibonacci(length):
    """创建一个financci的生成器"""
    a, b = 0, 1
    current_num = 0
    while current_num < length:
        # 函数中由yield 则这个不是简单的函数，而是一个生成器模板
        print("111")
        ret = yield a
        print("222")
        print(">>>>ret>>>>", ret) 
        a, b = b, a+b
        # print(a, end=",")
        current_num += 1


obj = fibonacci(10)

ret =  next(obj)
print(ret)
ret =  next(obj)
print(ret)

# 第一次最好不用send启动
# ret = obj.send("hhhhh")  # send里面的参数当作结论传递给 yield的返回值
# print(ret)


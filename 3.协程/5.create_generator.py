# 生成器是特殊的迭代器


def fibonacci(length):
    """创建一个financci的生成器"""
    a, b = 0, 1
    current_num = 0
    while current_num < length:
        # 函数中由yield 则这个不是简单的函数，而是一个生成器模板
        yield a 
        a, b = b, a+b
        # print(a, end=",")
        current_num += 1

# 如果调用finbonacci(length)表示创建一个生成器
obj = fibonacci(10)
for num in obj:
    print(num)
print(list(obj))


# print(list(fibonacci(10)))

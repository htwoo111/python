class Line(object):
    """创建一个类，去解一元一次方程"""
    def __init__(self, k, b):
        self.k = k
        self.b = b

    def __call__(self, x):
        print((self.k * x) + self.b)


line = Line(1, 2)
line(0)
line(1)
line(2)
line(3)
line(4)
line = Line(113, 23)
line(0)
line(1)
line(2)
line(3)
line(4)
# 创建类浪费资源

print("-" * 50)

print("--------闭包-------------")
# 闭包：函数内部嵌套函数， 一般内部函数调用时会用到外部函数的变量值
def line_6(k, b):
    def create_y(x):
        print(k * x + b)
    return create_y

line_6_1 = line_6(1, 2)
line_6_1(1)
line_6_1(2)
line_6_1(3)

line_6_2 = line_6(11, 23)
line_6_2(1)
line_6_2(2)
line_6_2(3)

# 思考： 函数、匿名函数、闭包、对象当做实参时有什么区别？
# 1.匿名函数能够完成基本的简单功能， 传递是这个函数的引用只有功能
# 2.普通函数能够完成较为复杂的功能， ， ， 传递是这个函的引用只有功能
# 3.闭包能够将较为复杂的功能，传递是这个闭包中的函数以及数据， 因此传递是功能+ 数据
# 4.对象能够完成最为复杂的功能，传递是很多数据+ 很多功能， 因此传递是功能+ 数据








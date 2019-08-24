# 1.类属性是所有实列对象共有的(类对象自己可以调用)，
# 一般实例对象无法修改类方法,(实例对象.__class__.xxx修改)
# 2.实列属性是每一个实列对象独有的
# 3.静态方法与普通函数相似。静态方法的用处在于，所有实列方法都可以调用，
# 同时不修改(重写)里面的内容


class Province(object):
    country = "China"

    def __init__(self, name):
        self.name = name
        print(self.name)

    @classmethod
    def class_func(cls):
        print(cls.country)
        return ""

    @staticmethod
    def static_func():
        print("静态方法")


guangdong = Province("广东")
# print(guangdong.__class__.country)
print(Province.class_func())
print(guangdong.class_func())
guangdong.static_func()
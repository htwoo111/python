print("******多继承使用super().__init__ 发发生的状态******")

class Parent(object):
    def __init__(self, name, *args, **kwargs):   # 为了避免报错，使用不定长参数，接收参数
        print("parent的init开始调用")
        self.name = name 
        print("parent的init结束调用----")


class Son1(Parent):
    def __init__(self, name, age, *args, **kwargs):  # 为了避免报错，使用不定长参数，接收参数
        print("son111的init开始调用")
        self.age = age
        super().__init__(name, *args, **kwargs)  # 为了避免报错，使用不定长参数，接收参数
        print("son111的init结束调用-----")


class Son2(Parent):
    def __init__(self, name, gender, *arg, **kwargs):  # 为了避免报错，使用不定长参数，接收参数
        print("son222的init开始调用")
        self.gender = gender
        super().__init__(name, *arg, **kwargs)
        print("son222的init结束调用-----")


class Grandson(Son1, Son2):
    def __init__(self, name , age, gender):
        print("Grandson的init开始调用")
        # 多继承时， 相对于使用类名.__init__方法，要把父类全部重写一遍
        # 而super只用一句话，执行了全部父类的方法， 这也是多继承需要全部传参的原因
        # super(Grandson, self).__init__(name, age, gender)
        super().__init__(name, age, gender)
        print("Grandson的init结束调用-----")


print(Grandson.__mro__)

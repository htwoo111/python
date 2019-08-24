class Test1(object):
    """普通方法创建类"""
    def __init__(self):
        print("init 1")

    @staticmethod
    def static_method():
        print("static method 1")
    
    @classmethod
    def class_method(cls):
        print("class method 1")

# -------------------------------------------------
# 元类创建类
def __init__(self):
    print("init 2")

@staticmethod
def static_method():
    print("static method 2")

@classmethod
def class_method(cls):
    print("class method 2")

# 变量_接收引用 = type("类名", (父类, ), {类属性，类方法})
Test2 = type("Test2",
             (object,),
             {"__init__":__init__, "static_method":static_method, "class_method":class_method})


def main():
    test1 = Test1()
    test1.static_method()
    test1.class_method()
    
    test2 = Test2()
    test2.static_method()
    test2.class_method()




if __name__ == "__main__":
    main()

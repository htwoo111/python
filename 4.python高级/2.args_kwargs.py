def test1(a, b, *args, **kwargs):
    print("------1-------")
    print(a)
    print(b)
    print(args)
    print(kwargs)


def test2(a, b, *args, **kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)
    test1(a, b, args, kwargs)  # test1(1,2, (3, 4, 5, {'name': '小米', 'age': 10})
    test1(a, b, *args, kwargs)  # test1(1, 2, 3, 4, 5, {'name': '小米', 'age': 10})
    test1(a, b, *args, **kwargs)  # test1(1, 2, 3, 4, 5,name='小米', age=10)


# test2(1,2,3,4,5,name="小米", age=10)


def test3(a, b, *args, **kwargs):
    name = args[0]
    age = args[1]
    print(a)
    print(b)
    print(name)
    print(age)


test3(1, 2, 3, 4)
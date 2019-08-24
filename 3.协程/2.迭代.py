# from collections import Iterable
# from collections import Iterator


class Classmate(object):
    
    def __init__(self):
        self.names = list()
        self.current_num = 0

    def add(self, name):
        self.names.append(name)

    def __iter__(self):
        """如果想要对象成为可以迭代的，那么必须使用_iter__方法"""
        return self

    def __next__(self):
        if self.current_num < len(self.names):
            ret = self.names[self.current_num]
            self.current_num += 1
            return ret
        else:
            raise StopIteration

c = Classmate()
c.add("a")
c.add("b")
c.add("c")


for name in c:
    print(name)

# c_iterator = iter(c)
# print("是否为可迭代",isinstance(c, Iterable))
# print("是否为迭代器",isinstance(c_iterator, Iterator))
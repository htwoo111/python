from contextlib import contextmanager


def write_file_1(file_name, content):
    """普通版"""
    f = open(file_name, "r")
    f.write(content)
    f.close()


def write_file_2(file_name, content):
    """进阶版"""
    f = open(file_name, "r")
    try:
        f.write(content)
    except IOError:
        print("oops error")  # 处理异常
    finally:
        f.close()


def write_file_3(file_name, content):
    """"高级版"""
    with open(file_name, "r") as f:
        f.write()


class File(object):
    """
    其作用与上面高级版类似,
    采用上下文管理器
    当调用with的时候会自动调用__enter__方法
    当调用完成时会自动调用__exit__方法
    """
    def __init__(self, file_name, mode):
        self.file_name = file_name
        self.mode = mode

    def __enter__(self):
        print("entering")
        self.f = open(self.file_name, self.mode)
        return self.f

    def __exit__(self, *args):
        print("exit...")
        self.f.close()


with File("文件名", "w") as f:
    print("writing")
    f.write("hello world")


@contextmanager
def my_open(path, mode):
    f = open(path, mode)
    yield f
    f.close()

with my_open("a.txt", "w") as f:
    f.write("hello world")

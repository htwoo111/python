import time


def test1():
    while True:
        print("----1----")
        # time.sleep(0.1)
        time.sleep(1)
        yield  # 让函数暂停执行


def test2():
    while True:
        print("----2----")
        # time.sleep(0.1)
        time.sleep(1)
        yield  # 让函数暂停执行


def main():
    t1 = test1()
    t2 = test2()
    while True:
        # 协程--并发，切换的资源最少
        next(t1)   # 两个函数交替执行，时间间隔短，相当于同时执行pip
        next(t2)


if __name__ == "__main__":
    main()
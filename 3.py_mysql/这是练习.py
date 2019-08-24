import threading


class Test1(object):
    def __init__(self):
        self.name = 'lihua'

    # def process(self):
    #     t1 = threading.Thread(target=Test1.run)
    #     t1.start()
    #     t1.join()

    @staticmethod
    def run():
        for i in range(10):
            print('start 1------')


class Test2(object):
    def __init__(self):
        pass

    # def process(self):
    #     t2 = threading.Thread(target=Test2)
    #     t2.start()
    #     t2.join()

    @staticmethod
    def run():
        for i in range(10):
            print("2-2-2-2-2-2-2")


def main():
    test1 = Test1()
    test2 = Test2()

    t1 = threading.Thread(target=test1.run)
    t2 = threading.Thread(target=test2.run)

    t1.start()
    t2.start()


if __name__ == "__main__":
    main()

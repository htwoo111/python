import threading
import time


class MyThread(threading.Thread):

    def run(self):
        for i in range(5):
            time.sleep(1)
            msg = "I'm " + self.name + ' @' + str(i)
            print(msg)
        MyThread.login(self)
        MyThread.register(self)

    def login(self):
        print("---这是登录----")

    def register(self):
        print("----这是注册----")


if __name__ == "__main__":
    t = MyThread()

    t.start()

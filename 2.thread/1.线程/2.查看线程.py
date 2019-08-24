import threading
import time


def test1():
    for i in range(5):
        print("-----test1------{}".format(i))
        time.sleep(1)


def test2():
    for i in range(10):
        print("-----test2------{}".format(i))
        time.sleep(1)

def main():
    t1 = threading.Thread(target=test1)
    t2 = threading.Thread(target=test2)
    
    t1.start()
    t2.start()
    while True:
        print(threading.enumerate())
        if len(threading.enumerate()) <= 2:
            break
        time.sleep(1)

if __name__ == "__main__":
    main()
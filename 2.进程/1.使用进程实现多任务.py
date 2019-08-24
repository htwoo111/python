import threading
import time
import multiprocessing


def test1():
    while True:
        print("11111-----")
        time.sleep(1)


def test2():
    while True:
        print("2-------")
        time.sleep(1)


def main():
    # t2 = threading.Thread(target=test2)
    # t1 = threading.Thread(target=test1)

    # t1.start()
    # t2.start()

    p1 = multiprocessing.Process(target=test1)
    p2 = multiprocessing.Process(target=test2)
    

    p1.start()
    p2.start()

if __name__ == "__main__":
    main()

    
"""能共享的资源，操作系统会复制一份，
   不能共享的资源，会修改资源"""
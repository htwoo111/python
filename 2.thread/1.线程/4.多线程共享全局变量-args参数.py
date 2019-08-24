import threading
import time

g_nums = [11, 22]

def test1(temp):
    temp.append(33)
    print("------in test11111 g_nums = {}".format(str(g_nums)))


def test2(temp):
    print("-------in test2 g_nums = {}".format(str(g_nums)))

def main():
    t1 = threading.Thread(target=test1, args=(g_nums,))
    t2 = threading.Thread(target=test2, args=(g_nums,))

    t1.start()
    time.sleep(1)

    t2.start()
    time.sleep(1)
    print("---- mainnnn g_nums = {}".format(g_nums))


if __name__ == "__main__":
    main()
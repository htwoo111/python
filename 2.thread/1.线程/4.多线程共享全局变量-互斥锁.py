import threading
import time

g_num = 0

def test1(num):
    global g_num
    # 上锁，如果之前没上锁，此时上锁成功
    # 如果上锁之前，已经被上锁，那么此时会堵塞在这里，直到锁被解开为止
    mutex.acquire()
    for i in range(num):
        g_num += 1
    # 解锁
    mutex.release()
    print("------in test11111 g_num = {}".format(g_num))


def test2(num):
    global g_num
    mutex.acquire()
    for i in range(num):
        g_num += 1
    mutex.release()
    print("-------in test2 g_nums = {}".format(str(g_num)))

# 创建一个互斥锁,默认不上锁
mutex = threading.Lock()


def main():
    t1 = threading.Thread(target=test1, args=(10000,))
    t2 = threading.Thread(target=test2, args=(10000,))

    t1.start()
    print("")
    t2.start()
    
    time.sleep(2)
    
    print("main -----g_num = {}".format(g_num))

if __name__ == "__main__":
    main()
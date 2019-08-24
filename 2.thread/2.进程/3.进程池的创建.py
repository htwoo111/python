# -*- coding:utf-8 -*-
from multiprocessing import Pool
import os, time, random


def worker(msg):
    t_start = time.time()
    print("{}.开始执行，进程号是{}".format(msg, os.getpid()))
    # random.random()随机生成0-1之间的浮点数
    time.sleep(random.random() * 2)
    t_stop = time.time()
    print(msg, "执行完毕，耗时{:.2f}".format(t_stop-t_start))


def main():
    po = Pool(3)  # 定义一个进程池，最大进程为3
    for i in range(0,10):
        # Pool().apply_async(要调用的函数名, (传递目标参数的元组,))
        # 每次循环将会用空闲出来的子进程去调用目标
        po.apply_async(worker, (i,))
    print("----start-----")
    po.close()  # 关闭进程池，关闭后po不再接收新的请求
    po.join()   # 等待pool中所有的子进程执行完成，必须放在close()后面
    print("-----end------")

if __name__ == "__main__":
    main()
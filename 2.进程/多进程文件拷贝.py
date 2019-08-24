import multiprocessing
import os


def copy_file(q, old_file_name, new_file_name, file_name):
    """完成文件的复制"""
    # 从要复制的文件中读取数据
    old_f = open(old_file_name + "/" + file_name, "rb")
    content = old_f.read()
    old_f.close()

    # 创建新文件，完成复制
    new_f = open(new_file_name + "/" + file_name, "wb")
    new_f.write(content)
    new_f.close()
    
    q.put(file_name)


def main():
    # 获取用户想要下载的文件名
    old_file_name = input("请输入想要复制的文件名:")

    # 创建新的文件
    try:
        new_file_name = old_file_name + "_copy"
        os.mkdir(new_file_name)
    except:
        pass
    
    # 获取待复制文件夹里面的文件列表 os.listdir
    file_names = os.listdir(old_file_name)

    # 创建进程池，使用多进程进行拷贝  使用3个进程
    po = multiprocessing.Pool(3)

    # 创建队列，准备完成进度条
    q = multiprocessing.Manager().Queue()

    # 向进程中添加任务
    for file_name in file_names:
        po.apply_async(copy_file, args=(q, old_file_name, new_file_name, file_name))

    # 关闭进程池
    po.close()
    # po.join()

    all_file_num = len(file_names)
    file_num = 0
    while True:
        q.get()
        file_num += 1
        print("\r当前完成进度为{:.1%}".format(file_num / all_file_num))
        
        if file_num >= all_file_num:
            break



if __name__ == "__main__":
    main()
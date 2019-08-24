import os
import multiprocessing 


def copy_file(q, file_name, old_folder_name, new_folder_name):
    """完成文件的复制"""
    # print("文件名是{},从[{}]---->[{}]".format(file_name, old_folder_name, new_folder_name))
    old_f = open(old_folder_name + "/" + file_name,"rb")
    content = old_f.read()
    old_f.close()

    new_f = open(new_folder_name + "/" + file_name, "wb")
    new_f.write(content)
    new_f.close()

    # 如果文件拷贝完了，那么就向队列中写入信息，表示完成
    q.put(file_name)



def main():
    # 1.获取用户要复制的文件夹名
    old_folder_name = input("请输入要复制的文件夹的名字:")

    # 2.创建一个新的文件夹
    try:
        new_folder_name = old_folder_name + "_copy"
        os.mkdir(new_folder_name)
    except:
        pass

    # 3.获取文件夹中的所有待copy的文件名 listdir()
    file_names = os.listdir(old_folder_name)

    # 4.创建进程池
    po = multiprocessing.Pool(3)

    # 5.创建一个队列
    q = multiprocessing.Manager().Queue()

    # 6.向进程中添加copy文件任务
    for file_name in file_names:
        po.apply_async(copy_file, args=(q, file_name, old_folder_name, new_folder_name))

    # 复制原文件夹中的文件到新文件夹中去

    po.close()
    # po.join()
    all_file_num = len(file_names)  # 测试所有的文件个数
    file_num = 0
    while True:
        file_name = q.get()
        # print("已经完成{}的copy".format(file_name))
        file_num += 1
        print("\r拷贝的进度为{:.1%}".format((file_num / all_file_num)), end="")
        if  file_num >= all_file_num:
            break

if __name__ == "__main__":
    main()
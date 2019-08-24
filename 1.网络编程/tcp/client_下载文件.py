import socket

def download_file(client_socket):
    """从服务下载文件"""
    # 获取文件名，并发送给服务器
    file_name = input("请输入想要下载的文件名:")
    client_socket.send(file_name.encode("gbk"))
    
    # 从服务器接收数据
    file_data = client_socket.recv(1024 * 1024)

    # 将接收到的数据保存
    if file_data:
        with open("[new]" + file_name, "wb") as f:
            f.write(file_data)


def main():
    # 创建套接字
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 获取服务器IP和PORT
    server_ip = input("请输入服务器的IP:")
    server_port = int(input("请输入服务器的端口："))

    # 链接服务器
    client_socket.connect((server_ip, server_port))
 
    # 从服务器下载文件
    download_file(client_socket)
    
    # 关闭套接字
    client_socket.close()



if __name__ == "__main__":
    main()

    
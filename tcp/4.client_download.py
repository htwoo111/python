import socket


def main():
    # 创建套接字
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # 获取服务器的IP,port
    dest_ip = input("请输入下载的服务器的IP:")
    dest_port = int(input("请输入下载的服务器的PORT:"))

    # 链接服务器
    tcp_socket.connect((dest_ip, dest_port))

    # 获取下载的文件名
    download_file_name = input("请输入要下载的文件名:")

    # 将文件名发送给服务器
    tcp_socket.send(download_file_name.encode("utf-8"))

    # 接收文件中的数据
    recv_data = tcp_socket.recv(1024 * 1024) # 1024 = 1k, 1024 * 1024 = 1M

    if recv_data:
        # 保持接收数据到一个文件中
        with open("[new]" + download_file_name, "wb") as f:
            f.write(recv_data)
    # 关闭套接字
    tcp_socket.close()


if __name__ == "__main__":
    main()
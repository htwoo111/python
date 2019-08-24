import socket


def send_file_2_client(client_socket, client_addr):
    # 1.接收客户端发生过来的文件名
    file_name = client_socket.recv(1024).decode("gbk")
    print("客户端({})需要下载的文件是{}".format(str(client_addr), file_name))

    file_content = None
    # 2.打开并读取文件
    try:
        f = open(file_name, "rb")
        file_content = f.read()
    except Exception as ret:
        print("没有要下载的文件{}".format(file_name))

    # 3.发送数据给客户端
    # client_socket.send("hello".encode("gbk"))
    if file_content:
        client_socket.send(file_content)


def main():
    # 1.买个手机(创建套接字 socket)
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2.插入手机卡(绑定本地信息 bind)
    tcp_server_socket.bind(("", 7890))

    # 3.将手机设置为响铃模式(让默认的套接字由主动变为被动 listen)
    tcp_server_socket.listen(128)

    while True:
        # 4.等待别人的电话(等待一个客户端链接， accept)
        client_socket, client_addr = tcp_server_socket.accept()

        # 5.调用发送文件函数
        send_file_2_client(client_socket, client_addr)
        
        # 关闭套接字
        client_socket.close()
    tcp_server_socket.close()


if __name__ == "__main__":
    main()
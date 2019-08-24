import socket


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

        print(client_addr)
        print("")
        print(client_socket)

        # 接收客户端发生过来的数据
        recv_data = client_socket.recv(1024)
        print(recv_data.decode("gbk"))

        # 发送数据给客户端
        client_socket.send("hello".encode("gbk"))
        
        # 关闭套接字
        client_socket.close()
    tcp_server_socket.close()


if __name__ == "__main__":
    main()
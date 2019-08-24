import socket


def recv_msg(client_socket):
    """接收来自客户端的信息"""
    recv_data = client_socket.recv(1024)
    # print(recv_data.decode("gbk"))
    return recv_data


def send_msg(client_socket):
    """回送信息给客户端"""
    msg = input("请输入想要发送的信息：")
    client_socket.send(msg.encode("gbk"))

def main():
    # 创建套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # 绑定本地信息
    tcp_server_socket.bind(("", 7890))

    # 将套接字由主动转为被动
    tcp_server_socket.listen()

    # while循环服务客户端
    while True:
        # 等待客户端链接
        client_socket, client_addr = tcp_server_socket.accept()
        # while循环为同一客户多次服务
        while True:
            # 打印选项
            # print("-" * 50)
            # print("1.接收信息")
            # # print("2.发送信息")
            # print("0.退出服务")
            
            # op = input("请输入要进行的操作：")
            # if op == "1":
            recv_data = recv_msg(client_socket)
            if recv_data:
                print(recv_data.decode("gbk"))
            else:
                break
            # elif op =="2":
            #     send_msg(client_socket)
            # elif op =="0":
            #     break
            # else:
            #     print("输入错误")

        # 关闭客户端的套接字
        client_socket.close()

    # 关闭服务器的套接字
    tcp_server_socket.close()


if __name__ == "__main__":
    main()
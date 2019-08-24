import socket

def main():
    # 创建一个udp套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 绑定port
    udp_socket.bind(("", 8080))

    # 获取对方的ip/port
    dest_ip = input("请输入对方的ip:")
    dest_port = int(input("请输入对方的port："))

    # 从键盘获取数据
    send_data = input("请输入要发送的数据：")

    # 使用套接字收发数据
    udp_socket.sendto(send_data.encode("utf-8"), (dest_ip, dest_port))

    # 接收回送过来的数据
    recv_data = udp_socket.recvfrom(1024)
    print(recv_data)

    # 关闭套接字
    udp_socket.close()

if __name__ == "__main__":
    main()
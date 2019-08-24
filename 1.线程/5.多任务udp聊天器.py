import socket
import threading


def recv_msg(udp_socket):
    """"接收数据被显示"""
    # 接收数据
    while True:
        recv_data = udp_socket.recvfrom(1024)
        print("IP:{}:{}".format(recv_data[1], recv_data[0].decode("gbk")))


def send_msg(udp_socket, dest_ip, dest_port):
    """发送信息"""
    # 发送数据
    while True:
        send_data = input("请输入要发送的信息")
        udp_socket.sendto(send_data.encode("gbk"), (dest_ip, dest_port))



def main():
    """完成udp聊天器的整体控制"""

    # 创建套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 绑定本地信息
    udp_socket.bind(("", 7890))

    # 获取对方IP
    dest_ip = input("请输入对方IP：")
    dest_port = int(input("请输入对方端口："))

    # 创建两个线程去执行相应的功能
    # 1.创建接收线程
    t_recv = threading.Thread(target=recv_msg, args=(udp_socket,))
    # 2. 创建发送线程
    t_send = threading.Thread(target=send_msg, args=(udp_socket, dest_ip, dest_port))

    # 启动线程
    t_recv.start()
    t_send.start()


if __name__ == "__main__":
    main()
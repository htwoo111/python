import socket

def main():
    # 1.创建套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 2.绑定一个本地信息
    localaddr = ("", 7788)
    udp_socket.bind(localaddr)
    # 3。接收数据
    # 接收到的数据是一对元组("接收到的数据"，(ip, port))
    recv_data = udp_socket.recvfrom(1024) 
    recv_msg = recv_data[0]  # 存储接收到的信息
    recv_addr = recv_data[1]  # 存储发信人的信息
    # 4.打印接收到的数据
    print("来自{}的信息：{}".format(str(recv_addr), recv_msg.decode("gbk")))
    # 5.关闭套接字
    udp_socket.close()

if __name__ == "__main__":
    main()
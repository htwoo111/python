import socket

def main():
    # 创建一个udp套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    
        # 从键盘获取数据
        send_data = input("请输入要发送的信息：")

        # 使用套接字收发数据
        # 将(字符串)变量转换成字节，用encode
        udp_socket.sendto(send_data.encode("utf-8"), ip_and_port)
    

    # 关闭套接字
    udp_socket.close()

if __name__ == "__main__":
    main()
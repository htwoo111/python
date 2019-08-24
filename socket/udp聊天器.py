import socket

def send_msg(udp_socket):
        """发送信息"""
        # 获取要发送的内容
        dest_ip = input("请输入目标IP:")
        dest_port = int(input("请输入目标端口："))
        send_data = input("请输入要发送的信息：")
        udp_socket.sendto(send_data.encode("gbk"), (dest_ip, dest_port))

def recv_msg(udp_socket):
        """接收数据"""
        recv_data = udp_socket.recvfrom(1024)
        print("{}:{}".format(str(recv_data[1]), recv_data[0].decode("gbk"))) 

def main():
    # 创建套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 绑定信息
    udp_socket.bind(("", 7788))
            
    # while循环进行处理事情
    while True:
        print("---------xxx聊天器---------")
        print("1.发送信息")
        print("2.接收信息")
        print("0.退出系统")
        op = input("请输入现有的操作：")
        if op == "1":
            # 发送
            send_msg(udp_socket)
        elif op == "2":
            # 接收并显示
            recv_msg(udp_socket)
        elif op == "0":
            break
        else:
            print("输入有误")



if __name__ == "__main__":
    main()
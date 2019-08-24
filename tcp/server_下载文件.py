import socket

def send_data_2_client(client_socket, client_addr):
    # 接收客户端发送过来的文件名
    file_name = client_socket.recv(1024).decode("gbk")
    print("客户端：{}想要下载的文件是{}".format(client_addr, file_name))
    
    file_data = None
    # 尝试打开文件，若文件存在则读取，若文件不存在则打印错误
    try:
        f = open(file_name, "rb")
        file_data= f.read()
    except Exception:
        print("文件：{}不存在".format(file_name))

    # 判断是否读取到文件
    if file_data:
        client_socket.send(file_data)


def main():
    # 创建套接字
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # 绑定本地信息
    server_socket.bind(("", 7890))

    # 将套接字由自动转为被动接收数据
    server_socket.listen(128)

    # while循环对多个客户端进行服务
    while True:
        # 等待客户端链接
        print("开始服务...")
        client_socket, client_addr = server_socket.accept()

        # 回送客户端数据
        send_data_2_client(client_socket, client_addr)

        # 关闭客户端的套接字
        client_socket.close()
        print("完成当前服务...")
        
    # 关闭服务器的套接字
    server_socket.close()


if __name__ == "__main__":
    main()
import socket
import time

tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_server_socket.bind(("", 7890))
tcp_server_socket.listen(128)
tcp_server_socket.setblocking(False)  # 设置套接字为非堵塞状态

client_socket_list = list()

while True:
    time.sleep(1)
    try:
        new_socket, new_addr = tcp_server_socket.accept()
    except Exception:
        print("没有客户端链接")
    else:
        print("-----有新的客户端链接了-----")
        new_socket.setblocking(False)
        client_socket_list.append(new_socket)

    for client_socket in client_socket_list:
        try:
            recv_data = client_socket.recv(1024)
        except Exception:
            print("没有接收到客户端发过来的数据")
        else:
            if recv_data:
                print("客户端发送数据了！！！！！")
            else:
                client_socket.close()
                client_socket_list.remove(client_socket)
                print("客户端已经关闭")





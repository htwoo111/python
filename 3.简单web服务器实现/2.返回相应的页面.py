import socket

def service_client(client_socket):
    # 1.接收浏览器发送过来的请求，即http请求
    request = client_socket.recv(1024)
    print(request)
    # 2.返回http格式的数据给浏览器
    # 2.1准备发送给浏览器的数据 --headers
    response = "HTTP/1.1 200 OK\r\n"
    response += "\r\n"
    # 2.2准备发送给浏览器的数据 --body

    f = open("D:/python/3.web服务器/3.简单web服务器实现/html/index.html", "rb")
    html_content = f.read()
    f.close()

    # 将response header发送给浏览器
    client_socket.send(response.encode("utf-8"))
    # 将response body发送给浏览器
    client_socket.send(html_content)

    # 关闭套接字
    client_socket.close()


def main():
    """用来完成整体的控制"""
    # 创建套接字
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 绑定本地信息
    server_socket.bind(("", 8080))

    # 将套接字由主动转为被动接收数据
    server_socket.listen(128)
    
    while True:
        # 等待客户端链接
        client_socket, client_addr = server_socket.accept()
        
        # 为这个客户端服务
        service_client(client_socket)
    
    # 关闭监听套接字
    server_socket.close()
    



if __name__ == "__main__":
    main()
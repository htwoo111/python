import socket
import re


def service_client(new_socket, request):
    """为这个客户端返回数据"""
    # 1. 接收浏览器发送过来的请求 ，即http请求  
    request_lines = request.splitlines()
    print(">"*20)
    print(request_lines)

    # 用正则匹配用户访问的文件名
    file_name = ""
    ret = re.match(r"[^/]+(/[^ ]*)", request_lines[0])
    if ret:  # 匹配到字符串
        file_name = ret.group(1)
        if file_name == "/":
            file_name = "/index.html"

    # 2. 返回http格式的数据，给浏览器
    try:
        f = open("D:/python/3.web服务器/3.简单web服务器实现/html" + file_name, "rb")
    except:
        response = "HTTP/1.1 404 NOT FOUND\r\n"
        response += "\r\n"
        response += "------file not found-----"
        new_socket.send(response.encode("utf-8"))
    else:
        html_content = f.read()
        f.close()

        response_body = html_content 
        response_header = "HTTP/1.1 200 OK \r\n"
        response_header += "Content-Length:%d\r\n" % len(response_body)
        response_header += "\r\n"
        response = response_header.encode("utf-8") + response_body

        new_socket.send(response)
        new_socket.send(html_content)


def main():
    """用来完成整体的控制"""
    # 1. 创建套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # 2. 绑定
    tcp_server_socket.bind(("", 7890))

    # 3. 变为监听套接字
    tcp_server_socket.listen(128)
    tcp_server_socket.setblocking(False)  # 将套接字变为非堵塞

    # 创建一个空列表用来接收返回的客户端的套接字
    client_socket_list = list()
    while True:
        # 4. 等待新客户端的链接
        try:
            new_socket, client_addr = tcp_server_socket.accept()
        except Exception as ret:  # 由于套接字被设定为非堵塞，当没有客户端链接时，需要接收异常
            pass
        else:  # 如果有客户端链接，则将其套接字变为非堵塞， 同时在列表中添加其套接字
            new_socket.setblocking(False)
            client_socket_list.append(new_socket)

        # 遍历列表，对所有已链接的客户端接收数据 
        for client_socket in client_socket_list:
            try:
                recv_data = client_socket.recv(1024).decode("utf-8")
            except Exception as ret:  # 由于客户端的套接字被变为非堵塞，当客户端没有发送数据时，会出现异常
                pass
            else:
                if recv_data:
                    service_client(client_socket, recv_data)
                else:
                    client_socket.close()
                    client_socket_list.remove(client_socket)

    # 关闭监听套接字
    tcp_server_socket.close()


if __name__ == "__main__":
    main()
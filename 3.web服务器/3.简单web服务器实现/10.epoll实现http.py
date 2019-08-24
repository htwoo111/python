import socket
import re
import select


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

    # 创建一个epoll对象
    epl = select.epoll()

    # 将监听套接字对应的fd注册到epoll中
    epl.register(tcp_server_socket.fileno(), select.EPOLLIN)

    # 创建一个空列表用来接收返回的客户端的套接字
    fd_event_dict = dict()
    while True:

        fd_event_list = epl.poll()  # 默认会堵塞， 直到os检测到数据到来
        # [(fd, event)]
        for fd, event in fd_event_list:
            # 4. 等待新客户端的链接
            if fd == tcp_server_socket.fileno():
                new_socket, client_addr = tcp_server_socket.accept()
                epl.register(new_socket.fileno(), select.EPOLLIN)
                fd_event_dict[new_socket.fileno()] = new_socket
            elif event == select.EPOLLIN:
                recv_data = fd_event_dict[fd].recv(1024).decode("utf-8")
                if recv_data:
                    service_client(fd_event_dict[fd], recv_data)
                else:
                    fd_event_dict[fd].close()
                    epl.unregister(fd)
                    del fd_event_dict[fd]

    # 关闭监听套接字
    tcp_server_socket.close()


if __name__ == "__main__":
    main()
import re
import socket
import multiprocessing
import time


class WSGIServer(object):
    def __init__(self):
        # 创建套接字
        self.tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        # 绑定本地信息
        self.tcp_server_socket.bind(("", 7788))

        # 变为被动监听
        self.tcp_server_socket.listen(128)

    def service(self, client_socket):
        """对客户端服务的相应操作"""
        # 接收来自客户端的数据
        request_data = client_socket.recv(1024).decode("utf-8")
        request_lines = request_data.splitlines()
        # print(request_lines)

        # 用正则表达式匹配客户端访问的文件名
        ret = re.match(r"[^/]+(/[^ ]*)", request_lines[0])
        # 如果正则表达式有匹配的结果，则用文件名接收此结果
        file_name = ""
        if ret:
            file_name = ret.group(1)
            if file_name == "/":
                file_name = "/index.html"

        # 根据文件名打开相应文件，将html的数据发送给客户端
        if not file_name.endswith(".py"):
        # 如果请求的资源不是以.py结尾，那么就认为是静态资源(html/css/js/png.jpg等)
            try:
                f = open("D:/python/3.web服务器/3.简单web服务器实现/html" + file_name, "rb")
            except:
                response = "HTTP/1.1 404 NOT FOUND\r\n"
                response += "\r\n"
                response += "----file not found-----"
                client_socket.send(response.encode("utf-8"))
            else:
                # 读取文件数据
                file_content = f.read()
                # 给客户端响应
                response = "HTTP/1.1 200 OK\r\n"
                response += "\r\n"
                client_socket.send(response.encode("utf-8"))
                client_socket.send(file_content)
        else:
        # 如果是以.py结尾的那么就认为是动态资源的请求
            header = "HTTP/1.1 200 OK\r\n"
            header += "\r\n"

            body = "hello python %s" %time.ctime() 

            response = header + body
            # 发送response给浏览器
            client_socket.send(response.encode("utf-8"))

        # 关闭套接字
        client_socket.close()

    def run_forever(self):
        # 等待链接
        while True:
            client_socket = self.tcp_server_socket.accept()[0]

            p = multiprocessing.Process(target=self.service, args=(client_socket,))
            p.start()

            # 创建新进程，会重新复制一份资源，子进程调用close，但主进程还没有调用close
            # 这样导致四次挥手没有完成，客户端需要等待几分钟
            client_socket.close()
            # 为客户端服务
            # service(client_socket)

        # 关闭套接字
        self.tcp_server_socket.close()


def main():
    """控制整体，创建一个web服务器对象，调用这个对象的run_forever方法"""
    wsgi_server = WSGIServer()
    wsgi_server.run_forever()


if __name__ == "__main__":
    main()

import socket
import re
import multiprocessing
import dynamic.mini_frame_2
import sys


class WSGIServer(object):
    def __init__(self, port):
        # 1.创建套接字
        self.tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
        # 2.绑定IP和PORT
        self.tcp_server_socket.bind(("", port))
        # 3. 将套接字变为被动监听
        self.tcp_server_socket.listen(128)

    def service(self, client_socket):
        # 1.接收来自客户端发送过来的信息，并解码 recv
        recv_data = client_socket.recv(1024).decode("utf-8")
        # 2.对接收过来的信息进行切割行
        recv_data_line = recv_data.splitlines()
        # 3.用正则表达式匹配客户想要打开的文件名
        ret = re.match(r"[^/]+([^ ]*)", recv_data_line[0])
            # 3.1 如果匹配到信息则开始获取文件名
        file_name = ""
        if ret:
            file_name = ret.group(1)
            if file_name == "/":
                file_name = "/index.html"

        # 判断网页是否为静态网页
        # 如果是静态网页，则：
        if not file_name.endswith(".py"):
            # 4.打开文件
            # 4.1 try打开文件，判断文件是否存在
            try:
               f = open("D:/python/3.web服务器/3.简单web服务器实现/html" + file_name, "rb")
            # 4.2 except如果文件不存在，则返回给浏览器404(response, header)
            except:
                response = "HTTP/1.1 404 NOT FOUND\r\n"
                response += "\r\n"
                header = "------NOT FOUND------"
                response += header
                client_socket.send(response.encode("utf-8"))
            # 4.3 如果文件存在，则读取文件内容:
            else:
                content = f.read()
                f.close()
                response = "HTTP/1.1 200 OK\r\n"
                response += "\r\n"
                # 返回 content并发送response，header给浏览器
                client_socket.send(response.encode("utf-8"))
                client_socket.send(content)
        # 如果是动态网页，则调用满足WSGI的函数application：
        else:
            env = dict()
            env["PATH_INFO"] = file_name
            body = dynamic.mini_frame_2.application(env, self.set_response_header)
            header =  "HTTP/1.1 %s\r\n" % self.status
            for temp in self.headers:
                header += "%s:%s\r\n" % (temp[0], temp[1])
            header += "\r\n"
            # 设置回送给浏览器的response
            response = header + body
            # 回送response
            client_socket.send(response.encode("utf-8"))
        
        # 关闭客户端套接字
        client_socket.close()

    def set_response_header(self, status, headers):
        """接收application返回的字典和header"""
        self.status = status
        self.headers = headers

    def run(self):
        # 1.while循环为客户端服务
        while True:
            # 1.1调用accept方法开始为客户端服务
            client_socket, address = self.tcp_server_socket.accept()
            # 1.2 创建多进程，调用 service方法
            p = multiprocessing.Process(target=self.service, args=(client_socket,))
            # 1.3启动进程
            p.start()
            # 1.4关闭客户端套接字
            client_socket.close()
        # 2.关闭服务器的套接字
        self.tcp_server_socket.close()


def main():
    """主程序，创建wsgi类对象，让类对象执行run方法"""
    if len(sys.argv) == 2:
        try:
            port = int(sys.argv[1])
        except:
            print('端口输入错误')
            return
    else:
        print("请按照以下方式运行程序")
        print("python xxxx.py 1234")
        return

    wsgi_server = WSGIServer(port)
    wsgi_server.run()


if __name__ == "__main__":
    main()

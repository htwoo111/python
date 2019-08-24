# -*- codding:utf8 -*-
import time
import socket
import multiprocessing
import re
import sys
# import dynamic.mini_frame as mini_frame


class WSGIServer(object):
    def __init__(self, port, app, static_path):
        """初始化"""
        # 创建套接字
        self.tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # 绑定IP 和 PORT
        self.tcp_server_socket.bind(("", 7899))
        # 将套接字由主动变为被动监听
        self.tcp_server_socket.listen(128)
        
        self.application = app
        self.static_path = static_path

    def service(self, client_socket):
        """根据浏览器的请求，对浏览器进行服务"""
        # 接收来自浏览器的request headers
        recv_data = client_socket.recv(1024).decode("utf-8")
        recv_data_lines = recv_data.splitlines()
        print(recv_data_lines)
        # 获取用户向访问的文件名
        ret = re.match(r"[^/]+(/[^ ]*)", recv_data_lines[0])
        # print(ret.group(1))
        file_name = ""
        # 如果正则匹配到，则为文件名
        if ret:
            file_name = ret.group(1)
            if file_name == "/":
                file_name = "/index.html"
        else:
            print("输入的文件有误...")
        
        # 判断是否为静态请求 (文件名以.py结尾的则认为是动态)
        # 静态请求
        if not file_name.endswith(".html"):
            # 根据文件名打开相应的文件
            try:
                f = open(self.static_path + file_name, mode="rb")
            # 如果文件不存在，则返回给浏览器404
            except:
                response = "HTTP/1.1 404 NOT FOUND\r\n"
                response += "\r\n"
                # TODO(用于调试，调试完成，文件名记得删掉)    
                response += "-------NOT FOUND-------(%s)" % file_name
                client_socket.send(response.encode("utf-8"))
            else:
                content = f.read()
                f.close()
                response = "HTTP/1.1 200 OK\r\n"
                response += "\r\n"
                client_socket.send(response.encode("utf-8"))
                client_socket.send(content)

        # 动态请求
        else:
            # 定义一个字典，接收文件名，并返回给框架的application函数
            environ = dict()
            environ["PATH_INFO"] = file_name
            # print(environ)
            body = self.application(environ, self.recv_status_header)
            # 对从application返回过来的header进行处理
            header = "HTTP/1.1 %s\r\n" % self.status
            for temp in self.headers:
                header += "%s:%s\r\n" % (temp[0], temp[1])
                header += "\r\n"
            response = header + body
            client_socket.send(response.encode("utf-8"))

        # 关闭套接字
        client_socket.close()
            

    def recv_status_header(self, environ, headers):
        """根据wsgi协议，接收返回过来的字典(status)，和header"""
        # 接收返回过来的状态 200 OK
        self.status = environ
        self.headers = headers

    def run(self):
        """启动服务器"""
        # while 循环为浏览器服务
        while True:
            # accept 接收浏览器发送过来的请求
            client_socket, client_addr = self.tcp_server_socket.accept()
            # 使用多进程为浏览器进行服务 调用service 方法
            p = multiprocessing.Process(target=self.service, args=(client_socket,))
            # 启动进程
            p.start()
            # 关闭客户端套接字
            client_socket.close()
        # 关闭服务器套接字
        self.tcp_server_socket.close()            


def main():
    """主函数，创建wsgi服务器对象，并调用run方法"""
    if len(sys.argv) == 3:
        try:
            port = int(sys.argv[1])  # 7890
            frame_app_name = sys.argv[2]  # mini_frame:application
        except Exception as ret:
            print("端口输入错误。。。。。")
            return
    else:
        print("请按照以下方式运行:")
        print("python3 xxxx.py 7890 mini_frame:application")
        return

    # mini_frame:application
    ret = re.match(r"([^:]+):(.*)", frame_app_name)
    if ret:
        frame_name = ret.group(1)  # mini_frame
        app_name = ret.group(2)  # application
    else:
        print("请按照以下方式运行:")
        print("python3 xxxx.py 7890 mini_frame:application")
        return

    with open("./web_server.conf") as f:
        conf_info = eval(f.read())
    # 此时 conf_info是一个字典里面的数据为：
    # {
    #     "static_path":"./static",
    #     "dynamic_path":"./dynamic"
    # }
    sys.path.append(conf_info['dynamic_path'])

    # import frame_name --->找frame_name.py
    frame = __import__(frame_name)  # 返回值标记这 导入的这个模板
    app = getattr(frame, app_name)  # 此时app就指向了 dynamic/mini_frame模块中的application这个函数



    # 创建wsgi_server 对象
    wsig_server = WSGIServer(port, app, conf_info['static_path'])
    # 调用wsgi_server对象的run方法
    wsig_server.run()


if __name__ == "__main__":
    main()



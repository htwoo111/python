# 创建一个字典，来接收向装饰器传递的文件名
FUNC_DICT = dict()
def route(url):
    """对装饰器再度装饰，获取文件名"""
    def set_func(func):
        FUNC_DICT[url] = func
        """设置一个装饰器，获取函数的引用"""
        def call_func(*args, **kwargs):
            return func(*args, **kwargs)
        return call_func
    return set_func

@route("/login.html")
def login():
    """返回登录页面"""
    return "this is login page, welcome"

@route("/index.html")
def index():
    """返回索引页面"""
    return "this is index page"


def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html;charset=utf-8')])
    file_name = environ["PATH_INFO"]
    try:
        func = FUNC_DICT[file_name]
        return func()
    except Exception as ret:
        return "mini_frame 产生异常：%s" % ret
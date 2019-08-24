def login():
    """返回登录页面"""
    return "this is login page"


def index():
    """返回索引页面"""
    return "this is index page"


def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html;charset=utf-8')])
    if environ["PATH_INFO"] == "/index.py":
        return index()
    elif environ["PATH_INFO"] == "/login.py":
        return login()
    return "mini_frame_application"
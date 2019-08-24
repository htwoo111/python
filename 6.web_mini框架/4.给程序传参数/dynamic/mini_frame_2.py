def index():
    with open("D:/python/6.web_mini框架/3.解耦/templates/center.html") as f:
        content = f.read()
    return content

def login():
    return '这是登录'

def center():
    with open("D:/python/6.web_mini框架/3.解耦/templates/index.html") as f:
        return f.read()

def application(env, start_response):
    start_response('200 OK', [('Content-Type', 'text/html;charset=utf-8')])
    file_name = env['PATH_INFO']
    if file_name == '/index.py':
        return index()
    elif file_name == '/center.py':
        return center()
    else:
        return 'Hello World 哈哈'

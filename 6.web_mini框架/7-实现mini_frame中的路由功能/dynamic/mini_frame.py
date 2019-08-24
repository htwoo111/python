import re 
# URL_FUNC_DICT = {
#     "/index.py" : index,
#     "/center.py" : center
# }

# 定义一个字典根据用户想要打开的文件名返回相应函数的引用
URL_FUNC_DICT = dict()

# 对装饰器再度装饰
def route(url):
    # 定义一个装饰器，对函数装饰的同时，获取函数的引用
    def set_func(func):
        # 根据文件名网字典里面添加函数的引用
        URL_FUNC_DICT[url] = func
        def call_func(*args, **kwargs):
            return func(*args, **kwargs)
        return call_func
    return set_func

@route("/index.py")
def index():
    with open("./templates/index.html") as f:
        content = f.read()
    
    my_stock_info = "哈哈哈 这是你本月名词"
    content = re.sub(r"\{%content%\}", my_stock_info, content)
    return content

@route("/center.py")
def center():
    with open("./templates/center.html") as f:
        content = f.read()

    my_stock_info = "哈哈哈 这是mysql"
    content = re.sub(r"\{%content%\}", my_stock_info, content)
    return content



def application(env, start_respoense):
    start_respoense('200 OK', [('Content-Type', 'text/html;charset=utf-8')])
    file_name = env['PATH_INFO']

    # 判断文件名是否在字典里
    try:
        func = URL_FUNC_DICT[file_name]
        return func()
    except Exception as ret:
        return '产生异常 %s' % ret
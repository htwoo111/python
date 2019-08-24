import re
from pymysql import connect


def set_mysql():
    """用来执行sql语句，返回(cursor, conn)"""
    conn = connect(host='localhost',port=3307,user='root',password='htwoo111',
                   database='stock_db',charset='utf8')
    cursor = conn.cursor()
    return (cursor, conn)


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

@route("/center.html")
def center():
    """返回用户中心页面"""
    with open("./1.wsgi_server/templates/center.html", encoding="utf-8") as f:
        content = f.read()
    cursor, conn = set_mysql()
    sql = "select i.code,i.short,i.chg,i.turnover,i.price,i.highs,f.note_info from info as i inner join focus as f on i.id=f.info_id;"
    cursor.execute(sql)
    all_stock_info = cursor.fetchall()  # 去出来的是元组
    # 关闭mysql
    cursor.close()
    conn.close()
# 从前端获取模板
    tr = """<tr>
            <td>{0}</td>
            <td>{1}</td>
            <td>{2}</td>
            <td>{3}</td>
            <td>{4}</td>
            <td>{5}</td>
            <td>{6}</td>
            <td>
                <a type="button" class="btn btn-default btn-xs" href="/update/{7}.html"> <span class="glyphicon glyphicon-star" aria-hidden="true"></span> 修改 </a>
            </td>
            <td>
                <input type="button" value="删除" id="toDel" name="toDel" systemidvaule="{8}">
            </td>
        </tr>
    """
    return_tr = ""
    for stock_info in all_stock_info:
        return_tr += tr.format(stock_info[0], stock_info[1], stock_info[2], stock_info[3],
                     stock_info[4], stock_info[5], stock_info[6], stock_info[1], stock_info[1])

    # 对html匹配到的内容进行修改,将查询到的股票信息传入
    content = re.sub(r"\{%content%\}", return_tr, content)
    return content

@route("/index.html")
def index():
    """返回索引页面"""
    with open("./1.wsgi_server/templates/index.html", encoding="utf-8") as f:
        content = f.read()
    # 执行sql语句，查询股票信息
    cursor, conn = set_mysql()
    sql = "select * from info;"
    cursor.execute(sql)
    all_stock_info = cursor.fetchall()  # 去出来的是元组
    # 关闭mysql
    cursor.close()
    conn.close()
    # 从前端获取模板
    tr = """<tr>
            <td>{0}</td>
            <td>{1}</td>
            <td>{2}</td>
            <td>{3}</td>
            <td>{4}</td>
            <td>{5}</td>
            <td>{6}</td>
            <td>{7}</td>
            <td>
                <input type="button" value="添加" id="toAdd" name="toAdd" systemidvaule="{8}">
            </td>
            </tr>
    """
    return_tr = ""
    for stock_info in all_stock_info:
        return_tr += tr.format(stock_info[0], stock_info[1], stock_info[2], stock_info[3],
                     stock_info[4], stock_info[5], stock_info[6], stock_info[7], stock_info[1])

    # 对html匹配到的内容进行修改,将查询到的股票信息传入
    content = re.sub(r"\{%content%\}", return_tr, content)
    return content
    

def application(environ, start_response):
    """主函数，wsgi协议的application"""
    start_response('200 OK', [('Content-Type', 'text/html;charset=utf-8')])
    file_name = environ["PATH_INFO"]
    try:
        func = FUNC_DICT[file_name]
        return func()
    except Exception as ret:
        return "mini_frame 产生异常：%s" % ret
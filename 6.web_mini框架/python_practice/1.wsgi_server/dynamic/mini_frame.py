# -*- codding:utf8 -*-
import re
from pymysql import connect
import urllib.parse


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

@route(r"/center.html")
def center(ret):
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
                     stock_info[4], stock_info[5], stock_info[6], stock_info[0], stock_info[0])

    # 对html匹配到的内容进行修改,将查询到的股票信息传入
    content = re.sub(r"\{%content%\}", return_tr, content)
    return content


@route(r"/index.html")
def index(ret):
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
    

@route(r"/add/(\d+)\.html")
def add_focus(ret):
    """添加关注"""
    # 获取股票代码
    stock_code = ret.group(1)

    cursor, conn = set_mysql()
    # 1.判断要关注的股票是否存在
    sql = """select * from info where code=%s;"""
    cursor.execute(sql, args=(stock_code,))
    # 如果查询为empty，说明查询的股票不存在
    if not cursor.fetchone():
        cursor.close()
        conn.close()
        return "对不起，这个股票不存在....大哥，我们是创业公司，给条生路...."

    # 2.判断要关注的股票是否已经关注过了
    sql = """select * from info as i  inner join focus as f on i.id=f.info_id where i.code=%s;"""
    cursor.execute(sql, args=(stock_code,))
    # 判断是否已经关注过，关注过则为True
    if cursor.fetchone():
        cursor.close()
        conn.close()
        return "对不起，这个股票您已经关注过了..."
    
    # 3.关注股票
    sql = """insert into focus(info_id) select id from info where code=%s;"""
    cursor.execute(sql, args=(stock_code,))
    conn.commit()

    # 关闭mysql
    cursor.close()
    conn.close()
    return "关注成功"


@route(r"/del/(\d+)\.html")
def del_focus(ret):
    """删除关注"""
    # 获取股票代码
    stock_code = ret.group(1)

    cursor, conn = set_mysql()
    # 1.判断要删除关注的股票是否存在
    sql = """select * from info where code=%s;"""
    cursor.execute(sql, args=(stock_code,))
    # focus_info = cursor.fetchone()  
    # 如果查询为empty，说明查询的股票不存在
    # if not focus_info:
    
    if not cursor.fetchone():
        cursor.close()
        conn.close()
        return "对不起，这个股票不存在....大哥，我们是创业公司，给条生路...."
    
    # 2.删除股票
    sql = """delete from focus where info_id=(select id from info where code=%s);"""
    cursor.execute(sql, args=(stock_code,))
    conn.commit()

    # 关闭mysql
    cursor.close()
    conn.close()
    return "删除成功"


@route(r"/update/(\d+)\.html")
def update(ret):
    # 打开update.html页面
    with open("./1.wsgi_server/templates/update.html", encoding="utf-8") as f:
        content = f.read()
    # 获取股票代码
    stock_code = ret.group(1)
    # 获取conne 和 cursor
    cursor, conn = set_mysql()
    
    # 显示更新页的股票备注
    sql = "select note_info from focus where info_id=(select id from info where code=%s);"
    cursor.execute(sql, args=(stock_code,))
    note_info = cursor.fetchone()[0]  # 去出来的是元组
    # 关闭mysql
    cursor.close()
    conn.close()
    # 替换update.html里面需要{%code%} 和 {%note_info%}
    content = re.sub(r"\{%code%\}", stock_code, content)
    content = re.sub(r"\{%note_info%\}", note_info, content)
    return content


@route(r"/update/(\d+)/(.*)\.html")
def update_note(ret):
    # 获取股票代码
    stock_code = ret.group(1)
    # 获取股票备注信息
    note_info_v1 = ret.group(2)  # 返回str, 输入中文时，浏览器会对中文进行编码
    # 对note_info进行解析，防止出现中文乱码
    note_info_v2 = urllib.parse.unquote(note_info_v1)
    # 获取conne 和 cursor
    cursor, conn = set_mysql()
    
    # 2.修改数据库里focus 的 note_info
    sql = "update focus set note_info=%s where info_id=(select id from info where code=%s);"
    cursor.execute(sql, args=(note_info_v2, stock_code))
    # 提交sql语句
    conn.commit()
    # 关闭mysql
    cursor.close()
    conn.close()
    return "修改成功"

def application(environ, start_response):
    """主函数，wsgi协议的application"""
    start_response('200 OK', [('Content-Type', 'text/html;charset=utf-8')])
    file_name = environ["PATH_INFO"]
    try:
        # func = FUNC_DICT[file_name]
        # return func()
        for url, func in FUNC_DICT.items():
            # {
            #   r"/index.html":index,
            #   r"/center.html":center,
            #   r"/add/\d+\.html":add_focus
            # }
            ret = re.match(url, file_name)
            if ret:
                return func(ret)
        else:
            return "请求的url(%s)没有对应的函数" % url
    except Exception as ret:
        return "mini_frame 产生异常：函数/文件%s" % ret
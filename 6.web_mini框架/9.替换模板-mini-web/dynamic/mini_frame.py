import re 
from pymysql import connect
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

@route("/index.html")
def index():
    with open("./templates/index.html") as f:
        content = f.read()
    
    # my_stock_info = "哈哈哈 这是你本月名词"
    # content = re.sub(r"\{%content%\}", my_stock_info, content)
    # 连接mysql数据库
    conn = connect(host='localhost',port=3307,user='root',password='htwoo111',database='stock_db',charset='utf8')
    cs = conn.cursor()
    cs.execute("select * from info;")
    stock_infos = cs.fetchall()
    cs.close()
    conn.close()
    # 设置TR模板
    
    tr_template = """<tr>
        <td>{}</td>
        <td>{}</td>
        <td>{}</td>
        <td>{}</td>
        <td>{}</td>
        <td>{}</td>
        <td>{}</td>
        <td>{}</td>
        <td>
            <input type="button" value="添加" id="toAdd" name="toAdd" systemidvaule="000007">
        </td>
        </tr>
        """
    html = ""
    for line_info in stock_infos:
        html += tr_template.format(line_info[0],line_info[1],line_info[2],line_info[3],line_info[4],line_info[5],line_info[6],line_info[7])


    content = re.sub(r"\{%content%\}", html, content)
    return content

@route("/center.html")
def center():
    with open("./templates/center.html") as f:
        content = f.read()

    my_stock_info = "哈哈哈 这是mysql"
    # 连接mysql数据库
    conn = connect(host='localhost',port=3307,user='root',password='htwoo111',database='stock_db',charset='utf8')
    cs = conn.cursor()
    cs.execute("select i.code,i.short,i.chg,i.turnover,i.price,i.highs,f.note_info from info as i inner join focus  as f on i.id=f.info_id;")
    stock_infos = cs.fetchall()
    cs.close()
    conn.close()
    
    # 设置TR模板
    tr_template = """
        <tr>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>
                <a type="button" class="btn btn-default btn-xs" href="/update/300268.html"> <span class="glyphicon glyphicon-star" aria-hidden="true"></span> 修改 </a>
            </td>
            <td>
                <input type="button" value="删除" id="toDel" name="toDel" systemidvaule="300268">
            </td>
        </tr>
    """

    html = ""
    for line_info in stock_infos:
        html += tr_template.format(line_info[0],line_info[1],line_info[2],line_info[3],line_info[4],line_info[5],line_info[6])


    content = re.sub(r"\{%content%\}", html, content)
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
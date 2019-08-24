from pymysql import connect

pw = input("请输入密码：")
# 连接mysql
conn = connect(host='localhost',
               port=3307, user='root', password=pw,
               database='python_test', charset='utf8')

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = conn.cursor()

# 通过execute('sql语句') 执行sql语句
cursor.execute('select * from students')  # 返回查询到的行数，不显示数据

# 取查询的结果
cursor.fetchall()
# cursor.fecchmany(n) 取n个，不写取0个
cursor.fetchmany()
# 一条一条取，会记录上一次查询的数据
cursor.fetchone()

# 先关闭游标，在关闭连接
cursor.close()
conn.close()

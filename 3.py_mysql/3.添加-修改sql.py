from pymysql import connect


conn = connect(host='localhost', user='root', password='htwoo111',
               port=3307, database='jing_dong', charset='utf8')
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = conn.cursor()
# 执行sql语句
cursor.execute("""insert into goods_cates (name) values ("硬盘");""")

# 执行之后一定要提交，不提交则作废
conn.commit()

cursor.execute("""insert into goods_cates (name) values ("硬盘-1");""")
cursor.execute("""insert into goods_cates (name) values ("硬盘-2");""")
# 返回前一次commit，即上面的sql语句无效
conn.rollback()

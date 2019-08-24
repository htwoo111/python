from pymysql import connect


class JD(object):
    def __init__(self):
        # 连接mysql
        self.conn = connect(host='localhost', user='root', password='htwoo111',
                            port=3307, database='jing_dong', charset='utf8')
        # 创建游标对象 cursor
        self.cursor = self.conn.cursor()

    # def __del__(self):
    #     """完成关闭游标，关闭连接"""
    #     self.cursor.close()
    #     self.conn.close()

    def execute_sql(self, sql):
        """执行sql语句"""
        self.cursor.execute(sql)
        for temp in self.cursor.fetchall():
            print(temp)

    def show_all(self):
        """显示所有商品"""
        # 接收想要执行的sql语句 sql
        sql = 'select * from goods;'
        # 调用execute()方法，执行sql语句
        self.execute_sql(sql)

    def show_cates(self):
        """显示所有商品的分类"""
        # 接收想要执行的sql语句 sql
        sql = 'select name from goods_cates;'
        # 调用execute()方法，执行sql语句
        self.execute_sql(sql)

    def show_brands(self):
        # 接收想要执行的sql语句 sql
        sql = 'select brand from goods_brands;'
        # 调用execute()方法，执行sql语句
        self.execute_sql(sql)

    def add_brand(self):
        item_name = input("输入新商品分类的名称：")
        sql = """insert into goods_brands (brand) values ("%s")""" % item_name
        self.cursor.execute(sql)
        self.conn.commit()

    def get_info_by_name(self):
        find_name = input("请输入要查询的商品名字:")
        # sql = """select * from goods where name='%s';""" % find_name
        # print("---------%s---------" % sql)
        # self.execute_sql(sql)
        sql = "select * from goods where name=%s"
        self.cursor.execute(sql, [find_name])
        print(self.cursor.fetchall)

    @staticmethod
    def print_menu():
        """打印菜单"""
        print("-------京东商城--------")
        print("1.显示所有商品")
        print("2.显示所有商品的分类")
        print("3.显示所有品牌")
        print("4.添加一个商品的分类")
        print("5.根据名字查询商品信息:")
        print("0.进入订单页面")
        op = input("请输入要进行的操作:")
        return op

    def run(self):
        # while 循环让顾客多次查询
        while True:
            # 调用打印选项方法，并返回顾客想要进行的操作选项
            op = self.print_menu()
            if op == "1":
                # 查询所有商品
                self.show_all()
            elif op == "2":
                # 查询所有商品的分类
                self.show_cates()
            elif op == "3":
                # 查询所有品牌
                self.show_brands()
            elif op == "4":
                # 添加品牌分类
                self.add_brand()
            elif op == "5":
                self.get_info_by_name()
            elif op == "0":
                # self.__del__()
                break
            else:
                print("输入有误，请重新输入！")


def main():
    # 创建一个jd的类
    jd = JD()
    # 调用jd的run方法，让其运行
    jd.run()


if __name__ == "__main__":
    main()

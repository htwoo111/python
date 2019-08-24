from pymysql import connect


class JD(object):
    def __init__(self):
        # 调用connect方法，链接mysql，conn接收返回结果
        self.conn = connect(host='localhost', port=3307, user='root',
                            password='htwoo111', database='jing_dong',
                            charset='utf8')
        # 调用cursor方法, 创建游标对象 cursor
        self.cursor = self.conn.cursor()

    def __del__(self):
        # 关闭游标，关闭链接
        self.cursor.close()
        self.conn.close()

    def execute_sql(self, sql):
        """执行操作"""
        self.cursor.execute(sql)
        # 遍历打印商品信息
        for temp in self.cursor.fetchall():
            print(temp)

    def show_all_items(self):
        """显示所有的商品"""
        sql = "select * from goods;"
        self.execute_sql(sql)

    def show_cates(self):
        """显示商品的分类"""
        sql = "select name from goods_cates;"
        self.execute_sql(sql)

    def show_brands(self):
        """显示所有商品的品牌"""
        sql = "select brand from goods_brands;"
        self.execute_sql(sql)

    @staticmethod
    def print_menu():
            print("-------京东商城-------")
            print("1.所有的商品")
            print("2.所有的商品分类")
            print("3.所有的商品品牌分类")
            print("---------------------------------------")
            return input("请输入要执行的操作：")

    def run(self):
        while True:
            op = self.print_menu()
            if op == "1":
                # 查询所有商品
                self.show_all_items()
            elif op == "2":
                # 查询分类
                self.show_cates()
            elif op == "3":
                # 查询所有品牌分类
                self.show_brands()
            else:
                # 错误处理
                print("输入错误，请重新输入")


def main():
    # 1.创建一个京东商城的类对象 jing_dong
    jing_dong = JD()
    # 2.调用类对象的run方法，运行
    jing_dong.run()


if __name__ == "__main__":
    main()

from pymysql import connect


def main():
    conn = connect(host='localhost', user='root', password='htwoo111',
                   port=3307, database='python_test', charset='utf8')

    cursor = conn.cursor()

    for i in range(100000):
        cursor.execute("insert into test values('haha %d')" % i)
        print("第{}条".format(i))

    conn.commit()


if __name__ == "__main__":
    main()

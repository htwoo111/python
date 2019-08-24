<<高性能msql>>






-- 数据库的操作

    -- 链接数据库
    mysql -uroot -p
    mysql -uroot -p[password]

    -- 退出数据库
    exit/quit/ctrl + c

    -- 显示当前数据库版本
    select version();
    -- 显示当前数据库时间
    select now();

    -- 显示所有的数据库
    show databases;

    -- 创建数据库
    -- create database 数据库名 charset=utf8;
    create database python04 charset=utf8;

    -- 查看创建数据库的语句
    -- show create database 数据库名
    show create database python04;

    -- 删除数据库
    -- drop database `数据库名` # 如果数据库名含特殊符号是添加`[tab键上面的]
    drop database python04





    -- 查看当前使用的数据库
    select database();

    -- 选择使用数据库
    -- use 数据库名
    use python04;

    -- 查看当前数据库所有的表
    show tables;

    -- 创建表
    -- create table 数据表名 (字段 类型 约束[, 字段 类型， 约束])
    -- 创建classes表(id, name)
    create table classes (id int, name varchar(30));
    -- 创建xxx表, 两个字段(id, name) id的类型int 约束(主键, 非空，自动增长)
    create table xxx(
        id int primary key not null auto_increment,
        name varchar(30)
        );

    -- 创建students表(id, name, age, high, gender, cls_id)
    create table students (
        id int unsigned primary key not null auto_increment,
        name varchar(20),
        age tinyint unsigned,  -- （0，255）整数 ，unsigned表示非负 
        high decimal(5,2),     -- decimal(5,2) 5位数，其中两位为小数
        gender enum("男", "女", "保密") default "保密",  -- enum() 枚举，从里面选 默认为保密
        cls_id int unsigned
    );

--------------------------------------------------------------------------

    -- 往数据表插入数据
    insert into students values(0, "xiaoming", 18, 166.9, "男", 1);
    -- 查看数据
    select * from 数据表名;

    -- 修改-添加字段
    -- alter table 表名 add 字段 类型;
    alter table students add birthday datetime;

    -- 修改表-修改字段，不不不不重命名版
    -- alter table 表名 modify 字段名 类型
    alter table students modify birthday date; -- 将students 中birthday字段的类型由datetime改为date

    -- 修改表-修改字段，重命名版
    -- alter table 表名 change 原名 新名 类型和约束;
    alter table students change birthday birth date default "2000-01-01";

    -- 修改表-删除字段
    -- alter table students drop 字段名;
    alter table students drop high; 

    -- 删除数据表
    drop table 数据表名：

    -- 查看一个数据表的结构
    -- desc 数据表名
    desc python04
    


----------------------------------------------------------------------
-- 数据表的增删改查 CURD create update read delete

-- 增加
    -- insert into 表名 values();
    insert into classes values(1,"菜鸟班")

+----+----------+------+--------+--------+------------+
| id | name     | age  | gender | cls_id | birth      |
+----+----------+------+--------+--------+------------+
|  1 | xiaoming |   18 | 男     |      1 | NULL       |
|  2 | laowang  |   18 | 女     |     11 | 2000-11-23 |
+----+----------+------+--------+--------+------------+ 
    insert into students values(0, 18, "男", 21, "2000-06-04")
    insert into students values(null, 18, "男", 21, "2000-06-04")
    insert into students values(default, 18, "男", 21, "2000-06-04")

    -- 字段的约束条件有枚举的话，可以用1,2,3..选择，但不能超过枚举的数量
    insert into students values(0, 18, 1, 21, "2000-06-04")

    -- 字段中只插入部分
    -- insert into 表名 (字段名,[]) values(属性,[])
    insert into students (name, gender) values("小乔", "女");
    -- 多行插入
    insert into students (name, gender) values("小乔", "女"),("貂蝉","女");
    insert into students values(0, "赵信", 18, "男", 21, "2000-06-04"),
    (0, "梨花", 10, "男", 222, "1999-02-01")


-- 修改
    -- 匹配修改,只修改一个
    -- update 数据表名 set 字段名=[];
    update students set gender="女" ;
    -- update 数据表名 set 字段名=[] where id=[]; 一般where后面用主键锁定位置
    update students set gender="女" where id=1;
    update students set gender="女" where name="效力";

    -- 匹配修改，修改多个
    -- update 数据表名 set 字段名=[],字段名=[] where id=[];


-- 查询
    -- 查询所有字段
    -- select * from 表名
    select * from students
    -- select * from 表名 where 字段名=[];
    select * from students where id=6; -- 查询id=6的所有
    select * from students where id>6; -- 查询id=6的所有
    -- 查询指定字段
    -- select 字段名,[] from 表名 [where];
    select name,gender from students;
    -- select 字段名 as 别名, [] as [] from 表名 [where];
    -- 哪个字段名先写，哪个显示在前面
    select name as "姓名",gender as "性别" from students;
    select gender as "性别",name as "姓名" from students;


-- 删除数据
    -- 删除数据表
    -- delete from 数据表名;
    delete from students; --整个数据表中的数据全部删除
    -- delete from 数据表名 where [] -- 匹配删除


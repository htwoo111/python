-- 数据的准备
    -- 创建一个数据库
    create database python_test charset=utf8;
    
    -- 使用一个数据库
    use python_test;

    -- 显示当前使用的数据库
    select database();

    -- 创建一个数据表  
    -- students表
    create table students(
        id int unsigned primary key auto_increment not null,
        name varchar(20) default '',
        age tinyint unsigned default 0,
        height decimal(5,2),
        gender enum("男", "女", "中性", "保密") default "保密",
        cls_id int unsigned default 0,
        is_delete bit default 0
    );

    -- classes表
    create table classes(
        id int unsigned auto_increment primary key not null,
        name varchar(30) not null
    );

    -- 插入数据
        -- students
        insert into students values
        (0, "小明", 18, 180.00, 2, 1, 0),
        (0, "小明月", 18, 180.00, 2, 2, 1),
        (0, "彭于晏", 29, 185.00, 1, 1, 0),
        (0, "刘德华", 59, 175.00, 1, 2, 1),
        (0, "黄蓉", 38, 160.00, 2, 1, 0),
        (0, "凤姐", 28, 180.00, 4, 2, 1),
        (0, "王祖贤", 18, 172.00, 2, 1, 1),
        (0, "周杰伦", 36, null, 1, 1, 0),
        (0, "程坤", 27, 181.00, 1, 2, 0),
        (0, "刘亦菲", 25, 166.00, 2, 2, 0),
        (0, "金星", 33, 162.00, 3, 3, 1),
        (0, "静香", 12, 180.00, 2, 4, 0),
        (0, "郭靖", 12, 170.00, 1, 4, 0),
        (0, "周杰", 34, 176.00, 2, 5, 0);
        -- classes
        insert into classes values
        (0, "python_01期"),
        (0, "python_02期"),
        (0, "python_04期");


-- 查询
    -- 1.基本查询
        -- 查询所有字段
        select * from 表名;
        select * from students;
        select * from classes;
        
        -- 查询指定字段
        -- select 字段1，字段2 ... from 表名；
        select name,age from students;

        -- 使用 as 给字段起别名
        -- select 字段1 as 别名1，字段2 as 别名2 ... from 表名；
        select name as 姓名,age as 年龄 from students;

        --select 表名.字段 ... from 表名；
        select students.name, students.age from students;

        -- 可以通过 as 给表起别名
        -- select 别名.字段 ....from 表名 as 别名;
        select s.name, s.age from students as s;

        -- 去重 查询
        -- select distinct 字段1 ... from 表名；
        select distinct gender from students;

    -- 2.条件查询
        -- 比较查询
            -- >
            -- 查询大于18岁的信息 
            select * from students where age>18;

            -- <
            select * from students where age<18;
            -- >=
            -- <=
            -- =
            select * from students where age=18;  -- python里面判断等否等于是用==
            -- !=
            select * from students where age != 18;

        -- 逻辑运算符
            -- and
            select * from students where age>18 and is_delete = 0;
            -- or
            -- 18岁以上或者身高大于180的
            select * from students where age>18 or height >180.00;
            -- not
            -- 不在 18岁以上的女性 这个范围
            select * from students where not (age>18 and gender="女性");
        -- 模糊查询
            -- like
            -- % 替代1个或者多个
            -- _替代1个

            -- 查询姓名中，已“小”开头的名字
            select name from students where name like"小%"; 
            -- c查询两个字的名字  
            select name from students where name like "__";

            -- rlike 正则表达式
            -- 查询以 周开始的姓名
            select name from students where name rlike "^周.*";
            -- 查询以周开头，以伦结尾的
            select name from students where name rlike "^周.*伦$";

    -- 3.范围查找
        -- in()表示在一个非连续的范围里
            -- 查询在18，34，12岁的人
            select name,age from students where age=18 or age=34 or age=12;
            select name,age from students where age in (18,34,12);
            
            -- not in 不在非连续的范围里
            select name,age from students where age not in (18,34,12);

            -- between .. and .. 在连续的范围内
            -- 查询[12,34] 包括12，34
            select name,age from students where age between 12 and 34;
            -- not between ... and ... 不在连续的范围内 

        -- 空判断
            -- 为空 is null
            -- 判断身高为空
            select * from students where height is null;

            -- 不为空 is not null
            -- 判断身高不为空
            select * from students where height is not null;

    -- 4.排序
        -- order by 字段名  (默认从小到大排序)
            -- asc 从小到大排序，即升序
            -- dasc 从大到小排序，即降序

            -- 查询年龄在18到34岁之间的女性，按年龄从小到大排序
            select name,
            age from students where 
            (age between 18 and 34) and gender=2 order by age;

            -- 查询年龄在18到34岁之间的女性，按年龄从大大大大到小排序
            select name,
            age from students where 
            (age between 18 and 34) and gender=2 order by age desc;

        -- order by 多个字段
            -- 查询年龄在18到34岁之间的女性，身高从高到矮排序，
            -- 如果身高相同的情况下年龄从小到大排序；哪个先写排哪个
            select * from students where 
            (age between 18 and 34) and gender=2 
            order by height desc,age asc;
            
            -- 按照年龄从小到大,身高从高到矮的排序
            select * from students order by age asc,height desc;

    -- 5.聚合函数
        -- count() 总数
        -- 查询男性有多少人，女性有多少人
        select count(*) from students where gender=1;
        select count(*) from students where gender=2;

        -- max() 最大值
        -- 查询年龄最大的
        select max(age) from students;

        -- 查询女性最高身高
        select max(height) from students where gender=2;

        -- min() 最小值

        -- sum() 求和
        -- 计算所有人的年龄总和
        select sum(age) from students;

        -- avg() 平均值
        -- 计算平均年龄
        select avg(age) from students;
        select sum(age)/count(age) from students;

        -- round(值,保留的位数) 四舍五入保留
        -- 计算所有人的平均年龄，保留一位小数
        select round(avg(age),1) from students;

        -- 计算男性的平均身高，保留两位小数
        select round(avg(height),2) from students where gender=1;

    -- 6.分组(一般和聚合函数一起用)
        -- group by
        -- 按照性别分组，查询所有的性别
        select gender from students group by gender;
        -- 按照性别分组，查询所有的性别,并统计认识
        select gender,count(*) from students group by gender;
        select gender,avg(age) from students group by gender;
        
        -- group_concat(...)
        -- 查询同种性别中的姓名
        select gender,group_concat(name) from students group by gender;
        -- 计算男性人数
        -- select gender,count(*) from students where gender=1 group by gender;
        select gender,group_concat(name,age,id) from students group by gender;
        select gender,group_concat(name," ",age," ",id) from students group by gender;

        -- having
        -- 查询平均年龄超过30岁的性别，以及姓名 having avg(age)>30;
        select gender,group_concat(name),round(avg(age),1) 
        from students 
        group by gender having avg(age)>30;
        -- 查询每种性别中的人数多于2个的信息
        select gender,group_concat(name) 
        from students 
        group by gender having count(*)>2;

    -- 7.分页
        -- limit [count] 限制查询个数
        -- 查询5个数据
        select * from students limit 5;
        
        -- limit [start], [count] 从start+1开始 限制显示count个
        -- 从第4个开始，显示5个数据
        select * from students limit 3,5;
        -- 每页显示2个，第1页面
        select * from students limit 0,2;
        -- 每页显示2个，第2页面
        select * from students limit 2,2;
        -- 每页显示2个，第3页面
        select * from students limit 4,2;

        -- 按照排序，限制显示 limit 要放在最后面
        select * from students order by age desc limit 4,2;
        
    -- 8.链接查询
        -- 内链接 交集
            -- select ... from [表名A] inner join [表名B];
            select * from students inner join classes;

            -- 条件关联
            -- select ... from [表A] inner join [表B] on 条件;
            select * from students inner join classes 
            on students.cls_id=classes.id;

            -- 部分显示
            select students.*,classes.name 
            from students inner join classes 
            on students.cls_id=classes.id;
            
            -- 起别名
            select * from students as s inner join classes as c 
            on s.cls_id=c.id;

            select s.name,c.name from students as s inner join classes as c 
            on s.cls_id=c.id;

            -- 在以上查询中，把班级姓名放在第一列
            select c.name,s.name 
            from students as s inner join classes as c 
            on s.cls_id=c.id;

            -- 按照班级顺序排
            select c.name,s.* 
            from students as s inner join classes as c 
            on s.cls_id=c.id order by c.name,s.id ;
        
        -- 外链接  左链接，右链接
            -- left join 以左边为基准，找到显示，找不到显示为null
            select s.*,c.* 
            from students as s left join classes as c
            on s.cls_id=c.id;

            +----+-----------+------+--------+--------+--------+-----------+------+--------------+
            | id | name      | age  | height | gender | cls_id | is_delete | id   | name         |
            +----+-----------+------+--------+--------+--------+-----------+------+--------------+
            |  1 | 小明      |   18 | 180.00 | 女     |      1 |           |    1 | python_01期  |
            |  3 | 彭于晏    |   29 | 185.00 | 男     |      1 |           |    1 | python_01期  |
            |  5 | 黄蓉      |   38 | 160.00 | 女     |      1 |           |    1 | python_01期  |
            |  7 | 王祖贤    |   18 | 172.00 | 女     |      1 |          |    1 | python_01期  |
            |  8 | 周杰伦    |   36 |   NULL | 男     |      1 |           |    1 | python_01期  |
            |  2 | 小明月    |   18 | 180.00 | 女     |      2 |          |    2 | python_02期  |
            |  4 | 刘德华    |   59 | 175.00 | 男     |      2 |          |    2 | python_02期  |
            |  6 | 凤姐      |   28 | 180.00 | 保密   |      2 |          |    2 | python_02期  |
            |  9 | 程坤      |   27 | 181.00 | 男     |      2 |           |    2 | python_02期  |
            | 10 | 刘亦菲    |   25 | 166.00 | 女     |      2 |           |    2 | python_02期  |
            | 11 | 金星      |   33 | 162.00 | 中性   |      3 |          |    3 | python_04期  |
            | 12 | 静香      |   12 | 180.00 | 女     |      4 |           | NULL | NULL         |
            | 13 | 郭靖      |   12 | 170.00 | 男     |      4 |           | NULL | NULL         |
            | 14 | 周杰      |   34 | 176.00 | 女     |      5 |           | NULL | NULL         |
            +----+-----------+------+--------+--------+--------+-----------+------+--------------+

            -- 查询没有对应班级信息的学生
            -- select ... from xxx as x left join ... as x on ... having ...;
            -- having 一般用于对结果再次查询
            select s.*,c.* 
            from students as s left join classes as c
            on s.cls_id=c.id having c.id is null;
    -- 9.自关联     
    -- 用同一张表链接查询
    select * from area1 as province inner join area1 as city on province.aid=city.pid having province.atitle='广东省'; 
    
    -- 10.子关联
    -- 标量子查询

    -- 查询身高最高的男生信息;
    select * from students where height=(select max(height) from students);

    --11.从别的表插入数据
        -- insert into 表名 (字段名) select ....
        insert into goods_cates (name) select cate_name from goods group by cate_name;

        update goods as g inner join goods_cates as c on g.cate_name=c.name set g.cate_name=c.id; 
    
    -- 外键
    -- alter table 表A add foreign key (表中的字段) references 表B(表B的字段);
    -- 在表A某个字段中设置外键，外键参考值表B的字段
    alter table goods add foreign key (cate_id) references goods_cates(id);
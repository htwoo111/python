create table goods(
    id int unsigned primary key auto_increment not null,
    name varchar(150) not null,
    cate_name varchar(40) not null,
    brand_name varchar(40) not null,
    price decimal(10,3) not null default 0,
    is_show bit not null default 1,
    is_saleoff bit not null default 0
);


insert into goods values(0,'r510vc 15. 6英寸笔记本', '笔记本','华硕','3399',default,default);
insert into goods values(0,'y400n 14. 0英寸笔记本电脑', '笔记本','联想','4999',default,default);
insert into goods values(0,'g150th15.6英寸游戏本x55eEc', '游戏本','雷神','8499',default,default);
insert into goods values(0,'15. 6英寸笔记本x246超极本', '超极本','联想','4899',default,default);
insert into goods values(0,'u330p 13.3英 寸超极本svp', '超极本','联想','4299',default,default);
insert into goods values(0,'3226scb触控超极本', '超级本','索尼','7999',default,default);
insert into goods values(0,' ipadmini7.9英寸平板电脑ipad', '平板电脑','苹果','6899',default,default);
insert into goods values(0,'air 9.7英寸平板电脑', '平板电脑','苹果','4399',default,default);
insert into goods values(0,'ipad mint配备retina 显示屏ideacentre', '平板电脑','苹果','4499',default,default);
insert into goods values(0,'C340 20英寸一体电脑', '笔记本','华硕','3399',default,default);
insert into goods values(0,'vostro 3800-r1206台式电脑', '台式机','戴尔','4499',default,default);
insert into goods values(0,'imac me086ch/a 21. 5英寸一体电脑', '台式机','宏基','3499',default,default);
insert into goods values(0,'at7-74141p台式电脑linux )z220sff ', '台式机','惠普','5299',default,default);
insert into goods values(0,'f4f06pa工作站poweredge i服务器mac', '服务器/工作站','华为','28889',default,default);
insert into goods values(0,' x3250 m4机架式服务器', '服务器/工作站','华硕','7699',default,default);
insert into goods values(0,'f4f06pa工作站poweredge i服务器mac', '服务器/工作站','索尼','3399',default,default);
insert into goods values(0,'商务双肩包', '笔记本配件','索尼','99',default,default);


select * from goods inner join  (
     select
     cate_name,
     max(price) as max_price
    --  min(price) as min_price,
    --  avg(price) as avg_price,
     from goods group by cate_name
     ) as goods_new_info
     on goods.cate_name=goods_new_info.cate_name and goods.price=goods_new_info.max_price;

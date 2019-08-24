create table orders(
    id int unsigned primary key not null auto_increment,
    order_date_time datetime not null default now(),
    customer_id int unsigned not null,
    foreign key (customer_id) references customers(id)
)

create table customers(
    id int unsigned primary key  not null auto_increment,
    name varchar(10) not null,
    address varchar(20) not null,
    tel bigint unsigned not null,
    account int unsigned not null,
    password int unsigned not null
)

create table order_detail(
    id int unsigned primary key not null auto_increment,
    order_id int unsigned not null,
    goods_id int unsigned not null,
    quantity int unsigned not null default 0,
    foreign key (order_id) references orders(id),
    foreign key (goods_id) references goods(id)
)
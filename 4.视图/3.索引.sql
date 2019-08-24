-- 开启运行时间监督功能
set profiling=1

-- 查看执行时间
show profiles

-- 创建索引
-- create index 新索引表名 on 要索引的表(字段名())
create index title_index on test(title(10));

-- 查看所有
--show index from 表名
show index from test;

-- 删除索引
-- drop index 索引名 on 表名
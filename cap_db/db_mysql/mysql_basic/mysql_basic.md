### 8.x 版本说明
 - 8.x 性能更高, 支持NoSql, 窗口函数, 隐藏索引, 降序索引, 可用可靠
### 下载安装
 - 官方地址: MySQL Installer for ...
 - 镜像地址: https://www.filehorse.com/
 - docker:
    ```zsh
        docker run \
        -p 3306:3306 \
        --name mysql8 \
        -v /Users/yunsong/mysql8/conf:/etc/mysql/conf.d \
        -v /Users/yunsong/mysql8/logs:/logs \
        -v /Users/yunsong/mysql8/data:/var/lib/mysql \
        -e MYSQL_ROOT_PASSWORD=123456 \
        -d mysql:8
    ```
 - docker-compose
### 库语句
```mysql
    # 数据库列表
    show databases ;
    # 创建数据库
    create database if not exists test_db 
        default character set utf8mb4 
        default collate utf8mb4_general_ci;
    # 查看数据库创建信息
    show create database test_db;
    # 修改库字符集
    alter database test_db character set utf8mb4;
    # 删除数据库
    drop database if exists test_db;
    # 选择/使用库
    use test_db;
```
### 表语句
```mysql
   # 创建数据表
   create table students (
       id bigint auto_increment primary key comment 'id',
       name varchar(20) not null default '' comment '姓名',
       gender varchar(7) not null default 'unknown' comment '性别',
       age int not null default 0 comment '年龄',
       mobile varchar(11) default '' not null comment '电话'
   );
    # 查看表
    show tables ;
    desc students;
    # 删除表
    drop table if exists students;
    # 修改表
    alter table students rename to stu; #修改表名
    alter table students character set utf8; #修改字符集
    # 添加列
    alter table students add remark varchar(200) not null default ''comment '备注';
    # 修改列
    alter table students change new_info info varchar(800) not null default '' comment '自我介绍';
    # 修改类型
    alter table students modify new_info text;
    # 删除列
    alter table students drop new_info;
```
### 数据类型
|    mysql类型    |   go类型    |      大小       |            范围             |   说明   |
|:-------------:|:---------:|:-------------:|:-------------------------:|:------:|
|    tinyint    |   int8    |    1 byte     |    -128~127<br />0~255    | 有/无符合  |
|   smallint    |   int16   | 2 byte 16 bit | -32768~32767<br/>0~65535  |   小    |
|   mediumint   |     -     |    3 byte     | -2^31~2^31-1<br/>0~2^32-1 |   中    |
|      int      | int/int32 |    4 byte     |             -             |   整数   |
|    bigint     |   int64   |    8 byte     |             -             |   大型   |
|     float     |  float32  |    4 byte     |             -             |  单精度   |
|    double     |  float64  |    8 byte     |             -             |  双精度   |
| decimal(10,2) |  float64  |   And more    |       总共有10位,其中2位小数       |   价格   |
|    char(n)    |  string   |     === n     |         最多255个字节          | 定长字符串  |
|  varchar(n)   |  string   |     <= n      |         0~65535字节         | 变长字符串  |
|  tinyblob(n)  |  string   |     <= n      |           0~255           | 二进制字符串 |
|    blob(n)    |  string   |     <= n      |          0~65535          | 二进制字符串 |
| mediumblob(n) |  string   |     <= n      |         0~1677215         | 二进制字符串 |
|  longblob(n)  |  string   |     <= n      |       0~4294967295        | 二进制字符串 |
|   tinytext    |  string   |       -       |           0~255           |  字符串   |
|     text      |  string   |       -       |          0~65535          |  字符串   |
|  mediumtext   |  string   |       -       |         0~1677215         |  字符串   |
|   longtext    |  string   |       -       |       0~4294967295        |  字符串   |
|     data      | time.Time |       -       |             -             |  年月日   |
|     time      |     -     |       -       |             -             |  时分秒   |
|     year      |     -     |       -       |             -             |   年    |
|   datetime    | time.Time |       -       |             -             | 年月日时分秒 |
|   timestamp   |  float64  |       -       |             -             |  时间戳   |

### 字段约束
   - 非空/默认  not null / default ' '(0)(false)
   - 唯一  unique
   - 主键 primary key
   - 主键自增  auto_increment
   - 外键 foreign KEY(<列名>) references <主表名> (<列名>);
### 联合主键 key1 并且 key2 成立
```mysql
   create table grades(
       num char(8),
       course int,
       score int,
       primary key (num,course) # 定义为联合主键
   );
```
### 增删改查
```mysql
    # create
    insert into students (name, gender, age, mobile, new_info) values ('tom','boy',16,'123456789','info desc');
    # delete
    delete from students where id = 1;
    # update
    update students set name='andy' where id = 2;
    # select
    select * from students;
    select * from students where name = 'tom';
    select id,name from students where age > 16;
    select * from students where gender = 'boy' and age > 16;
    select * from students where gender = 'girl' or age < 26;
    select * from students where age between 16 and 56;
    select * from students where age not between 16 and 56;
    select * from students where name like '%pa%';
    select * from students where name like '_a%';
    select * from students where name like '___e%';
```
### 处理结果(详细函数请参考其他资料)
_https://www.runoob.com/mysql/mysql-functions.html_
```mysql
    # 计算: 出生年 = 当前年 - 年龄
    select id,name,2023-age from students where age <= 46;
    select id,name as '姓名',2023-age as '出生年' from students where age <= 46;
    select * from students order by age desc ;
    select * from students order by gender ;
    select * from students where age > 16 order by gender;
    select count(id) as count from students where gender = 'boy';
    select max(age) as max_age from students;
    select min(age) as min_age from students;
    select sum(age) as sum_age from students where gender = 'boy';
    select avg(age) as avg_age from students where gender = 'boy';
    alter table students add birthday datetime default null comment '生日';
    update students set birthday = now() where name = 'andy';
    update students set birthday = sysdate() where name = 'tom';
    select concat(name,'-',gender) from students; # 拼接
    select upper(name) from students;
    select lower(name) from students;
    select name,concat(substring(mobile,1,3),'****',substring(mobile,8,4)) from students;
    # 分组查询
    # 5.7之后默认启动 ONLY_FULL_GROUP_BY
    select @@global.sql_mode;
    #'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION'
    set @@global.sql_mode ='STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';
    select gender from students group by gender;
    select gender, count(id) as count from students group by gender; # 按分组 统计
    select gender, count(id) as count from students group by gender having count(id) > 1;
    # 分页查询
    select * from students limit 3,3 ;
```
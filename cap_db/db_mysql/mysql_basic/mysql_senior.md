#### 存储过程
_即封装数据库实现功能代码块 类似函数 procedure_
```mysql
    # 创建 实现加法运算
    create procedure proc_test(IN a int, In b int, OUT c int)
    begin 
        #定义局部变量
        declare m int default 0;
        SET m = a + b;
        SET c = m;
    end;
    # 调用
    set @result = 0;
    call proc_test(1,2,@result);
    select @result from dual;
    # 流程控制 if-then-else 
    create procedure proc_test2(IN way int,IN id int) 
    begin 
        if way = 0 then
            select * from students where students.id = id;
        else
            select * from classes where classes.id = id;
        end if;
    end;
    call proc_test2(0,1);
    # 循环控制 while / repeat / loop
    # while
    create procedure proc_test3(IN num int) 
    begin 
        declare i int;
        set i = 0;
        while i < num do
            select * from students where id = num;
            insert into classes (name,remark) values (concat(num,'班'),'add');
            set i = i + 1;
            end while;
    end;
    # repeat
    create procedure proc_test4(IN num int) 
    begin 
        declare i int;
        set i = 0;
        repeat 
            select * from students where id = i;
            set i = i + 1;
        until  i > num end repeat;
    end;
    # loop
    create procedure proc_test5(IN num int)
    begin 
        declare i int;
        set i = 0;
        myloop: loop
            if i = num then
                leave myloop;
            end if;
            select * from students where id = i;
            set i = i + 1;
        end loop;
    end;
```
#### 删改查
>存储过程属于某个库,只能再其库中使用
```mysql
    # 查看某个库有哪些存储过程
    show procedure status where db = 'test_db';
    # 修改存储过程特征
    alter procedure proc_test1 contains sql #特征...
    contains sql           # 子程序包含SQL语句但不包含读写数据语句
    no sql                 # 子程序不包含sql语句
    reads sql data         # 子程序包含读数据语句
    modifies sql data      # 子程序包含写数据语句
    sql security definer   # 限定仅创建者执行
    sql security invoker   # 调用者可执行
    comment '注释信息'   ;   
    # 删除存储过程
    drop procedure proc_test2_1;
```
#### 游标
```mysql
    # 查询一条记录 不用游标
    set @result = '';
    create procedure first_student(IN id int,OUT result varchar(100))
    begin 
        declare stu_id bigint;
        declare stu_name varchar(20);
        declare stu_age int ;
        select id,name,age into stu_id,stu_name,stu_age  from students where students.id = id; 
        set result = concat('~',stu_id,stu_name,stu_age);
    end;
    call first_student(1,@result);
    select @result from dual;

    # 使用游标
    create procedure first_student_cursor(IN max_id int,OUT result varchar(100))
    begin 
        declare stu_id bigint;
        declare stu_name varchar(20);
        declare stu_age int ;
        declare str varchar(50);
        # declare num int; # 多少条数据
        declare i int;
        # 创建游标
        declare cursor_first_stu cursor for 
            select id,name,age from students ; 
        # select count(1) into num from students;
        # 打开游标
        open cursor_first_stu;
        set i = 0;
        while i < max_id do
            fetch cursor_first_stu into stu_id,stu_name,stu_age;
            set i = i + 1;
            select concat_ws('~',stu_id,stu_name,stu_age) into str;
            set result = concat_ws(',',result,str);
            end while;
        # 关闭游标
        close cursor_first_stu;
    end;
    call first_student_cursor(6,@result);
    select @result from dual;
```
#### 触发器 (钩子)
>无需手动调用 用于insert/update/delete 
> before 数据操作之前触发, after 数据操作之后触发
> NEW 和 OLD 在触发器中新数据 和 旧数据
```mysql
    # 新建日志表
    create table logs(
      id bigint primary key auto_increment,
      access_time timestamp default 0 not null,
      info varchar(300)
    );
```
```mysql
    # 创建触发器
    # for each row 声明为行触发器
    create trigger tri_stu_count 
        after insert on students for each row
        insert into logs(access_time, info) values (now(),concat('insert',NEW.id,'student info'));
    # 查看触发器
    show triggers ;
    # 删除触发器
    drop trigger tri_stu_count;
```
#### 视图 虚拟表(一或多表查询结果)
```mysql
    # 创建视图
    create view view_stu_male AS
        select * from students where gender = '男';
    # 查询视图
    select * from view_stu_male;
    # 查看视图结构
    desc view_stu_male;
    # 修改视图
    create OR REPLACE view view_stu_male AS
         select * from students where gender = '女';
    # 修改方式二
    alter view view_stu_male as 
        select * from students where gender = '男';
    #删除视图
    drop view view_stu_male;
```
#### 索引
```mysql
    # 查看索引
    show create table students;
    show keys from students;
    # 删除索引
    drop index index_name on students;
```
#### 事务
```mysql
    # 8.0.3之前查看隔离级别 
    select @@tx_isolation;
    # 8.0.3之后 默认 REPEATABLE-READ
    select @@transaction_isolation;
    # read uncommitted 脏读,不可重复读,幻读    隔离性最低 并发性最高
    # read committed 不可脏读,不可重复读,幻读   
    # repeatable read 不可脏读,可重复读,幻读 
    # serializable 不可脏读,可重复读,不可幻读   隔离性最高  并发性最低
    # 修改隔离级别
    set session transaction isolation level repeatable read ;
    # 开启事务
    start transaction ;
    insert into students(name,age) values ('andy',16);
    # 回滚
    # rollback ;
    update classes set name = 'aa' where id = 5;
    # 提交
    commit ;
```
### Innodb行锁 受数据隔离级别影响
读锁: 多个事务可以共享锁,只能读不能改
写锁: 除非获取锁,否则不能读和改,Innodb 对于update,delete,insert会自动加写锁,select不会

### 主从复制 读写分离
```mysql
#主从复制
#两个SQL配置文件配置好,具体看本地配置
#主机创建用户
GRANT REPLICATION SLAVE ON *.* TO 'mysql1'@'%' IDENTIFIED BY '123456';

SHOW MASTER STATUS;
stop master;
reset master;

#从机连接主机
#默认端口: 
CHANGE MASTER TO MASTER_HOST='192.168.1.1',MASTER_USER='mysql1',MASTER_PASSWORD='123456',MASTER_LOG_FILE='marster-bin.000001',MASTER_LOG_POS=154;
#指定端口: 
CHANGE MASTER TO MASTER_HOST='192.168.1.1',MASTER_PORT=3306,MASTER_USER='mysql1',MASTER_PASSWORD='123456',MASTER_LOG_FILE='marster-bin.000001',MASTER_LOG_POS=154;
#启动从机
START SLAVE;
#查看从机状态
SHOW SLAVE status;
```

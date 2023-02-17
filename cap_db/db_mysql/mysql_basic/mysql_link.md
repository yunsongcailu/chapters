### 数据表关联关系
- 一对一
- 一对多
- 多对一
- 多对多
### 外键约束
```mysql
    # 学生表 与 班级表 关联
    create table classes(
        id int primary key auto_increment,
        name varchar(40) default '' not null ,
        remark varchar(100) default '' not null
    );
    create table hobby(
      id int primary key auto_increment,
      name varchar(50) default '' not null
    );
     create table students (
       id bigint auto_increment primary key comment 'id',
       name varchar(20) not null default '' comment '姓名',
       gender varchar(7) not null default 'unknown' comment '性别',
       age int not null default 0 comment '年龄',
       mobile varchar(11) default '' not null comment '电话',
       new_info varchar(800) default '' not null comment '介绍',
       birthday datetime default null comment '生日',
       class_id int ,
       hobby_id int ,
       constraint FK_STUDENTS_CLASSES foreign key (class_id) references classes(id),
       constraint FK_STUDENTS_HOBBY foreign key (hobby_id) references hobby(id)
   );
    create table scores(
      id int primary key auto_increment,
      sid bigint UNIQUE comment '学生ID',
      score float not null default 0 comment '得分',
      constraint FK_SCORES_STUDENTS foreign key (sid) references students(id)
    );
    # 为已创建表 添加外键
    alter table students add constraint FK_STUDENTS_CLASSES foreign key (class_id) references classes(id);
```
### 连接查询
```mysql
    #### 内连接 inner join
    # 低效率 where 只返回匹配条件的结果
    select  * from students inner join classes where students.class_id = classes.id;
    # 高效率 ON 只返回匹配条件的结果
    select  * from students inner join classes on students.class_id = classes.id;
    #### 左连接 left join 有成立的加入返回 没有成立的 不加入
    select  * from students left join classes on students.class_id = classes.id;
    #### 右连接
    select * from students right join classes c on c.id = students.class_id;
    #### 全连接
    select * from students FULL join classes c on FULL.class_id = c.id;
    #### 子查询 虚拟表必须要有别名
    select * from students where class_id = (select id from classes where classes.name = '一一班') limit 0,3;
    select * from students
    left join classes c on students.class_id = c.id
    left join hobby h on students.hobby_id = h.id
         where class_id = (select id from classes where classes.name = '一一班')
    limit 2,3;
    select * from students where class_id in (select id from classes where remark = '一年级');
    select * from students
    left join classes c on students.class_id = c.id
    left join hobby h on students.hobby_id = h.id
         where class_id in (select id from classes where classes.remark = '一年级')
    limit 2,3;
```


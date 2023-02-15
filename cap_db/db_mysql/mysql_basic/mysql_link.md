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


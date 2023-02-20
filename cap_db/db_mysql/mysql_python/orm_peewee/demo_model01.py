import datetime
import logging
from peewee import *

logger = logging.getLogger("peewee")
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler())

# 1. 定义并生成表
db = MySQLDatabase('test_db', host='192.168.1.136', port=13308, user='root', passwd='123456')


class BaseModel(Model):
    id = BigAutoField(primary_key=True)
    created_at = DateTimeField(default=datetime.datetime.now)
    updated_at = DateTimeField(null=True, default=None)
    deleted_at = DateTimeField(null=True, default=None)

    class Meta:
        database = db


class Person(BaseModel):
    name = CharField(verbose_name='姓名', max_length=10, null=False, index=True)
    passwd = CharField(verbose_name='密码', max_length=20, null=False, default='123456')
    email = CharField(verbose_name='邮箱', max_length=50, null=True, unique=True)
    gender = SmallIntegerField(verbose_name='性别', null=False, default=1)
    birthday = DateField(verbose_name='生日', null=True, default=None)
    is_admin = BooleanField(verbose_name='是否管理员', default=True)
    firstname = CharField()
    lastname = CharField()

    class Meta:
        table_name = 'persons'
        # 联合主键
        primary_key = CompositeKey('firstname', 'lastname')


# 联合主键 belongs to
class Pet(BaseModel):
    owner_firstname = CharField()
    owner_lastname = CharField()
    petname = CharField()

    class Meta:
        table_name = 'pets'
        # 联合外键
        constraints = [SQL('FOREIGN KEY(owner_firstname,owner_lastname) REFERENCES persons(firstname,lastname)')]


# 复合主键 many to many
class Blog(BaseModel):
    title = CharField()


class Tag(BaseModel):
    title = CharField()


class BlogToTag(BaseModel):
    blog = ForeignKeyField(Blog)
    tag = ForeignKeyField(Tag)

    class Meta:
        primary_key = CompositeKey('blog', 'tag')


class User(Model):
    id = BigAutoField(primary_key=True)
    username = CharField(max_length=120, unique=True, null=False)  # 唯一索引
    age = SmallIntegerField(null=False, default=0)
    created_at = DateTimeField(default=datetime.datetime.now)
    updated_at = DateTimeField(null=True, default=None)
    deleted_at = DateTimeField(null=True, default=None)

    # 额外信息
    class Meta:
        database = db


class Tweet(Model):
    id = BigAutoField(primary_key=True)
    user = ForeignKeyField(User, backref='tweets')
    message = TextField()
    created_at = DateTimeField(default=datetime.datetime.now)
    updated_at = DateTimeField(null=True, default=None)
    deleted_at = DateTimeField(null=True, default=None)
    is_published = BooleanField(default=True)

    class Meta:
        database = db


if __name__ == '__main__':
    db.connect()
    # db.create_tables([Person, Pet, Blog, Tag, BlogToTag])
    # person联合主键 没有id
    # pid = Person.insert({
    #     "firstname": "bee",
    #     "lastname": "ttt"
    # }).execute()
    # print(pid)
    # 复合查询
    # person = Person.select().where((Person.firstname == "bee") & (Person.lastname == "ttt"))
    # print(person.sql())
    # LIKE 查询 WHERE (`t1`.`firstname` LIKE %s)', ['%ee%'])
    # query = Person.select().where(Person.firstname.contains("ee"))
    # print(query.sql())
    # p = Person.select().dicts()
    # for row in p:
    #     print(row)
    # limit
    # p = Person.select().limit(1)
    # for row in p:
    #     print(row)
    # order
    # Person.select().order_by(Person.birthday.desc())
    # 去重
    # query = Person.select().distinct()
    # print(query)
    # 计数
    # query = Person.select().count()
    # 聚合
    # select max(birthday) from person;
    # query = Person.select(fn.MAX(Person.birthday))
    # 子查询 select name,is_relative from person where birthday = (select MAX(birthday) from person)
    # 需要别名
    # PersonAlias = Person.alias()
    # subSql = PersonAlias.select(fn.MAX(PersonAlias.birthday))
    # query = (Person.select(Person.is_relative, Person.name).where(Person.birthday == subSql))
    # print(query)
    # 分页
    # for tweet in Tweet.select().order_by(Tweet.id).paginate(2, 10):
    #     print(tweet.message)
    # 原生SQL
    # query = Person.raw('select * from persons where name = %s', "bee")
    # for q in query:
    #    print(q)
    # query = Person.select().where(SQL('username = "%s"' % 'bee'))
    query = Tweet.select(Tweet, User.username).json(User).where(User.username == 'mickey')
    for q in query:
        print(q.user.username, q.message)

import datetime
import logging

from peewee import *

logger = logging.getLogger("peewee")
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler())

# 1. 定义并生成表
db = MySQLDatabase('test_db', host='192.168.1.136', port=13308, user='root', passwd='123456')


# 继承Model
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
    # db.create_tables([User, Tweet])
    # charLine = User(id=1, username="tom")
    # charLine.save()  # 有主键更新,无主键则新建
    charLine = User(username="bee")
    row = charLine.save()
    # if row == 0:
    #     print("none")
    # else:
    #     print("ok")
    # charLine.save(force_insert=True)
    # lili = User.create(username="lili")
    # print(lili)
    # get 查询不到 抛异常
    # try:
    #     u = User.get(User.id == 2)
    # except User.DoesNotExist as e:
    #     print("not found")
    # else:
    #     print(u.username)
    # try:
    #     u = User.get_by_id(1)
    # except User.DoesNotExist as e:
    #     print("not found")
    # else:
    #     print(u.username)
    # User.select()组装sql for循环的时候才发起数据库请求
    # for user in User.select():
    #     print(user.username)
    # names = ["tom", "lili", "huey", "mickey"]
    # users = User.select().where(User.username.in_(names))
    # for user in users:
    #     print(user.username)
    # charLine = User(username="hubee")
    # row = charLine.save()
    # if row == 0:
    #     print("none")
    # else:
    #     print("ok")
    # line = User(id=1, age=1)
    # print(line.save())
    # line = User.update(age=2).where(User.username == "bee").execute()
    # print(line)
    # 物理删除
    # u = User.get(User.username == "bee")
    # u.delete_instance()
    # query = User.delete().where(User.username == "bee").execute()
    # print(query)

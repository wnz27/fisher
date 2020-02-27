# -*- coding:utf-8 -*-
# Create by 27
# @Time : 2020/2/26 18:46
__author__ = '27'
from sqlalchemy import Column, Integer, String
from flask_sqlalchemy import SQLAlchemy


# sqlalchemy，第三方
# Flask_SQLAlchemy 对上面的库做了优化的封装
# WTFORMS也是不止可以使用在flask，第三方
# Flask_WTFORMS也是对上面的库进行了封装


db = SQLAlchemy()

class Book(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    author = Column(String(30), default='未名')
    binding = Column(String(20))
    publisher = Column(String(50))
    price = Column(String(20))
    pages = Column(Integer)
    pubdate = Column(String(20))
    isbn = Column(String(15), nullable=False, unique=True)
    summary = Column(String(1000))
    image = Column(String(50))

    # MVC M Model 只有数据 = 数据表
    # ORM 对象关系映射，则包含的更广阔的，不止数据的创建，还有数据的查询，删除，等等操作，orm是让程序员通过操作model间接地操作数据库
    # Code First 关注的是数据表怎么创建的，解决的是创建数据的问题

    def sample(self):
        pass

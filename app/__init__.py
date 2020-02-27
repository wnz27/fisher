# -*- coding:utf-8 -*-
# Create by 27
# @Time : 2020/2/23 11:44

# 负责app的初始化工作
from flask import Flask
from app.models.book import db

__author__ = '27'


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.secure')
    app.config.from_object('app.setting')
    register_blueprint(app)

    db.init_app(app)
    db.create_all(app=app)  # 没有这句话不会有数据表，括号为空会抛出"No application found"错误
    '''
    查看源码可以有这样的写法：
    1、
    with app.app_context():
        db.create_all()
    2、
    sqlalchemy的app属性存在也可。这个方法不适合现在这个场景。
    '''
    return app


def register_blueprint(app):
    from app.web import web
    app.register_blueprint(web)



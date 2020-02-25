# -*- coding:utf-8 -*-
# Create by 27
# @Time : 2020/2/23 11:44

# 负责app的初始化工作
from flask import Flask

__author__ = '27'


def create_app():
    app = Flask(__name__)
    app.config.from_object('config')
    register_blueprint(app)
    return app


def register_blueprint(app):
    from app.web import web
    app.register_blueprint(web)



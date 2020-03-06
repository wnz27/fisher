"""
 Created by 七月 on 2018/1/26.
 微信公众号：林间有风
"""
from . import web

__author__ = '27'


@web.route('/set/cookie')
def set_cookie():
    pass


@web.route('/set/session')
def set_session():
    pass


@web.route('/get/session')
def get_session():
    pass

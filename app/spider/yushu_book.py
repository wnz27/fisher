# -*- coding:utf-8 -*-
# Create by 27
# @Time : 2020/2/22 22:04
__author__ = '27'
from app.libs.httper import HTTP
from flask import current_app  # current_app类似request对象，是个代理，与上下文有关


class YuShuBook:
    isbn_url = 'http://t.yushu.im/v2/book/isbn/{}'
    keyword_url = 'http://t.yushu.im/v2/book/search?q={}&count={}&start={}'

    @classmethod
    def search_by_isbn(cls, isbn):
        url = cls.isbn_url.format(isbn)   # self也可以访问到变量，因为链式查找
        result = HTTP.get(url)  # json在python会被转换成dict
        return result

    @classmethod
    def search_by_keyword(cls, keyword, page=1):
        url = cls.keyword_url.format(keyword, current_app.config['PER_PAGE'], cls.calculate_start(page))
        result = HTTP.get(url)
        return result

    @classmethod
    def calculate_start(cls, page):
        return (page - 1) * current_app.config['PER_PAGE']



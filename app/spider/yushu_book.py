# -*- coding:utf-8 -*-
# Create by 27
# @Time : 2020/2/22 22:04
__author__ = '27'
from app.libs.httper import HTTP
from flask import current_app  # current_app类似request对象，是个代理，与上下文有关


class YuShuBook:
    # 描述特征（类变量，实例变量）
    # 行为（方法）
    isbn_url = 'http://t.yushu.im/v2/book/isbn/{}'
    keyword_url = 'http://t.yushu.im/v2/book/search?q={}&count={}&start={}'

    def __init__(self):
        self.total = 0
        self.books = []

    def search_by_isbn(self, isbn):
        url = self.isbn_url.format(isbn)   # self也可以访问到变量，因为链式查找，也可以用类名访问
        result = HTTP.get(url)  # json在python会被转换成dict
        '''伪码,实际工程要这么做，减少爬数据次数
        book = query_from_mysql  #
        if book:
            return book
        else:
            save(result) 
        '''
        self.__fill_single(result)

    def __fill_single(self, data):
        self.total = 1
        self.books.append(data)

    def __fill_collections(self, data):
        self.total = data['total']
        self.books = data['books']

    def search_by_keyword(self, keyword, page=1):
        url = self.keyword_url.format(keyword, current_app.config['PER_PAGE'], self.calculate_start(page))
        result = HTTP.get(url)
        self.__fill_collections(result)

    def calculate_start(self, page):
        return (page - 1) * current_app.config['PER_PAGE']

    @property
    def first(self):
        return self.books[0] if self.total >= 1 else None



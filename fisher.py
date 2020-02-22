# -*- coding:utf-8 -*-
# Create by 27
# @Time : 2020/2/21 22:13
from yushu_book import YuShuBook

__author__ = '27'
from flask import Flask
from helper import is_isbn_or_key

app = Flask(__name__)
app.config.from_object('config')


# 较为简单的接收客户端参数的方式
@app.route('/book/search/<q>/<page>')
def search(q, page):
    '''
    q(请求关键字)/isbn: 普通关键字，isbn
    我们可以在代码判断是q还是isbn，不同在请求里（客户端）区分
    start:count: 可以合起来为：page
    '''
    isbn_or_key = is_isbn_or_key(q)
    if isbn_or_key == 'isbn':
        result = YuShuBook.search_by_isbn(q)    # alt + enter可以自动引入
        # 从视图函数返回的所有东西必须是字符串，所以这个result需要序列化
        return
    else:
        result = YuShuBook.search_by_keyword(q)
        return result




if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=app.config["DEBUG"], port=82)
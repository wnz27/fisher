# -*- coding:utf-8 -*-
# Create by 27
# @Time : 2020/2/21 22:13
__author__ = '27'
from flask import Flask
from helper import is_isbn_or_key

app = Flask()
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

    pass


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=app.config["DEBUG"], port=81)
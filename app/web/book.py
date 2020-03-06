# -*- coding:utf-8 -*-
# Create by 27
# @Time : 2020/2/23 08:39
from flask import jsonify, request, render_template, flash
# request的args是不可变字典，可以通过下面方式转换成可变字典，request是代理模式实现的，
# 在视图函数里使用的时候就是拿的到请求信息，在其他场景可能是空的。
# a = request.args.to_dict()

# from app.web import web 或者
from app.view_models.book import BookViewModel, BookCollection
from app.web import web
from app.libs.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook
from app.forms.book import SearchForm

__author__ = '27'

# 测试非线程隔离对象的问题
# @web.route('/test')
# def test1():
#     from flask import request
#     from app.libs.none_local import n
#     print(n.v)
#     n.v = 2
#     print(n.v)
#     print("*" * 80)
#     print(getattr(request, 'v', None))  # getattr相比与.语法更好的灵活性和容错性
#     setattr(request, 'v', 2)
#     print(request.v)  # 这里肯定有值了
#     print("*" * 80)
#     return ''  # 视图函数必须返回值，否则会抛出异常。

# 较为简单的接收客户端参数的方式
@web.route('/book/search')
def search():
    '''
    q(请求关键字)/isbn: 普通关键字，isbn
    start:count: 可以合起来为：page
    ?q=金庸&page=1
    '''
    # q = request.args['q']
    # 至少一个字符，长度限制
    # page = request.args['page']
    # 正整数，也要有长度限制
    # 第三方验证插件比较推荐，wtforms，引入一个叫"验证层"的概念，都不要把验证写在视图函数里。
    form = SearchForm(request.args)
    books = BookCollection()

    if form.validate():
        q = form.q.data.strip()  # 去掉空格，兼容用户输入别的空格
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)
        yushu_book = YuShuBook()

        # Messaging Flash
        if isbn_or_key == 'isbn':
            yushu_book.search_by_isbn(q)
        else:
            yushu_book.search_by_keyword(q, page)
        books.fill(yushu_book, q)
        # API
        # return jsonify(books)  # 做api的话，更为方便的返回方式
    else:
        flash("搜索的关键字不合要求，请重新输入！")
        # return jsonify(form.errors)
    return render_template('search_result.html', books=books, form=form)
    # 这样就算不输入查询参数，也会返回东西，因为如果不输入查询参数，那么form的isvalid不会通过


@web.route('/book/<isbn>/detail')
def book_detail(isbn):
    pass


@web.route('/test')
def test2():
    r = {
        'name': '',
        'age': 27
    }
    r1 = {

    }
    flash("hello,27!", category="error")
    flash("hello, 37!", category="warning")
    # 模板 html
    return render_template('test3.html', data=r, data1=r1)

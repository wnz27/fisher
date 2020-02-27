# -*- coding:utf-8 -*-
# Create by 27
# @Time : 2020/2/23 08:39
from flask import jsonify
from learn_note.learn_flask_basic_fisher import app
from app.libs.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook

__author__ = '27'

# 蓝图 blueprint 蓝本

'''
只把app导入过来，运行会报404，因为我们没有在入口文件跟视图函数做关联，所以这个文件根本没有运行。

然后我们在入口使用import导入本文件，的确会运行，但是依然会报404，为什么？
牵扯到endpoint，可以看源码，endpoint；url_map与view_func关系，他俩同时注册才算视图函数有效，
原因是循环导入了。走到用调试模式可以看到app被初始化了两次，然后运行的app和你注册路由函数的app不是同一个。
导致虽然url_map和view_func有search还是会404,可以用print打印id函数看出，我们再在if __nam__语句里打印一个id，
然后在视图函数上面打印一个id，就可以看出，我们最后运行的是第一次创建的那个app，但是给第二次实例化的那个app注册了视图函数。
这样肯定会404。
'''

print(id(app))
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
        # 从视图函数返回的所有东西必须是字符串，所以这个result需要序列化，
        # 只要是dict或者是其他对象都要进行序列化，序列化之后就是字符串格式了。
        # return json.dumps(result), 200, {'content-type': 'application/json'}
        # API
        return jsonify(result)
    else:
        result = YuShuBook.search_by_keyword(q)
        return result

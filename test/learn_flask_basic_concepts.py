# -*- coding:utf-8 -*-
# Create by 27
# @Time : 2020/2/27 17:38
__author__ = '27'
from flask import Flask, current_app

app = Flask(__name__)
# 应用上下文 对象 对Flask的封装
# 请求上下文 对象 对Request的封装
# Flask AppContext
# Request RequestContext
# 离线应用、单元测试，需要手动推入appcontext
# 当有请求的时候，app会自动进入栈中，没有的时候，需要我们自己手动把app核心对象推入栈中。
'''
所谓上下文对象，是把核心对象和其他外部信息封装组合在一起的对象。
故而我们想要使用Flask和Request这样的核心对象，请从AppContext和RequestContext中去拿核心对象。
'''
# ctx = app.app_context()
# ctx.push()
# a = current_app
# d = current_app.config["DEBUG"]
# ctx.pop()

# with语句改写
with app.app_context():  # with后面就是：上下文表达式
    a = current_app
    d = current_app.config["DEBUG"]

'''
with语句实现的关键是对象实现了__enter__以及__exit__方法。

可以对实现了上下文协议的对象使用with语句
通常把实现了上下文协议的对象叫上下文管理器
实现了__enter__和__exit__方法就是实现了上下文协议

上下文表达式必须返回一个上下文管理器，即返回一个实现了__enter__和__exit__的对象。
'''

'''
如数据库：
1、连接数据库
2、sql
3、释放资源
假如sql出现异常，阻塞住了，那么后面释放资源的语句不会被执行。

首先可以这样解决：
try：
except
finally
更优雅的方式就是上下文管理器
在__enter__定义连接方法
在__exit__定义释放连接的方法
把操作数据库的语句写进with的缩进代码块里。
'''

'''
再如文件读写
try:
    f = open('path')
    print(f.read())
finally:
    f.close()
用with改写：
with open('path') as f:  # 这个f不是上下文管理器,而是__enter__方法返回的值会赋给这个变量。
    print(f.read())
不用手动close，__exit__里面有close()的逻辑
'''

# class A:
#     def __enter__(self):
#         a = 1
#         return a
#     def __exit__(self):  # 会报错，这样写是错的
#         b = 2
# with A() as obj_A:
#     pass

class MyResource:
    def __enter__(self):
        print("connect to resource!!")
        return self
    def __exit__(self, exec_type, exec_value, tb):  # 如果with语句没有异常，后面三个参数都是None。tb是traceback对象，里面存着异常
        '''
        __exit__的返回值只有两种，True或者False
        如果这里返回True，那我们退出with语句时，with的外部不会抛出异常
        如果返回False，那退出with语句时，with的外部还是会抛出异常
        所以灵活的地方在于，你可以返回True，在内部处理异常，
        你也可以返回False，依然在外面处理异常
        如果你没有return语句，在python里就是None，那也相当于False
        所以没返回语句就是相当于返回了False
        可以断电查看，去掉return，依然会抛出异常
        '''
        if tb:
            print("process exception!")
        else:
            print("no exception!!")
        print("close resource connection!!")
        return True
    def query(self):
        print("query data!!")
with MyResource() as resource:
    1/0
    resource.query()

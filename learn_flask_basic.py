# -*- coding:utf-8 -*-
# Create by 27
# @Time : 2020/2/20 21:48
__author__ = '27'
from flask import Flask, make_response
# from config import DEBUG

app = Flask(__name__)
# from_object需要接收一个模块的路径，指出配置文件与该文件的相对路径即可，引入之后，可以把上面的from import语句注释掉了
app.config.from_object('config')
'''
如果在config文件里把DEBUG写成Debug，我用print(app.config['DEBUG'])会打印出False

我用print(app.config['Debug'])来打印，却出错了：
Traceback (most recent call last):
  File "learn_flask_basic.py", line 29, in <module>
    print(app.config['Debug'])
KeyError: 'Debug'

为什么？

下面是from_object的源码：
        if isinstance(obj, string_types):
            obj = import_string(obj)
        for key in dir(obj):
            if key.isupper():
                self[key] = getattr(obj, key)
然后点进isupper()里面有这样的解释：
S.isupper() -> bool
        Return True if all cased characters in S are uppercase and there is
        at least one cased character in S, False otherwise.
意思是所有的字母都是大写的时候，才返回True
也就是是说，只有在全大写的时候才会为属性的变量名称对应的字典的key设置它所对应的值，
如果你的config文件中配置项不用全部大写作为配置的变量名的话，那么就不会被设置到Config实例对应的字典中，
进而，如果你用你设置的变量名作为key来从config读取值的话，肯定是KeyError。

第一个问题，为什么会打印出False？
基于这个函数的源码，我们知道，你在配置文件里的Debug根本没有放进config的字典里，
所以这个False是从哪读出来的呢？
是flask默认的DEBUG参数就是False，所以我们可以打印出来False
'''

print(app.config['DEBUG'])

'''
在路由后面加斜杠，可以同时匹配用户输入加斜杠和不加斜杠的情况
!!!!!!!如果run()函数中debug参数没有开启，那么一定要重启服务才生效！！！！！
原理：
这是flask做了一次重定向
在客户端（浏览器）向服务器用url1发送第一次请求后，服务器由于种种原因，
可能是没有这个url1或者是不想让你访问这个url1，
会返回给客户端一条状态码为301（永久移动）或者302（临时移动）或者其他30x的消息，3开头的状态码表示重定向，
告诉客户端，应该使用url2的地址来请求，
之后客户端再次用url2来向服务器发送请求。
'''
# 第一种注册路由的方法
# @app.route('/hello')
def hello1():
    return 'Hello 272727!!!'
'''
flask 为什么要做重定向呢？
因为，如果从第一个url就进入请求资源的视图函数，从某种意义上讲违背了唯一url的原则
唯一url好处是，在被搜索引擎索引的时候，俩url是会被索引两次的，两个url如果对应的资源是一样的，那么完全没有必要。
关于被索引的问题牵扯seo。
'''

def hello2():
    # 函数视图
    '''
    还会返回status code
    content-type, 放在http header
    我们的web服务器要告诉客户端如何解析我返回的内容
    如果我们不指定，默认会把content-type设置为text/html
    所以也就是为什么我们要是返回<html></html>页面上什么都不显示
    '''
    # 返回普通字符串
    # headers = {
    #     'content-type': 'text/plain'
    # }
    # response = make_response('<html></html>', 404)    # 状态码只是标识，不会对返回的内容产生实质的影响。

    # 重定向尝试
    # headers = {
    #     'content-type': 'text/plain',
    #     'location': 'http://www.bing.com'
    # }
    # response = make_response('<html></html>', 301)

    # 比如给小程序或者别的应用提供接口，返回json数据
    headers = {
        'content-type': 'application/json'
    }
    # response = make_response({'123': 123}, 200)
    # response.headers = headers
    # return response
    # 最快速的方法，无需构造headers对象：
    return {'abc': 123}, 200, headers
    # return '<html></html>'

# 第二种注册路由的方法,用基于类的视图（即插视图），一定要使用以下方式来注册
app.add_url_rule('/hello', view_func=hello2)

if __name__ == "__main__":
    # 生产环境，一般会用ngnix +uwsgi来部署
    '''
    因为生产环境，一般会用ngnix +uwsgi来部署和启动项目
    所以使用if __name__ == "__main__":的好处是：
    生产环境不是手动执行该fisher文件，也就是说fisher在生产环境下不是入口文件了，
    而只是被uwsgi加载的模块文件，使用的是uwsgi作为web服务器，
    反过来说，如果没有这个语句，那么，在用uwsgi加载fisher这个模块后，app.run也会运行，
    又启动了flask内置的服务器，同时出现俩服务器，这就不可以。
    所以结论是，这个语句保证了生产环境下，不会运行flask自带的web服务器。
    '''

    # 修改代码自动重启服务器,在run()函数中把debug设置为True(使用的是配置文件注册进app的config的字典), 也可以用port=端口号来指定端口
    # app.config就是dict的子类
    app.run(host='0.0.0.0', debug=app.config['DEBUG'])



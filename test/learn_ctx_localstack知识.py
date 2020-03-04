# -*- coding:utf-8 -*-
# Create by 27
# @Time : 2020/2/29 23:46
import threading
import time

__author__ = '27'
'''
回顾：
current_app是一直指向_app_ctx_stack栈顶的，request是指向_request_ctx_stack栈顶的，有请求进来就是进到这个栈里。
当有请求的时候，app会自动进入栈中，这时候current_app就自动指向了app对象，当请求结束时，它们会被弹出。
没有请求的时候，如果要使用，则需要我们自己手动把app核心对象推入栈中，让current_app指向当前的app核心对象。

_app_ctx_stack和_request_ctx_stack都是LocalStack对象
LocalStack也是一个线程隔离的对象，它是如何做线程隔离的？看源码，也维护了一个Local的对象，使用Local的方法来实现线程隔离。
不同线程使用LocalStack推入栈的request是不一样的，所以多线程时，因为线程多所以出栈顺序也就是处理哪些线程的请求也是不定的。

与Local一样LocalStack也是可以单独使用在别的地方的，是一个单独的库。

LocalStack Local 字典是什么样的关系？
Local使用字典的方式实现线程隔离，而LocalStack使用Local来实际做出一个线程隔离的栈结构，

某句话：
软件世界的一切都是由封装构建的， 没有什么是封装解决不了的问题，如果一次封装解决不了问题，就再来一次。

编程也是一种艺术，含蓄！！！！！

'''
from werkzeug.local import LocalStack
# push pop top
s = LocalStack()
# s.push(1)
# print(s.top)  #  看源码，top方法加了@property，所以是以属性的方法调用，而不是方法来调用，所以不用加括号
# print(s.top)
# print(s.pop())
# print(s.top)
# s.push(1)
# s.push(2)
# print(s.top)
# print(s.top)
# print(s.pop())
# print(s.top)

# 数据结构就是限制了某些能力
s.push(1)
print("in {} after push, value is {}".format(threading.current_thread().getName(), str(s.top)))


def worker():
    print("in {} before push, value is {}".format(threading.current_thread().getName(), str(s.top)))
    s.push(2)
    print("in {} after push, value is {}".format(threading.current_thread().getName(), str(s.top)))


new_t = threading.Thread(name="27's new thread", target=worker)
new_t.start()
time.sleep(2)

print("finally in {}, value is {}".format(threading.current_thread().getName(), str(s.top)))

'''
回到问题的原点：
多线程的时候，并发请求多的时候，视图函数如何识别出request究竟是哪个请求呢？flask是如何处理这种情况？
这个请求被哪个线程实例化，那么任何一个线程引用到request这个变量名也就是执行top或者pop的时候，自然取出的就是自己实例化的请求对象，
而不可能是其他线程的。
所以线程隔离的意义在于，当前线程一定能正确引用到它所创建的对象，而不会引用到其他线程创建的对象。

想要临时保存用户相关的数据可以使用g，g也是线程隔离的对象。

app上下文和请求上下文对象都是被隔离对象，但是request是间接被隔离的，app全局只有一个，
也就是说我的app上下文可以在不同线程不一样，但是它们指向的app核心对像只有一个。

所以全局计数器可以用这个app实现，但是不推荐，因为有线程安全的问题。
可以用mysql或者redis来实现，方法有很多，不要局限。

总结：
current_app -> LocalStack.top = AppContext, top.app = Flask核心对象（app）
request -> LocalStack.top = RequestContext, top.request = Request核心对象（request）

'''
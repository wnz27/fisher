# -*- coding:utf-8 -*-
# Create by 27
# @Time : 2020/2/29 23:46
__author__ = '27'
'''
回顾：
current_app是一直指向_app_ctx_stack栈顶的，request是指向_request_ctx_stack栈顶的，有请求进来就是进到这个栈里。
当有请求的时候，app会自动进入栈中，这时候current_app就自动指向了app对象，
没有请求的时候，需要我们自己手动把app核心对象推入栈中，让current_app指向当前的app核心对象。

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
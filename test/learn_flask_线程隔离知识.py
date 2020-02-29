# -*- coding:utf-8 -*-
# Create by 27
# @Time : 2020/2/29 15:17
import time

__author__ = '27'

'''
面向对象：对象是保存状态的地方，比如flask的request，把每个进来的请求都封装为一个request对象，它们之间包含的属性参数都是不同的。
'''

'''
flask web 框架
引出的问题：从客户端发向服务器的请求，和服务器处理请求的线程，它们有什么关系？
具体化，假如客户端发了10个请求，flask是开启10个线程处理请求还是一个线程处理10个请求？
这句话是不精确的，flask是不会开启线程的，线程是由web服务器来开启的（webserver,如nginx，apache，tomcat IIS）
开发环境，启动的是flask内置的一个webserver，但生产环境，我们是用另外的webserver来部署flask代码。
默认情况下，flask自带的web服务器是以单进程单线程的方式在响应我们客户端的请求，所以这样的情况，10个请求进来，就是一个一个执行。
我们调试的时候也可以手动开启线程和进程：
在app.run中threaded=True就是开启多线程,不动进程的情况下，就是单进程的多线程，process=1，就是调整开启进程数量，默认是1。

当单线程的时候，请求是排队的，所以视图函数接收的request是明确的有顺序的。
但是多线程的时候，并发请求多的时候，视图函数如何识别出request究竟是哪个请求呢？flask是如何处理这种情况？
这就是线程隔离，
假如request = {k:v, k2:v2, k3:v3.......}
在多线程环境，线程有唯一标识，所以就可以让线程的唯一标识作为key，然后把请求当做value，所以大概这样：
request = {thread1:request1, ......}
对于线程来说，最符合唯一性的就是线程的id号。
所以这样用线程的id号作为键，利用最基本的数据结构字典就做成了线程隔离，不同的线程，都在字典中有它自己的状态，
所有线程相关的request实例化对象都被字典保存下来。
当然线程隔离只是一个思想，不是说只能用字典实现。
 
字典只是保存数据，我们还要操作数据，所以我们要把关于线程隔离的相关数据封装到一个对象中去，
这样我们在外部使用对象的相关方法就可以很方便的进行线程隔离的操作，
flask内部引用了一库叫werkzeug，这个库有个local模块，有一个Local对象，
flask做线程隔离的实质操作就是这个Local完成的，也就是借助字典的方式，自己封装了字典的方法。
所以我们在其他地方需要线程隔离，可以自己引入wergzeug来用它的local模块来做线程隔离操作。

最直观的思路是在当下线程拿到id，然后通过key取得对应request。
但是通过线程隔离对象L的角度考虑，不同线程对同一个线程隔离对象的操作时互不影响的，比如thread1 操作L.a thread2操作L.a，
就是在线程1给a赋值不会影响线程2给a赋值。那么这样一种对象就是线程隔离的对象。
原理就是字典，但是它以一种面向对象的方式把字典的原理封装为一个对象，让大家操作相关属性的时候就是像线程隔离的互不影响。
可以看看Local的源码就一目了然了，重点看下__setattr__和__getattr__，就完全明白，即使属性名一样，但是取的位置并不一样。
还有可以看一眼get_ident这个方法的说明。
这就是Local对象高明的地方，同样的语句在不同的线程使用的变量完全不一样。
还可以利用断点在__setattr__方法的ident = self.__ident_func__()那一行加个断点，可以清晰看到两次赋值时ident号是不一样的。

'''
from werkzeug.local import Local
from threading import Thread
import threading

local_obj = Local()
local_obj.b = 1


def worker():
    local_obj.b = 2
    print("thread: {}'s b is: {}".format(threading.current_thread().getName(), local_obj.b))


new_t = Thread(target=worker, name="27's_new_thread")
new_t.start()
time.sleep(2)

print("thread: {}'s b is: {}".format(threading.current_thread().getName(), local_obj.b))


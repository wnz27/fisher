# -*- coding:utf-8 -*-
# Create by 27
# @Time : 2020/2/23 11:44
# 负责web蓝图的初始化
from flask import Blueprint

__author__ = '27'

# 蓝图 blueprint 蓝本，单蓝图的初始化放在该蓝图的__init__文件下，方便这个蓝图的模块导入使用，
# 而项目最大的拆分单元是蓝图，少量蓝图在初始化app（项目）时候注册进app。
web = Blueprint('web', __package__)  # 也可以拆出去，解决循环引用的问题，虽然这样也可以实例化成功
print(id(web))
from . import book
from . import user


'''
这里也出现了循环引用，但是没问题，为什么呢？
断点模式看了一下，因为第二次不会重复导入，web的id打印了两次，第二次的被使用，
主要过程还未看明白。
'''

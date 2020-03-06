# -*- coding:utf-8 -*-
# Create by 27
# @Time : 2020/3/6 15:50
__author__ = '27'
class AAA:
    def __init__(self, name="123", age=1235):
        self.name = name
        self.age = age

a = AAA()
print(a.__dict__)
b = AAA("3333", 333)
print(b.__dict__)


def is_odd(n):
    return n % 2 == 1


tmplist = filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(tmplist)
newlist = list(tmplist)
print(newlist)

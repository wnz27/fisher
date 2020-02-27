# -*- coding:utf-8 -*-
# Create by 27
# @Time : 2020/2/21 22:45
__author__ = '27'
'''
使用python发送http请求的两个方法：
1、urllib
2、requests （推荐）

小原则：
对于外部获取的数据，如果出现异常，最好不要抛出来，而是应该默认值处理。
'''
import requests


class HTTP:  # python3中写与不写(object)没有区别
    @staticmethod
    def get(url, return_json=True):
        r = requests.get(url)
        # restful通常要求
        # 返回json
        # if r.status_code == 200:
        #     if return_json:  # 用一个return_json来标识是否返回json格式，使得这个get更具通用性
        #         return r.json()  # 返回json格式的数据
        #     else:
        #         return r.text  # 返回普通字符串
        # else:   # 兼容格式
        #     if return_json:
        #         return {}
        #     else:
        #         return ''
        if r.status_code != 200:
            return {} if return_json else ''
        return r.json() if return_json else r.text

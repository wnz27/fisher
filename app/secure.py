# -*- coding:utf-8 -*-
# Create by 27
# @Time : 2020/2/21 16:36
__author__ = '27'

'''
拆配置文件
secure适合放：

1、机密信息
数据库密码
账号
flask的app的key
等机密信息，单独放在一个文件

2、开发与生产环境不同的配置，也放在secure配置文件中。
如DEBUG

好处：
secure配置文件永远不要上传到git上~~~
1、安全性
2、为开发减少冲突，secure存放的是生产与开发不相同的信息，
如果把所有都放在一个配置文件，那么大家总是pull来pull去的容易出问题。
'''

# debug
DEBUG = True

# 数据库配置
SQLALCHEMY_DATABASE_URI = 'mysql+cymysql://root:123456@localhost:3306/fisher'


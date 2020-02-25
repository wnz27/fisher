# -*- coding:utf-8 -*-
# Create by 27
# @Time : 2020/2/21 22:13
__author__ = '27'
from flask import Flask

app = Flask(__name__)
print(id(app))
app.config.from_object('config')

from app.web import book
'''
这样导入，它会产生循环导入的问题：运行入口fisher.py 导入book，进入book.py，导入fisher的app，
进入fisher，然后不会再执行这句话了，因为一个文件的导入只会执行一次，并且这时候不会启动app.run，
因为这是从book进来的fisher，if __name__ == "__main__":语句不会判断生效。然后返回book里面，
然后会接着book里面的代码走。
'''

if __name__ == "__main__":
    print(id(app))
    app.run(host='0.0.0.0', debug=app.config["DEBUG"], port=82)
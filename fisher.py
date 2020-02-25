# -*- coding:utf-8 -*-
# Create by 27
# @Time : 2020/2/21 22:13
from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=app.config["DEBUG"], port=82)

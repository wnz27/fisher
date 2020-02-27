# -*- coding:utf-8 -*-
# Create by 27
# @Time : 2020/2/24 18:58
from wtforms import Form, StringField, IntegerField

from wtforms.validators import Length, NumberRange, DataRequired

__author__ = '27'


class SearchForm(Form):
    q = StringField(validators=[DataRequired(), Length(min=1, max=30)])  # DataRequired()防止用户只在q传一个空格进去
    page = IntegerField(validators=[NumberRange(min=1, max=99)], default=1)


# -*- coding:utf-8 -*-
# Create by 27
# @Time : 2020/2/24 18:58
from wtforms import Form, StringField, IntegerField

from wtforms.validators import Length, NumberRange

__author__ = '27'


class SearchForm(Form):
    q = StringField(validators=[Length(min=1, max=30)])
    page = IntegerField(validators=[NumberRange(min=1, max=99)], default=1)


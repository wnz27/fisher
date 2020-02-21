# -*- coding:utf-8 -*-
# Create by 27
# @Time : 2020/2/21 22:35
__author__ = '27'
def is_isbn_or_key(word):
    '''
    判断word是isbn还是普通关键字
    :param word: 客户端传参
    :return: string,
    isbn13 13个0-9的数字组成
    isbn10 10个0-9的数字，还有一些" - "组成
    现在的新书一般都是isbn13
    '''
    isbn_or_key = 'key'
    if len(word) == 13 and word.isdigit():
        isbn_or_key = 'isbn'
    short_word = word.replace('-', '')
    if '-' in word and len(short_word) == 10 and short_word.isdigit():
        isbn_or_key = 'isbn'
    return isbn_or_key
# -*- coding:utf-8 -*-
# Create by 27
# @Time : 2020/3/5 00:59
__author__ = '27'
class BookViewModel:
    def __init__(self, book):  # 处理单本数据，如果要处理集合数据，那先把单本的数据处理好
        self.title = book['title']
        self.publisher = book['publisher']
        self.author = '、'.join(book['author'])
        self.image = book['image']
        self.price = book['price']
        self.summary = book['summary']
        self.isbn = book['isbn']
        self.pages = book['pages']
        self.pubdate = book['pubdate']
        self.binding = book['binding']

    # 如果一个方法对数据处理且返回数据，不妨把它按照属性来看待，那么html模板里调用的时候就无需使用括号了，更方便适用与阅读
    @property
    def intro(self):
        intros = filter(lambda x: True if x else False,
                        [self.author, self.publisher, self.price])

        return ' / '.join(intros)


class BookCollection:
    def __init__(self):
        self.total = 0
        self.books = []
        self.keyword = ''

    def fill(self, yushu_book, keyword):
        self.total = yushu_book.total
        self.keyword = keyword
        self.books = [BookViewModel(book) for book in yushu_book.books]


class _BookViewModel:   # 不用了
    # 描述特征（类变量，实例变量）
    # 行为（方法）
    @classmethod
    def package_single(cls, data, keyword):
        returned = {
            'book': [],
            'total': 0,
            'keyword': keyword
        }
        if data:
            returned['total'] = 1
            returned['books'] = [cls.__cut_book_data(data)]
        return returned

    @classmethod
    def package_collections(cls):
        pass

    @classmethod
    def __cut_book_data(cls, data):
        book = {
            'title': data['title'],
            'publisher': data['publisher'],
            'pages': data['pages'],
            'author': '、'.join(data['author']),
            'price': data['price'],
            'summary': data['summary'],
            'image': data['image']
        }
        return book


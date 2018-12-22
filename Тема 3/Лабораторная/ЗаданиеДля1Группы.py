# задание для подгруппы 1
# Галкин Антон |  ИВТ | 3 курс | 1 подгруппа
"""
  Лабораторная работа 18.10.2018
  1 подгруппа 3ИВТ/16

  Описание задачи:
  Разработать фрагмент объектно-ориентированного кода для приложения, позволяющего бронировать книги.

  Доделать:
  Реализовать сохранение книг, взятых пользователем.

  Реализовать тесты с использованием одной из библиотек для тестирования

"""


class Book:
    def __init__(self, author, title):
        self.author = author
        self.title = title

    def __repr__(self):
        return "Book: " + self.author + " – " + self.title

    def __str__(self):
        return "Book: " + self.author + " – " + self.title


class User:
    def __init__(self):
        self.__books = list()

    def show_books(self):
        for b in self.__books:
            print(b)

    def borrow_book(self, book):
        if not isinstance(book, Book):
            raise TypeException
        self.__books.append(book)


b1 = Book('Nick', 'book1')
b2 = Book('Anton', 'book2')
u1 = User()
u1.borrow_book(b1)
u1.borrow_book(b2)
u1.show_books()
class Book:
    def __init__(self, title, author, pages, year):
        self.year = year
        self.pages = pages
        self.author = author
        self.title = title


class DigitBook(Book):
    def __init__(self, title, author, pages, year, size, frm):
        super().__init__(title, author, pages, year)
        self.size = size
        self.frm = frm


book = Book('title', 'author', 42, 2000)
db = DigitBook('title2', 'author2', 43, 1900, 55, 'frm')

print(db.frm)

class Author:

    all_authors = []

    def __init__(self,name : str):
        self.name = name
        Author.all_authors.append(self)


class Book:

    all_books = []

    def __init__(self,title : str):
        self.title = title
        Book.all_books.append(self)


class Contract:

    all_contracts = []

    def __init__(self,author : Author,book : Book,date : str,royalties : int):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all_contracts.append(self)
        
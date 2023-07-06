class Book:
    _TotalBooks = 0 #init value
    _average_page = 0
    _listofbook = []

    def __init__(self, *args, **kwargs):
        self._name = kwargs.get('name')
        self._author = kwargs.get('author')
        self._cover_type = kwargs.get('cover_type')
        self._publication_date = kwargs.get('publication_date')
        self._language = kwargs.get('language')
        self._print_length = kwargs.get('print_length')
        Book._TotalBooks += 1
        Book._average_page = (self._print_length + Book._average_page)//Book._TotalBooks
        Book._listofbook.append(self)

    def __del__(self):
        Book._TotalBooks -= 1
        Book._listofbook.remove(self)
        Book._average_page = sum(book._print_length for book in Book._listofbook) // Book._TotalBooks if Book._TotalBooks > 0 else 0
    @property
    def Name(self):
        return self._name
    @Name.setter
    def Name(self,value):
        self._name = value
    @Name.getter
    def Name(self):
        return self._name

    @property
    def author(self):
        return self._author
    @author.setter
    def author(self,value):
        self._author=value
    @author.getter
    def author(self):
        return self._author

    @property
    def cover_type(self):
        return self._cover_type;

    @cover_type.setter
    def cover_type(self,value):
        self._cover_type = value
    @cover_type.getter
    def cover_type(self):
        return self._cover_type


    @property
    def language(self):
        return self._language
    @language.getter
    def language(self):
        return self._language
    @language.setter
    def language(self,value):
        set._language=value

    @property
    def publication_date(self):
        return self._publication_date
    @publication_date.setter
    def publication_date(self,value):
        self._publication_date=value

    @publication_date.getter
    def publication_date(self):
        return self._publication_date


    @staticmethod
    def get_totalbooks():
        return Book._TotalBooks

    @classmethod
    def get_average_page(cls):
        return cls._average_page

    @classmethod
    def search_by_name(cls, otherbook):
        if isinstance(otherbook, Book):
            for book in cls._listofbook:
                if book._name == otherbook._name and book._author == otherbook._author:
                    return book
            return None
        else:
            return None

    @classmethod
    def arrange_by_name(cls):
        return  sorted(cls._listofbook,key=lambda book: book._name)
    @classmethod
    def arrange_by_length(cls):
        return sorted(cls._listofbook,key=lambda book: book._print_length)


    def __eq__(self,other_book):
        if isinstance(other_book,Book):
            return self._name == other_book._name  and self._publication_date == other_book._publication_date and self._author == other_book._author
        return False
    def __lt__(self,other_book):
        if isinstance(other_book,Book):
            return self._publication_date<other_book._publication_date
    def __repr__(self):
        attributes = [f"{attribute}: {value}" for attribute, value in self.__dict__.items() if value is not None]
        return "\n".join(attributes)



book1 = Book(name='cPython Crash Course', author='Eric Matthes', cover_type='Paperback', publication_date='2015', language='English', print_length = 560)
book2 = Book(name='bPython Crash Course', author='Eric Matthes', cover_type='Paperback', publication_date='2015', language='English', print_length = 562)
book2 = Book(name='aPython Crash Course', author='Eric Matthes', cover_type='Paperback', publication_date='2015', language='English', print_length = 564)
print(book1)
"""
print(book1)
print("-----")
print(book2.Name)
print(book1.author)
print(book1==book2)
print(Book._average_page)
print(Book.search_by_name(book2))
tempt=Book.arrange_by_name()
print(tempt)
print("-----")
tempt=Book.arrange_by_length()
print(tempt)
"""
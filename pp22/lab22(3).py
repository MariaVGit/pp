class Book:
    def __init__(self, title, author, publisher, year):
        self.__title = title
        self.__author = author
        self.__publisher = publisher
        self.__year = year

    def show_short_info(self):
        print(f"tytuł: {self.__title} autor: {self.__author}")
    def show_full_info(self):
        print(f"tytuł: {self.__title} autor: {self.__author} wydawca: {self.__publisher} rok: {self.__year}")

books = []
books.append(Book("Dzieci z Bullerbyn","Astrid Lindgren","Nasza Księgarnia",1999))
books.append(Book("Moby Dick","Herman Malville","Amercom",2009))

for book in books:
    book.show_full_info()


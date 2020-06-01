import datetime

class Document:
    def __init__(self, authors, date):
        self.__authors = authors
        self.__date = date
    def getAuthors(self):
        return self.__authors
    def addAuthors(self, name):
        self.__authors.append(name)
    def getDate(self):
        return self.__date

class Book(Document):
    def __init__(self, authors, date, title):
        super().__init__(authors, date)
        self.__title = title
    def getTitle(self):
        return self.__title

class EMail(Document):
    def __init__(self, authors, date, subject, to):
        super().__init__(authors, date)
        self.__subject = subject
        self.__to = to
    def getSubject(self):
        return self.__subject
    def getTo(self):
        return self.__to

d1 = Document(["Bruno", "Heitor"], datetime.datetime(2020, 5, 20))
d2 = Book(["J. R. R. Tolkien"], datetime.datetime(1954, 7, 29), "The Lord of the Rings")
d3 = EMail(["Bruno"], datetime.datetime.now(), "Exercícios de Python", ["Evandro"])

print("Doc - Autores:", d1.getAuthors(), "Data:", d1.getDate().strftime("%x"))
print("Livro", d2.getTitle(), "- Autores:", d2.getAuthors(), "Data:", d2.getDate().strftime("%x"))
print("Email", d3.getSubject(), "- Para:", d3.getTo(), "- Autores:", d3.getAuthors(), "Data:", d3.getDate().strftime("%x"))

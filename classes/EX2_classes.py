class Book:
    def __init__(self, name, pages, author, price):
        self.__name = name
        self.__pages = pages
        self.__author = author
        self.__price = price
    def mostraLivro(self):
        print(
            "Livro: %s\nQuantidade de páginas: %d\nAutor: %s\nPreço: %0.2f"
            %(self.__name, self.__pages, self.__author, self.__price)
        )
    def getPrice(self):
        return round(self.__price, 2)
    def setPrice(self, price):
        self.__price = price

livros = []
for i in range(3):
    name = input("Entre com o nome do livro " + str(i + 1) + ": ")
    pages = int(input("Entre com a quantidade de páginas do livro " + str(i + 1) + ": "))
    author = input("Entre com o autor do livro " + str(i + 1) + ": ")
    price = float(input("Entre com o preço do livro " + str(i + 1) + ": "))
    print("\n")
    livros.append(Book(name, pages, author, price))

livros[0].mostraLivro()
livros[1].mostraLivro()
livros[2].mostraLivro()
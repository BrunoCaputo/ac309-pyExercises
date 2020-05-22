class Cart:
    def __init__(self):
        self.__produtos = []
    def inserirProduto(self, product, quantity):
        product.setQuantity(quantity)
        self.__produtos.append(product)
    def listaProduto(self):
        return self.__produtos
    def somaTotal(self):
        total = 0
        for i in self.__produtos:
            total += i.getValorProduto()
    
class Product:
    def __init__(self, name, price):
        self.__nomeProduto = name
        self.__quantity = 0
        self.__valorProduto = price
    def setQuantity(self, quantity):
        self.__quantity += quantity
    def getQuantity(self):
        return self.__quantity
    def getNomeProduto(self):
        return self.__nomeProduto
    def getValorProduto(self):
        return self.__valorProduto

product1 = Product("Celular", 1500.0)
product2 = Product("Mesa", 500.95)

cart = Cart()
cart.inserirProduto(product1, 1)
cart.inserirProduto(product2, 2)
for i in cart.listaProduto():
    print(
        "%dx %s - R$%0.2f"
        %(i.getQuantity(), i.getNomeProduto(), float(i.getQuantity() * i.getValorProduto()))
    )

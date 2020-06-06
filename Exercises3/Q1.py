# Crie uma Classe Pessoa, contendo os atributos encapsulados, com seus respectivos seletores
# (getters) e modificadores (setters), e ainda o construtor padrão e pelo menos mais dois
# métodos conforme sua percepção sobre o problema. 
# Atributos: nome (String); endereço (String); telefone (String);

class Pessoa:
    def __init__(self, name, address, phone):
        self.__nome = name
        self.__endereco = address
        self.__telefone = phone
    def ehAmigo(self, person):
        print("%s e %s são amigos!" %(self.__nome, person.getNome()))
    def estuda(self):
        print("%s está estudando!" %(self.__nome))
    def getNome(self):
        return self.__nome
    def setNome(self, name):
        self.__nome = name
    def getEndereco(self):
        return self.__endereco
    def setEndereco(self, address):
        self.__endereco = address
    def getTelefone(self):
        return self.__telefone
    def setTelefone(self, phone):
        self.__telefone = phone

p1 = Pessoa(
    input("Entre com o nome: "),
    input("Entre com o endereço: "),
    input("Entre com o telefone: ")
    )
p2 = Pessoa(
    input("Entre com o nome: "),
    input("Entre com o endereço: "),
    input("Entre com o telefone: ")
    )
p1.ehAmigo(p2)
p2.estuda()
# Implemente a classe Vendedor como subclasse da classe Empregado.
# Um determinado vendedor tem como atributos, para além dos atributos da classe Pessoa
# e da classe Empregado, o atributo valorVendas (correspondente ao valor monetário dos
# artigos vendidos) e o atributo comissão (porcentagem do valorVendas que será adicionado
# ao vencimento base do Vendedor). Note que deverá redefinir nesta subclasse o método herdado
# calcularSalario (o salário de um vendedor é equivalente ao salário de um empregado usual
# acrescido da referida comissão). Escreva um programa de teste adequado para esta classe.

class Pessoa:
    def __init__(self, name, address, phone):
        self.__nome = name
        self.__endereco = address
        self.__telefone = phone

    def ehAmigo(self, person):
        print("%s e %s são amigos!" % (self.__nome, person.getNome()))

    def estuda(self):
        print("%s está estudando!" % (self.__nome))

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


class Empregado(Pessoa):
    def __init__(self, name, address, phone, cod, baseSal, fee):
        super().__init__(name, address, phone)
        self.__codigoSetor = cod
        self.__salarioBase = baseSal
        self.__imposto = fee

    def calcularSalario(self):
        return round(self.__salarioBase * (1 - (self.__imposto / 100.0)), 2)

    def getCodigoSetor(self):
        return self.__codigoSetor

    def setCodigoSetor(self, cod):
        self.__codigoSetor = cod

    def getSalarioBase(self):
        return self.__salarioBase

    def setSalarioBase(self, baseSal):
        self.__salarioBase = baseSal

    def getImposto(self):
        return self.__imposto

    def setTelefone(self, fee):
        self.__imposto = fee


class Vendedor(Empregado):
    def __init__(self, name, address, phone, cod, baseSal, fee, sellVal, comission):
        super().__init__(name, address, phone, cod, baseSal, fee)
        self.__valorVendas = sellVal
        self.__comissao = comission

    def calcularSalario(self):
        comissao = self.__valorVendas * (1 + (self.__comissao / 100))
        return super().calcularSalario() + comissao

    def getValorVendas(self):
        return self.__valorVendas

    def setValorVendas(self, sellVal):
        self.__valorVendas = sellVal

    def getComissao(self):
        return self.__comissao

    def setComissao(self, comission):
        self.__comissao = comission


v1 = Vendedor(
    input("Entre com o nome: "),
    input("Entre com o endereço: "),
    input("Entre com o telefone: "),
    int(input("Entre com o código do setor: ")),
    float(input("Entre com o salário base: ")),
    float(input("Entre com o imposto (0 - 100)%: ")),
    float(input("Entre com o valor de vendas: ")),
    float(input("Entre com a comissão (0 - 100)%: ")),
)
print("Salário: R$%.2f" % v1.calcularSalario())

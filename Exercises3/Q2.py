# Considere, como subclasse da classe Pessoa, a classe Empregado.
# Considere que cada instância da classe Empregado tem, para além dos atributos que
# caracterizam a classe Pessoa, os atributos codigoSetor (inteiro), salarioBase (vencimento base)
# e imposto (porcentagem retida dos impostos).
# Implemente a classe Empregado com métodos seletores e modificadores e um método calcularSalario().
# Escreva um programa de teste adequado para a classe Empregado.

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
        
e1 = Empregado(
    input("Entre com o nome: "),
    input("Entre com o endereço: "),
    input("Entre com o telefone: "),
    int(input("Entre com o código do setor: ")),
    float(input("Entre com o salário base: ")),
    float(input("Entre com o imposto (0 - 100)%: "))
)
print("Salário: R$%.2f" %e1.calcularSalario())
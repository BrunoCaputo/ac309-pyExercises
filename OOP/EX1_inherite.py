class Funcionario:
    def __init__(self, name, cpf, sal):
        self.__nome = name
        self.__cpf = cpf
        self.__salario = sal
    def getNome(self):
        return self.__nome
    def getCpf(self):
        return self.__cpf
    def getSalario(self):
        return self.__salario
    def setCpf(self, cpf):
        self.__cpf = cpf
    def setSalario(self, sal):
        self.__salario = sal
    def aumentaSalrio(self, perc):
        self.__salario += self.__salario * perc / 100

class Gerente(Funcionario):
    def __init__(self, name, cpf, sal, add, qtt):
        super().__init__(name, cpf, sal)
        self.__adicionalSalario = add
        self.__qtdGerenciados = qtt
    def getQtd(self):
        return self.__qtdGerenciados
    def setQtd(self, qtt):
        self.__qtdGerenciados = qtt
    def getAdicional(self):
        return self.__adicionalSalario
    def setAdicional(self, add):
        self.__adicionalSalario = add

f1 = Gerente("Bruno", "111.111.111-11", 5000.0, 10, 5)
f2 = Funcionario("Joãozinho", "222.222.222-22", 3000.0)

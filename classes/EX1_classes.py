# Implemente a classe Funcionário. Um funcionário tem um nome e um Salário como atributo.
# Os métodos devem ser: cadastraFuncionário, aumentarSalario (que aumente o salário do 
# funcionário em uma certa porcentagem digitada como entrada de dados) e mostrarSalario.

class Employee:
    def __init__(self):
        self.__name = ""
        self.__sal = 0.0
    def cadastraFuncionario(self, name, sal):
        self.__name = name
        self.__sal = sal
    def aumentarSalario(self, perc):
        self.__sal += (self.__sal * perc / 100)
    def mostrarSalario(self):
        print("O salário de %s é de R$%0.2f" %(self.__name, self.__sal))

name = input("Entre com o nome do funcionário: ")
sal = float(input("Entre com o salário do funcionário: "))
funcionario1 = Employee()
funcionario1.cadastraFuncionario(name, round(sal, 2))
funcionario1.mostrarSalario()
funcionario1.aumentarSalario(5)
funcionario1.mostrarSalario()
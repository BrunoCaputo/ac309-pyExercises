# Crie um programa capaz de ler vários números e colocá-los em uma lista. Depois disso, mostre:
# a. Quantos números foram digitados; 
# b. A lista de valores ordenada de forma decrescente; 
# c. Se o valor 5 está ou não dentro da lista.
from random import randint

qtt = randint(1, 10)  #Gera um número aletatório entre 1 e 10, inclusive
numbers = []

for i in range(qtt):
    num = int(input("Entre com um número: "))
    numbers.append(num)

print("Quantidade de números digitados:", len(numbers))
numbers.sort()
print("Lista em ordem crescente:", numbers)
has5 = "Sim" if 5 in numbers else "Não"
print("Tem o valor 5? %s" %has5)

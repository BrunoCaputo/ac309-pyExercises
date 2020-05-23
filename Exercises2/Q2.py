# Crie um programa que leia vários números e os coloque em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores pares
# e os valores ímpares da primeira lista, respectivamente.
# No final, mostre o conteúdo das três listas geradas.
from random import randint

qtt = randint(1, 10)  #Gera um número aletatório entre 1 e 10, inclusive
numbers = []
even = []
odd = []

for i in range(qtt):
    num = int(input("Entre com um número: "))
    numbers.append(num)
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)

numbers.sort()
print("Lista original:", numbers)
even.sort()
print("Pares:", even)
odd.sort()
print("Ímpares:", odd)

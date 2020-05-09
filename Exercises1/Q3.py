# Faça um algoritmo que leia o preço de um produto e o desconto e mostre seu novo preço
# com de desconto;
# O calculo do desconto deve ser feito em uma função.

price = float(input("Entre com o preço do produto: "))
discount = float(input("Entre com o desconto: "))

def calcDiscount(price, discount):
    return round(price - discount, 2)

val = calcDiscount(price, discount)
if val < 0:
    print("Desconto maior que o preço")
else:
    print("O preço com desconto é:", val)
# Faça um programa que leia um número de 0 a 9999 e mostre na tela:
# qual é o número da unidade, dezena, centena e milhar

num = int(input("Entre com um número de 0 a 9999: "))

if num < 0 or num > 9999:
    print("Fora da faixa!")
elif num >= 1000:
    t = int(num / 1000)
    h = int((num - (t * 1000)) / 100)
    d = int((num - (t * 1000) - (h * 100)) / 10)
    u = int((num - (t * 1000) - (h * 100) - (d * 10)))
    print("Unidade:", u, ", Dezena:", d, ", Centena:", h, ", Milhar:", t)
elif num >= 100:
    h = int((num) / 100)
    d = int((num - (h * 100)) / 10)
    u = int((num - (h * 100) - (d * 10)))
    print("Unidade:", u, ", Dezena:", d, ", Centena:", h)
elif num >= 10:
    d = int((num) / 10)
    u = int((num - (d * 10)))
    print("Unidade:", u, ", Dezena:", d)
else:
    print("Unidade:", num)
    
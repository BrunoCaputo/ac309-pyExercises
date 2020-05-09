# Faça um programa que leia o peso de cinco pessoas e no final mostre
# qual foi o maior e o menor peso lido

w = []

for i in range(5):
    w.append(round(float(input("Entre com o" + str(i + 1) + "º peso em kg: ")), 2))

w.sort()

print("Menor peso lido:", str(w[0]) + "kg")
print("Maior peso lido:", str(w[-1]) + "kg")
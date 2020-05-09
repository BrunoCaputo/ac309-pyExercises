# Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0.50 por Km para viagens até 200Km e R$0.45
# para viagens mais longas

def calcPrice(dist):
    if dist <= 200:
        return dist * 0.5
    else:
        return dist * 0.45

dist = float(input("Entre com a distância em km: "))
price = calcPrice(dist)

print("O preço da passagem é", "R$" + str(price))
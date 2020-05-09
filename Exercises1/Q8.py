# Escreva um programa que leia a velocidade de um carro.
# Se ele não ultrapassar 80Km/h, deseje a ele boa viagem, senão,
# mostre a ele duas mensagens: uma mensagem dizendo que ele foi multado
# e outra com o valor total da multa (R$50.00 por cada Km acima do limite);

def calcTt(vel):
    return round((vel - 80) * 50.0, 2)

vel = int(input("Entre com a velocidade do carro: "))

if vel <= 80:
    print("Tenha uma boa viagem!")
else:
    trafficTicket = calcTt(vel)
    print("Você foi multado!")
    print("Sua velocidade era de", str(vel) + "km/h.", "Sua multa é de", "R$" + str(trafficTicket))


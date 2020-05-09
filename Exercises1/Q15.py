# Elabore um programa que, ao inserir o valor de um produto e sua condição de pagamento,
# ele informe o seguinte: Se for pagamento à vista, mostre o preço do produto com 10% de desconto;
# Se for cartão à vista, mostre o preço com 5% de desconto; Se for cartão mas parcelado,
# mostre o preço do produto 15% mais caro

payment = [1, 2, 3]
val = float(input("Entre com o valor do produto: "))
pay = int(input("Entre com o tipo de pagamento (1) - à vista (2) - cartão à vista (3) - cartão parcelado: "))

while not pay in payment:
    print ("Opção inválida!")
    pay = int(input("Entre com o tipo de pagamento (1) - à vista (2) - cartão à vista (3) - cartão parcelado: "))

if pay == 1:
    print("À vista - 10% de desconto")
    newVal = round(val * 0.9, 2)
    print("Novo valor:", "R$" + str(newVal))
elif pay == 2:
    print("Cartão à vista - 5% de desconto")
    newVal = round(val * 0.95, 2)
    print("Novo valor:", "R$" + str(newVal))
else:
    print("Cartão parcelado - 15% de acréscimo")
    newVal = round(val * 1.15, 2)
    print("Novo valor:", "R$" + str(newVal))
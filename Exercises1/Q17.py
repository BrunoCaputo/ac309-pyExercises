# Crie um programa que leia o ano de nascimento de 7 pessoas e diga quantas delas
# já são maiores de idade (>= 18)

ages = []
adult = 0

for i in range(7):
    y = int(input("Entre com o " + str(i + 1) + "º ano de nascimento: "))
    ages.append(2020 - y)

for i in ages:
    if i >= 18:
        adult += 1

if adult == 0:
    print("Não há maiores de idade!")
elif adult == 7:
    print("Todos são maiores de idade!")
else:
    print("Há", adult, "maiores de idade!")

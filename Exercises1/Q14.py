# Desenvolva um programa que leia o peso e a altura de uma pessoa,
# calcule seu IMC e mostre seu status, de acordo com as informações:
# < 18.5 - Abaixo do peso;
# entre 18.5 e 25 - Peso ideal;
# 25 até 30 - Sobrepeso;
# 30 até 40 - Obesidade;
# Acima de 40 - Obesidade Mórbida

def calcBmi(w, h):
    bmi = w / (h ** 2)
    if bmi < 18.5:
        return "Abaixo do peso"
    elif bmi < 25:
        return "Peso ideal"
    elif bmi < 30:
        return "Sobrepeso"
    elif bmi < 40:
        return "Obesidade"
    else:
        return "Obesidade Mórbida"

w = float(input("Entre com o peso em kg: "))
h = float(input("Entre com a altura em m: "))

bmi = calcBmi(w, h)

print("IMC - Status:", bmi)
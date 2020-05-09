# Escreva um programa que pergunte o salário de um funcionário e calcule
# o valor do seu aumento. Para salários superiores a R$1500, dê um aumento de 10%.
# Para salários menores ou iguais a R$1500 dê um aumento de 15%;

def greaterSal(sal):
    if sal > 1500:
        return round(sal * 1.1, 2)
    else:
        return round(sal * 1.15, 2)

sal = float(input("Entre com o salário: "))

newSal = greaterSal(sal)

print("Salário com aumento:", "R$" + str(newSal))
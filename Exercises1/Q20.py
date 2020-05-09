# Crie um programa que leia dois valores e mostre um menu na tela com as seguintes opções:
# 1 – Somar;
# 2 – Multiplicar;
# 3 – Qual é o maior número;
# 4 – Sair do programa

def s(n1, n2):
    return round(n1 + n2, 2)

def mult(n1, n2):
    return round(n1 * n2, 2)

def greater(n1, n2):
    if n1 > n2:
        return round(n1, 2)
    else:
        return round(n2, 2)

num1 = float(input("Entre com o 1º valor: "))
num2 = float(input("Entre com o 2º valor: "))

op = 0

while op != 4:
    print("\nSelecione uma opção:")
    print("1 - Somar")
    print("2 - Multiplicar")
    print("3 - Maior número")
    print("4 - Sair")
    op = int(input("Opção escolhida -> "))
    while op < 1 or op > 4:
        print("Opção inválida!")
        op = int(input("Opção escolhida -> "))
    
    if op == 1:
        print("A soma é:", s(num1, num2))
    elif op == 2:
        print("A multiplicação é:", mult(num1, num2))
    elif op == 3:
        if num1 == num2:
            print("São iguais")
        else:
            print("O maior é:", greater(num1, num2))

print("\nSaindo...")
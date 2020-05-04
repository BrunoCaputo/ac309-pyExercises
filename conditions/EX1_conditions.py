N1 = int(input("Entre com a nota 1: "))
N2 = int(input("Entre com a nota 2: "))

media = (N1 + N2) / 2

if media >= 60:
    print("Aprovado")
elif 30 <= media < 60:
    print("Em exame")
else:
    print("Reprovado")
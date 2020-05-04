n = int(input("Entre com um número de 1 a 10: "))
tabuada = list()

if n > 10 or n <= 0:
    print("Fora da faixa de valores")
else:
    for i in range(1, 11):
        tabuada.append(n * i)
    print(tabuada)
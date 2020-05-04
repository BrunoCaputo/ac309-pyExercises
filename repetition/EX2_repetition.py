print("Entre com 10 notas")
notas = list();
for i in range(10):
    x = int(input("Nota " + str(i + 1) + ": "))
    notas.append(x)
media = sum(notas) / len(notas)
print(media)
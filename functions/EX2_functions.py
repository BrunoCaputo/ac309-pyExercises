def numeraLista(lista):
    count = 1
    for i in lista:
        print("Elemento " + str(count) + ": " + str(i))
        count += 1


L = ["teste", 5, 10, 9.5]
numeraLista(L)
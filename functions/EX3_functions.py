def mean(lista):
    media = sum(lista) / len(lista)
    return round(media, 2) 

L = [50, 60, 100, 23, 30, 98, 55]
print(mean(L))
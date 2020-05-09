# Faça um programa que leia a largura e altura de uma parede em metros e calcule a sua área.
# Em seguida, mostre também a quantidade de tinta necessária para pintá-la,
# sabendo que cada litro de tinta pinta uma área de 2m²

def calcArea(w, h):
    return round(w * h, 2)
def calcPaint(area):
    return round(area / 2.0, 2)

h = float(input("Entre com a altura: "))
w = float(input("Entre com a largura: "))

area = calcArea(w, h)
paint = calcPaint(area)

print("A quantidade de tinta para", str(area) + "m²", "é de", str(paint) + "l")
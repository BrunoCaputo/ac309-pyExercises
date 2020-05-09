# Escreva um programa que leia um valor em metros e o exiba convertido
# em centímetros e milímetros; O calculo de conversão deve ser feito em uma função.

def convertToCm(meter):
    return round(meter * 100, 2)
def convertToMm(meter):
    return round(meter * 1000, 2)

meter = float(input("Entre com um valor em metros: "))

cm = convertToCm(meter)
mm = convertToMm(meter)

print(str(meter) + "m", "em cm:", str(cm) + "cm", "e em mm:", str(mm) + "mm")
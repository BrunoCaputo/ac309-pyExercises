import math

x = int(input("Entre com um número:"))

log10 = math.log10(x)
log2 = math.log2(x)
sqrt = math.sqrt(x)
sin = math.sin(x)
print(
    "Log 10:", log10,
    "\nLog 2:", log2,
    "\nRaíz Quadrada:", sqrt,
    "\nSeno:", sin)
print(math.pi, math.e)
import matplotlib.pyplot as plt
import math

x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
root = []
euler = []
thirdDegree = []

for i in x:
    y = math.sqrt(i)
    root.append(y)
    y = math.e ** i
    euler.append(y)
    y = pow(i, 3) + 2 * i
    thirdDegree.append(y)


plt.title("Funções")
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")
plt.ylim(top=20)
plt.plot(x, root, 'r', label="\u221Ax") #\u221A = square root symbol
plt.plot(x, euler, 'b', label="e^x")
plt.plot(x, thirdDegree, 'g', label="x³+2x")
plt.legend(loc=2)
plt.grid(True)
plt.show()
plt.savefig('plot/Grafico.pdf', transparent=True, format='pdf')
print("Imagem salva!")

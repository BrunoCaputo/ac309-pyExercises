import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6, 7]
minT = [14, 14, 13, 13, 12, 15, 14]
maxT = [23, 25, 27, 28, 28, 27, 28]

plt.title("Temperaturas em São Paulo - Setembro de 2019")
plt.xlabel("Dias")
plt.ylabel("Temperatura (°C)")
plt.plot(x, minT, 'r', label="Temp. Mínima")
plt.plot(x, maxT, 'b', label="Temp. Máxima")
plt.legend(loc=2)
plt.grid(True)
plt.show()

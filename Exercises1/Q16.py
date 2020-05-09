# Desenvolva um programa que leia seis números inteiros e mostre a soma
# total apenas daqueles que forem ímpares

s = 0
nums = []

for i in range(6):
    nums.append(int(input("Entre com o " + str(i + 1) + "º número: ")))

for i in nums:
    if i % 2 != 0:
        s += i

if s == 0:
    print("Não há números ímpares!")
else:
    print("A soma dos números ímpares é:", s)
# Faça um programa que leia três números e mostre qual é o maior e qual é o menor

nums = []

for i in range(3):
    nums.append(int(input("Entre com o " + str(i + 1) + "º número: ")))

nums.sort()

print("Menor número:", nums[0], ", Maior número:", nums[-1])
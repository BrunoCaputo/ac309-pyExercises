var = input("Digite o nome completo: ")

upper = var.upper()
print("Maiúsculo:", upper)

lower = var.lower()
print("Minúsculo:", lower)

length = len(var)
print("Comprimento:", length)

count_a = var.count('a')
print("Quantidade de a:", count_a)

name = var.split(" ")
last_name = name[-1]
var.replace(last_name, "do Inatel")
print(var)
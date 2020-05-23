# Crie um programa que leia nome, sexo e idade de várias pessoas,
# guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
# No final, mostre: 
# a. Quantas pessoas foram cadastradas; 
# b. A média de idade do grupo; 
# c. Uma lista com todas as mulheres; 
# d. Uma lista com todas as pessoas com idade acima da média
from random import randint

qtt = randint(1, 4)  #Gera um número aletatório entre 1 e 4, inclusive
person = []
women = []
overMean = []

for i in range(qtt):
    name = input("Entre com o nome da " + str(i + 1) + "ª pessoa: ")
    gender = input("Entre com o sexo da " + str(i + 1) + "ª pessoa: ")
    age = int(input("Entre com a idade da " + str(i + 1) + "ª pessoa: "))
    person.append({"name": name, "gender": gender, "age": age})
    if gender == 'F':
        women.append({"name": name, "gender": gender, "age": age})

personQtt = len(person)
print("Quantidade de pessoas cadastradas:", personQtt)
totalAge = 0
for i in person:
    totalAge += i["age"]
mean = totalAge / personQtt
print("A média da idade do grupo é de %0.1f anos" %mean)
if len(women) > 0:
    print("Mulheres do grupo:")
    for i in women:
        print(
            "Nome: %s, Idade: %d anos" %(i["name"], i["age"]))
else:
    print("Não há mulheres no grupo")
for i in person:
    if i["age"] > mean:
        overMean.append(i)
if len(overMean) > 0:
    print("Pessoas com idade acima da média:")
    for i in overMean:
        print(
            "Nome: %s, Sexo: %s, Idade: %d anos"
            %(i["name"], "Masculino" if i["gender"] == "M" else "Feminino", i["age"])
        )
else:
    print("Não há pessoas com idade acima da média")
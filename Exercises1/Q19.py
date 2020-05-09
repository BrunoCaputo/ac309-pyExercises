# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final, mostre: 
# A média de idade do grupo;
# Qual o nome do homem mais velho;
# Quantas mulheres têm menos de 20 anos

people = []

for i in range(4):
    person = []
    person.append(input("Entre com o nome da " + str(i + 1) + "º pessoa: "))
    person.append(int(input("Entre com a idade da " + str(i + 1) + "º pessoa: ")))
    person.append(input("Entre com o sexo da " + str(i + 1) + "º pessoa - M ou F: "))
    people.append(person)

ages = 0
older = 0
older_name = ""
women = 0
for i in people:
    ages += i[1]
    if i[2] == 'M':
        if i[1] > older:
            older = i[1]
            older_name = i[0]
    if i[1] < 20 and i[2] == 'F':
        women += 1

print("A média de idade é:", round(ages / len(people), 2))
print("O homem mais velho é:", older_name)
if women == 0:
    print("Não há mulheres menores de 20 anos no grupo!")
else:
    print("Há", women, "mulheres menores de 20 anos")
# A confederação nacional de natação precisa de um programa que leia o ano de nascimento
# de um atleta e mostre sua categoria, de acordo com sua idade:
# Até 9 anos - MIRIM;
# Até 14 anos - INFANTIL;
# Até 19 anos - JÚNIOR;
# Até 20 anos - SENIOR;
# ACIMA de 20 - MASTER

def selectCategory(year):
    age = 2020 - year
    if age <= 9:
        return "MIRIM"
    elif age <= 14:
        return "INFANTIL"
    elif age <= 19:
        return "JÚNIOR"
    elif age <= 20:
        return "SENIOR"
    else:
        return "MASTER"

y = int(input("Entre com o ano de nascimento: "))

cat = selectCategory(y)

print("Categoria:", cat)

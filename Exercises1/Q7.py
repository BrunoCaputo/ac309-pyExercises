# Crie um programa que leia o nome de uma pessoa e diga se ela tem Silva no nome

name = input("Entre com o nome completo: ")
nameLower = name.lower()

if nameLower.find("silva") != -1:
    print("Contém Silva!")
else:
    print("Não contém Silva!")

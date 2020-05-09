# Faça um programa que leia algo do teclado e mostre se o conteúdo é formado por letras,
# números ou caracteres alfanuméricos

inp = input("Entre com alguma coisa: ")

if inp.isnumeric():
    print("A entrada é formada por apenas números!")
elif inp.isalpha():
    print("A entrada é formado por apenas letras!")
elif inp.isalnum():
    print("A entrada é formada por números e letras!")
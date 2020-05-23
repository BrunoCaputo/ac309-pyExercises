# Faça um programa que leia o nome e a média de um aluno e guarde-os em um dicionário.
# Em seguida, a partir da média, gera a situação final do aluno “AP” ou “RP”
# e também guarde no dicionário. No final mostre o conteúdo do dicionário.
name = input("Entre com o nome do aluno: ")
mean = float(input("Entre com a média do alunos: "))
if mean >= 60.0:
    situation = "AP"
else:
    situation = "RP"
student = {
    "nome": name,
    "média": mean,
    "situação": situation
}

print(student)

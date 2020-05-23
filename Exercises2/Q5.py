# Crie um programa que gerencia o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou.
# Depois, o programa deve ler quantos gols o jogador fez em cada partida,
# calcular o total de gols e guardar tudo isso em um mesmo dicionário

name = input("Entre com o nome do jogador: ")
matchQtt = int(input("Entre com a quantidade de partidas: "))
goals = []
goalsQtt = 0

for i in range(matchQtt):
    matchGoals = int(input("Entre com a quantidade de gols na " + str(i + 1) + "ª partida: "))
    goals.append(matchGoals)
    goalsQtt += matchGoals

player = {
    "nome": name,
    "partidas": matchQtt,
    "gols_partida": goals,
    "gols_total": goalsQtt
}

print(
    "Jogador: %s\nPartidas Jogadas:%d\nGols em cada partida:"
    %(player["nome"], player["partidas"])
)
for i in range(len(player["gols_partida"])):
    print(
        "Gols na %dª partida: %d"
        %(i + 1, player["gols_partida"][i])
    )
print("Total de gols:", player["gols_total"])
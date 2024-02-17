# Escreva um programa que permita ao usuário votar em três opções diferentes e, no final, exiba o número de votos de cada opção.

votosDisponiveis = 3
votos = []
opcoes = {
    1: "Fulano",
    2: "Beltrano",
    3: "Ciclano"
}

print("Candidatos disponíveis para o voto:\n1. Fulano\n2. Beltrano.\n3. Ciclano")

for i in range(votosDisponiveis):
    print("Voto numero ", i + 1, " será: ")
    voto = int(input())
    votos.append(voto)

for opcao in opcoes.keys():   
    print("A quantidade de votos no", opcoes[opcao], "foram", votos.count(opcao))
       
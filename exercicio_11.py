# Faça um programa que simule o lançamento de um dado. O usuário deve escolher quantos dados jogar e o programa deve exibir os resultados.

import random


quantidadeDeLancamentos = int(input("Quantos lances de dados deseja fazer: "))

def numeroAleatorio():
    return random.randint(1,6)

for lance in range(quantidadeDeLancamentos):
    print("O dado do lance ", lance + 1, "o resultado é " , numeroAleatorio())
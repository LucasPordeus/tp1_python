# Escreva um programa que combine elementos aleatórios de listas diferentes (personagens, ações, locais) para criar uma história curiosa.

import random


def numeroAleatorio():
    return random.randint(1,4)

def criarHistoria():
    personagens = {
        1: "João",
        2: "Maria",
        3: "Lucas",
        4: "Pedro",
    }

    acoes = {
        1: " andou sozinho",
        2: " caiu no chão",
        3: " brincou de bola",
        4: " comprou sorvete"
        }

    local = {
        1: " no shopping",
        2: " no parque",
        3: " na escola",
        4: " em casa"
    }

    print(personagens[numeroAleatorio()], acoes[numeroAleatorio()], local[numeroAleatorio()])

criarHistoria()



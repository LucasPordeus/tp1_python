# Escreva um programa que receba dois nomes de usuário e os combine de maneira criativa para formar um novo nome.

primeiraEscolhaNome = input("Escolha um nome: ")
segundaEscolhaNome = input("Escolha outro nome: ")

def criarNomeCriativo(primeiroNome, segundoNome):
    tamanhoPrimeiroNome = len(primeiroNome)
    tamanhoSegundoNome = len(segundoNome)
    menorNome = min(tamanhoPrimeiroNome, tamanhoSegundoNome)
    nomeCriativo = ""
    for i in range(menorNome):
        if tamanhoPrimeiroNome == tamanhoSegundoNome:
            nomeCriativo += primeiroNome[i] + segundoNome[i]
        else:
            nomeCriativo += primeiroNome[i] + segundoNome[i + 1]
    
    return nomeCriativo

print("O resultado do nome criativo feito pela combinação entre os dois nomes é: ", criarNomeCriativo(primeiraEscolhaNome,segundaEscolhaNome))
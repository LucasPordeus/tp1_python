# Crie um programa que pergunte a idade do usuário e verifique se ele é maior de idade ou não.

def verificacaoMaiorDeIdade(idade):
    if(idade >= 18):
        print("É maior de idade!")
    else:
        print("É menor de idade!")

idade = int(input("Qual sua idade: "))

verificacaoMaiorDeIdade(idade)
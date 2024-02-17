# Faça um programa que calcule o Índice de Massa Corporal (IMC) do usuário e forneça feedback com base no valor (por exemplo, abaixo do peso, peso normal, sobrepeso).

def calcularImc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

print("Seu IMC é: ", calcularImc(peso, altura))
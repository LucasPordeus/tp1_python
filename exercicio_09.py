# Desenvolva um programa que aplique descontos diferentes com base no valor da compra: desconto de 10% para compras acima de R$100, 15% para compras acima de R$200, etc.

def aplicarDesconto(valor):
    if(valor >= 200):
        valorComDesconto = valor - (valor * 0.15)
    if(valor >= 100 and valor < 200):
        valorComDesconto = valor - (valor * 0.10)
    if(valor < 100):
        valorComDesconto = valor
    
    return valorComDesconto

valor = float(input("Qual o valor da sua compra: "))

print("O valor da sua compra com desconto é: ", aplicarDesconto(valor))
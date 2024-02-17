# Desenvolva um programa que peça ao usuário para escolher uma operação (adição, subtração, multiplicação, divisão) e dois números, e então execute a operação escolhida com os números.

def operacaoSoma(primeiroNumero, segundonumero):
    resultado = primeiroNumero + segundonumero
    print("O resultado da soma é ", resultado)

def operacaoSubtracao(primeiroNumero, segundoNumero):
    resultado = primeiroNumero - segundoNumero
    print("O resultado da subtração é ", resultado)

def operacaoMultiplicacao(primeiroNumero, segundoNumero):
    resultado = primeiroNumero * segundoNumero
    print("O resultado da multiplicação é ", resultado)

def operacaoDivisao(primeiroNumero, segundoNumero):
    resultado = primeiroNumero / segundoNumero
    print("O resultado da divisão é ", resultado)

def finalizarPrograma():
    print("Programa finalizado!")

operacoes = {
    1: operacaoSoma,
    2: operacaoSubtracao,
    3: operacaoMultiplicacao,
    4: operacaoDivisao,
}

operacao = 0

def interfaceDeEscolha():
    print("Escolha uma opção de operação matemática: ")
    print("1. SOMA\n2. SUBTRAÇÃO\n3. MULTIPLICAÇÃO\n4. DIVISÃO\n5. SAIR DO PROGRAMA")
   

while(operacao != 5):
    interfaceDeEscolha()
    operacao = int(input())

    if operacao == 5:
        finalizarPrograma()
    else:
        primeiroNumero = float(input("Escolha um número: "))
        segundoNumero = float(input("Escolha outro número: "))

        if operacao in operacoes:
            operacoes[operacao](primeiroNumero, segundoNumero)
        else:
            print("Operação inválida, escolha outra operação!")
    
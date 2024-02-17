# Crie um programa que peça ao usuário para inserir dois números e, em seguida, calcule e exiba a soma, subtração, multiplicação, divisão e divisão inteira desses números.

primeiroNumero = float(input("Escolha um número: "))
segundoNumero = float(input("Escolha outro número: "))

operacaoSoma = primeiroNumero + segundoNumero
operacaoSubtracao = primeiroNumero - segundoNumero
operacaoMultiplicacao = primeiroNumero * segundoNumero
operacaoDivisao = primeiroNumero / segundoNumero
operacaoDivisaoInteiro = int(primeiroNumero / segundoNumero)

print("\nOs resultados das operação básicas entre esses dois números são:")
print("1. SOMA = ", operacaoSoma)
print("2. SUBTRAÇÃO = ", operacaoSubtracao)
print("3. MULTIPLICAÇÃO = ", operacaoMultiplicacao)
print("4. DIVISÃO = ", operacaoDivisao)
print("5. DIVISÃO COM RESULTADO INTEIRO = ", operacaoDivisaoInteiro)
# Crie um programa que classifique as palavras inseridas pelo usuário como curtas (menos de 5 letras) ou longas (5 letras ou mais).

palavra = input("Digite uma palavra: ")
tamanhoPalavra = len(palavra)

if tamanhoPalavra < 5:
    print("A palavra é curta!")
else:
    print("A palavra é longa!")


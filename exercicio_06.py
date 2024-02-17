numeroSecreto = 7

def escolherNumero():
   numeroEscolhido = int(input("Qual o número secreto: ")) 
   return numeroEscolhido

numeroEscolhido = escolherNumero()

while(numeroEscolhido != numeroSecreto):
    if(numeroEscolhido > numeroSecreto):
        print("O número secreto é menor que o número escolhido, tente novamente!")
    if(numeroEscolhido < numeroSecreto):
        print("O número secreto é maior que o número escolhido, tente novamente!")
    numeroEscolhido = escolherNumero()

print("Você ganhou, acertou o número secreto que é ", numeroSecreto)
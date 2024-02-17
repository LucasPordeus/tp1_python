# Crie um programa que apresente ao usuário uma série de escolhas (como em uma história) e conduza a diferentes resultados com base nessas escolhas.

def filmeTerrorAlienigenas():
    print("Bem-vindo ao filme de terror alienígena!")
    print("Você está em uma estação espacial abandonada em um planeta distante...")
    print("Você ouve ruídos estranhos vindos de uma sala escura à sua frente e uma escotilha que leva ao exterior.")

    escolha = input("Você deseja investigar a sala escura ou abrir a escotilha? (sala/escotilha): ").lower()

    if escolha == "sala":
        print("Você decide investigar a sala escura...")
        print("Dentro da sala, você encontra destroços de equipamentos e manchas de sangue.")
        escolhaDestrocos = input("Você continua explorando ou volta para a escotilha? (explorar/voltar): ").lower()
        
        if escolhaDestrocos == "explorar":
            print("Enquanto explora, você encontra uma criatura alienígena escondida nas sombras.")
            print("Ela se aproxima rapidamente e você não tem para onde correr...")
            print("Você foi capturado pelos alienígenas!")
        elif escolhaDestrocos == "voltar":
            print("Você decide voltar para a escotilha.")
            print("No caminho de volta, você ouve ruídos estranhos se aproximando.")
            print("Você se prepara para o pior.")

    elif escolha == "escotilha":
        print("Você decide abrir a escotilha e explorar o exterior da estação espacial...")
        print("Você vê uma paisagem desolada e assustadora lá fora.")
        escolhaPaisagem = input("Você continua explorando ou volta para dentro? (explorar/voltar): ").lower()
        
        if escolhaPaisagem == "explorar":
            print("Enquanto explora, você encontra marcas estranhas no solo.")
            print("De repente, você é cercado por uma horda de criaturas alienígenas.")
            print("Você tenta correr, mas é capturado!")
        elif escolhaPaisagem == "voltar":
            print("Você decide voltar para dentro da estação.")
            print("Enquanto retorna, você ouve um estrondo vindo da escotilha.")
            print("Você se prepara para o pior.")

    else:
        print("Opção inválida. Por favor, escolha 'sala' ou 'escotilha'.")

filmeTerrorAlienigenas()

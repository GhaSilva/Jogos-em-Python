import random
def jogar():
    print("*******************************")
    print("Bem vindo ao jogo de Advinhação")
    print("*******************************")

    numero_secreto = random.randrange(1,101)
    total_de_tentativas = 0
    rodada = 1
    pontos = 1000

    print("Qual o nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")
    nivel = int(input("Sua escolha: "))

    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5



    for rodada in range(1, total_de_tentativas+1):
        print("Tentativa {} de {}" .format(rodada,total_de_tentativas))
        chute = int(input("Digite seu numero: "))
        if(chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100")
        print("Você digitou ", chute)

        acertou = numero_secreto == chute
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (acertou):
            print("Você acertou")
            print("Você acertou e fez {} pontos!".format(pontos))
            break

        else:
            if (maior):
                print("Você errou! O seu chute foi maior do que o número secreto")
            elif (menor):
                print("Você errou! O seu chute foi menor do que o número secreto")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos -= pontos_perdidos
            rodada += 1

    print("Fim de jogo")

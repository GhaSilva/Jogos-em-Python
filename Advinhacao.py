print("*******************************")
print("Bem vindo ao jogo de Advinhação")
print("*******************************")

numero_secreto = 42
total_de_tentativas = 3
rodada = 1


while(rodada <= total_de_tentativas):
    print("Tentativa {} de {}" .format(rodada,total_de_tentativas))
    chute = int(input("Digite seu numero: "))

    print("Você digitou ", chute)

    acertou = numero_secreto == chute
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if (acertou):
        print("Você acertou")
        break
    else:
        if (maior):
            print("Você errou! O seu chute foi maior do que o número secreto")
        elif (menor):
            print("Você errou! O seu chute foi menor do que o número secreto")
        rodada += 1
print("Fim de jogo")
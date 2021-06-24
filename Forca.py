def jogar():
    print("*******************************")
    print("***Bem vindo ao jogo de Forca**")
    print("*******************************")

    palavra_secreta = "banana".upper()
    letras_acertadas = ["_", "_", "_", "_", "_", "_"]
    enforcou = False
    acertou = False
    erros = 0
    print(letras_acertadas)
    while(not enforcou and not acertou):

        chute = input("Qual letra? ").strip().upper()

        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute.upper() == letra.upper()):
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

        if(acertou):
            print("Parabens, você ganhou!")
        else:
            print("Você perdeu...")


    print("Fim de jogo")
if(__name__ == "__main__"):
    jogar()
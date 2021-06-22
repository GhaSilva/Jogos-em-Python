import Forca
import Advinhacao

print("*******************************")
print("*******Escolha seu jogo********")
print("*******************************")

def escolhe_jogo():
    print("(1) Forca (2) Advinhação")

    jogo = int(input("Qual jogo? "))

    if(jogo == 1):
        print("Jogando Forca")
        Forca.jogar()
    elif(jogo == 2):
        print("Jogando Advinhação")
        Advinhacao.jogar()
if(__name__ == "__main__"):
    escolhe_jogo()
import Forca
import Advinhacao

print("*******************************")
print("*******Escolha seu jogo********")
print("*******************************")


print("(1) Forca (2) Advinhação")

jogo = int(input("Qual jogo? "))

if(jogo == 1):
    print("Jogando Forca")
    Forca.jogar()
elif(jogo == 2):
    print("Jogando Advinhação")
    Advinhacao.jogar()
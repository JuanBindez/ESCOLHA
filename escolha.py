import random
import os


maquina_escolheu = random.randrange(0, 9)

vc_escolheu = int(input("escolha um numero de 0 a 9:"))

if maquina_escolheu == vc_escolheu:
    os.system("clear")
    print("parabéns vc acertou")

else:
    os.system("clear")
    print("a maquina escolheu: \n", maquina_escolheu)
    print("vc escolheu: \n", vc_escolheu)

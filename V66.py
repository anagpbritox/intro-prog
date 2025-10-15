# @cikey b8c2f0e997296c4047aa90efbb14a388
# @sid 20251174010038
# @aid V6.6

# você deve ter feito o anterior

import random

def megasena():
    nummegasena = random.randint(1, 1000)
    trys = 0
    while True:
        palpite = int(input("Digite um numero entre 1 e 1000: "))
        trys += 1
        if trys >= 6:
            print("acabou suas tentativas")
            break

        if palpite < nummegasena:
            print("O numero secreto e MAIOR.")
        elif palpite > nummegasena:
            print("O numero secreto e ENOR.")
        else:
            print(f"Parabens! Você acertou! O numero secreto era {nummegasena}.")
            break
       
megasena()
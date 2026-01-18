# @cikey b8c2f0e997296c4047aa90efbb14a388
# @sid 20251174010038
# @aid V7.3


import random

def quinadavirada():
    numeros = random.sample(range(1, 41), 25)
    numeros.sort()
    return numeros
print(quinadavirada())
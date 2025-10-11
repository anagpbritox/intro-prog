# @cikey b8c2f0e997296c4047aa90efbb14a388
# @sid 20251174010038
# @aid V6.4


#begin_inputs
 
#end_inputs

def craps():
    jogadas = input().split(",")
    jogadas = [int(j.strip()) for j in jogadas]

    primeiro = jogadas[0]

    if primeiro in (7, 11):
        print("Voce ganhou!")
        return
    elif primeiro in (2, 3, 12):
        print("Voce perdeu!")
        return
    else:
        ponto = primeiro
        for valor in jogadas[1:]:
            if valor == ponto:
                print("Voce ganhou!")
                return
            elif valor == 7:
                print("Voce perdeu!")
                return
        print("Jogo inconclusivo (nenhum ponto ou 7 obtido).")

craps()
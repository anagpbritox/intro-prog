# @cikey b8c2f0e997296c4047aa90efbb14a388
# @sid 20251174010038
# @aid V5.2


#begin_inputs


#end_inputs

minutos = 0
tempo_tartaruga = 1  
tempo_lebre = 10 

while True:
    minutos += 1
    tartaruga = 500 + tempo_tartaruga * minutos
    lebre = tempo_lebre * minutos
    if lebre > tartaruga:
        print(minutos)
        break
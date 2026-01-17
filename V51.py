# @cikey b8c2f0e997296c4047aa90efbb14a388
# @sid 20251174010038
# @aid V5.1


#begin_inputs
 

#end_inputs

soma = 0

while True:
    peso = int(input())   
    soma += peso
    if soma> 500:
        print("Peso excedido")
        break
# @cikey b8c2f0e997296c4047aa90efbb14a388
# @sid 20251174010038
# @aid V4.2


#begin_inputs

contador = 0

for n in range(10):
    idade = int(input("Digite as idades: "))
    if idade >= 18:
        contador += 1

#end_inputs

print(contador)
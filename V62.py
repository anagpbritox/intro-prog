# @cikey b8c2f0e997296c4047aa90efbb14a388
# @sid 20251174010038
# @aid V6.2


#begin_inputs

n = int(input())

#end_inputs

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end = " ")
    print()
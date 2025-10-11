# @cikey b8c2f0e997296c4047aa90efbb14a388
# @sid 20251174010038
# @aid V6.3


#begin_inputs

n = int(input())
  
#end_inputs

def reverso(n):
    return int(str(n)[::-1])

print(reverso(n))
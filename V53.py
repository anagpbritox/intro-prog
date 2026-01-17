# @cikey b8c2f0e997296c4047aa90efbb14a388
# @sid 20251174010038
# @aid V5.3


#begin_inputs

crescimento_ceara_mirim = 1.03
ceara_mirim = 73000

crescimento_taipu = 1.10
taipu = 12000

crescimento_parnamirim = 1.01
parnamirim = 250000

#end_inputs

ano = 0

while parnamirim > ceara_mirim and parnamirim > taipu:
    parnamirim = round(parnamirim * crescimento_parnamirim)
    ceara_mirim = round(ceara_mirim * crescimento_ceara_mirim)
    taipu = round(taipu * crescimento_taipu)
    ano += 1

print(f"Parnamirim sera a terceira cidade em: {ano}")
print(f"Populacao Parnamirim: {parnamirim}")
print(f"Populacao Ceara mirim: {ceara_mirim}")
print(f"Populacao Taipu: {taipu}")
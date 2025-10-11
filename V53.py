# @cikey b8c2f0e997296c4047aa90efbb14a388
# @sid 20251174010038
# @aid V5.3


#begin_inputs

taipu = 12000
tx_taipu = 0.1 * taipu
parnamirim = 250000
tx_parnamirim = 0.01 * parnamirim
cearamirim = 73000
tx_cm = 0.03 * cearamirim

#end_inputs

ano = 0

while parnamirim > cearamirim and parnamirim > taipu:

    taipu = taipu + tx_taipu
    tx_taipu = 0.1 * taipu
    parnamirim = parnamirim + tx_parnamirim
    tx_parnamirim = 0.01 * tx_parnamirim
    cearamirim = cearamirim + tx_cm
    tx_cm = 0.03 * cearamirim

    ano += 1

print(ano)
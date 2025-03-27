import random

soma = 0
randon = -1

while randon !=0:
    randon = random.randint(0,9)
    print(f"Número gerado {randon}")
    soma += randon
if(randon == 0):
    print(f"Total: {soma}")
from random import randint as rd

def funcao(a,b,c):
    n1 = rd(a,b)
    n2 = rd(a,b)
    resultado = 0

    if c == "soma":
        return n1 + n2
    elif c == "subtração":
        return n1 - n2
    elif c == "multiplicação":
        return n1 * n2
          

print(funcao(1, 20, "soma"))



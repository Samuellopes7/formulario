print ("Digite uma palavra")
p = str(input (""))
vogais = 0
consoante = 0

for letra in p:
    if letra in "aeiou":
        vogal = vogais + 1
    else:  
        consoantes = consoantes + 1

print("O número de vogais e:", vogais, "O número de consoantes", consoantes)          

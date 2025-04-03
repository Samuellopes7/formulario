nome = input("Digite seu nome: ")

while nome != "joe":
    nome = input("Digite seu nome: ")
    

for tentativas in range(3):
    senha = input("Digite sua senha:")  
    if senha == "swordfish":
        print("Correta")
        break
    else:
        print("Errado")

print("Encerramento")
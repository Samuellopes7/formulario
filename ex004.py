print("Digite um número")
soma = input()

soma_di = 0

for digito in soma:
    if digito.isdigit():
        soma_di += int(digito)

print("A soma dos digitos é:", soma_di)

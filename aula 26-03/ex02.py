from random import randint
soma = 0
min = 1000
max = 0
for i in range(10):
    n = randint (0,100)
    if n % 10 == 0:
     print("bonus") 
    else:
       soma += n
       if n < min:
         min =n
       if n > max:
        max = n
        print(soma, min, max)



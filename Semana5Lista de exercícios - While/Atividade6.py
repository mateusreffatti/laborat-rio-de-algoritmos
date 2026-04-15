import random

oliveiras = random.randint(1, 100)

while True:
    palpite = int(input("Tente adivinhar a quantidade de oliveiras (1 a 100): "))
    
    if palpite < oliveiras:
        print("Há mais oliveiras, tente um número maior.")
    elif palpite > oliveiras:
        print("Há menos oliveiras, tente um número menor.")
    else:
        print("Parabéns! Você descobriu a quantidade de oliveiras!")
        break

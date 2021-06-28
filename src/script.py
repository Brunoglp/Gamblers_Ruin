import random

def bet():
    coins = 50 # Fichas al comienzo
    cont = 0 # Contador
    while coins > 0:
        cont += 1
        coins -= 1 # Le resta 1 porque estoy gastando una ficha
        n = random.randrange(11) # Randomizer con probabilidad del 40%
        if 0 < n < 4:
            coins += 2
        else:
            coins -= 1
        if cont == 300: # Para testear que funciona, se baja este IF de contador (a 10 por ejemplo)
            print(f'Le quedan {coins} fichas')
    print(f'Su noche de apuestas terminó! Ha realizado {cont} apuestas')

for i in range(1,21):
    bet()

# bug: si gano me imprime los dos prints (15;16)
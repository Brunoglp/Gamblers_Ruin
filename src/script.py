import random

def bet(coins, bets):
    cont = 0 # Contador
    while coins > 0 and cont < bets:

        n = random.randrange(11) # Randomizer con probabilidad del 40%
        if 0 < n < 4:
            coins += 1
        else:
            coins -= 1

        print(f'Le quedan {coins} fichas')

        cont += 1

    print(f'Su noche de apuestas terminó con {cont} apuestas')
    return cont, coins
        

result_coins = 0
for x in range(0, 20):
    result_coins += bet(50, 300)[1]
mid_value = result_coins / 20

result = bet( 50, 300 )

print(f'El valor medio de la cantidad de apuestas final es de {mid_value}')
print(f'Apostaste {result[0]} veces y te quedaste con un total de {result[1]} fichas')

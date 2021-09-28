#https://www.youtube.com/watch?v=8ext9G7xspg
import random

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c': 
# Para quando o feedback disser que está correto
        if low != high:
# Se o valor minimo é diferente do máximo, o computador, pensará outro valor
            guess = random.randint(low, high)
# O computador pensa de forma que estabelece parametros, sendo low ou high
# Incialmente, low corresponde a 1 e high ao valor dado de x
        else:
            guess = high  # could also be high b/c low = high
        feedback = input(f'É {guess} mauito alto (H) muito baixo (L), ou correto (C)? ').lower()
        if feedback == 'h': 
#Se o valor é 'h', o código estabelece um novo valor de high, sendo o prórprio - 1
#Por exemplo, se guess é 60, e o feedback é 'h' o novo parametro recebe high = 59
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    #quando o feedback = 'c'
    print(f'O computador encontrou o número, {guess}, corretamente!')


computer_guess(100)

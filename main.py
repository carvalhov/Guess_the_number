import random
#https://docs.python.org/3.7/library/random.html

def guess_a_number(x):
    #random_number recebe a função de numeros aleátorios entre 1 e x; 
    random_number = random.randint(1, x) 
    guess = 0
    #Enquanto o guess é diferente do numero alatório, o while contínua rodando, logo, só parará, se random_number é encontrado
    while guess != random_number:
        guess = int(input("Digite um numero entre 1 e " + str(x) + ": "))
        #dicas, para caso o valor esteja maior ou menor, que o numero pensado
        if guess < random_number:
            print("O numero está tão baixo.")
        elif guess > random_number:
            print("O numero está tão alto.")
    #Caso a o while encerrar, significa que o guess = random_number, logo, o jogador venceu e descobriu o número         
    print("Parabéns, você pensou o valor o numero correto")

guess_a_number(100)

#importando bibliotecas
from random import randint
#regras do jogo:
print('vamos jogar pedra, papel ou tesoura?')
print('''Escolha um número:
       0 - Pedra
       1 - papel
       2 - tesoura''')

#definindo as variaveis

item = ['Pedra','Papel','Tesoura']  #lista de opções

winner = 0    #Variavel de stop

#Montando interface do jogo:

while winner < 5:

    jg = int(input('Faça sua escolha: '))   #Escolha do jogador.

    pc = randint(0, 2)      #escolha do pc

    winner = winner + 1

    if pc < jg:     #jogador ganha.

        print(f'Você ganhou', item[jg], 'ganha de', item[pc])

    elif pc > jg:   #pc ganha.

        print(f'Eu ganhei', item[pc], 'ganha de', item[jg])

    else:   #empate.

         print('Empatamos')

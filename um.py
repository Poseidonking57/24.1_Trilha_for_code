#Pedra papel e tesoura 
import random as rd
import time as tp

print("Vamos jogar um pedra, papel ou tesoura?")
print('''Escolha um número:
       0 - Pedra
       1 - papel
       2 - tesoura''')
#Definindo as variaveis.
itens = ["Pedra", "Papel", "Tesoura"]

jg = int(input("Faça sua escolha: "))

pc = rd.randint(0,2)
#Montando o código.
pass #while 
if jg == pc:
    print('Preparar')
    tp.sleep(1)
    print('Apontar')
    tp.sleep(1)
    print('Vai')
    print(f'Eu escolhi,',itens[pc],f'e você também.',"Empatamos 😅")
elif jg < pc:
    print('Preparar')
    tp.sleep(1)
    print('Apontar')
    tp.sleep(1)
    print('Vai')
    print(itens[pc],'ganha de', itens[jg],"então eu ganhei 😜")
else:
    print('Preparar')
    tp.sleep(1)
    print('Apontar')
    tp.sleep(1)
    print('Vai')
    print(itens[jg],'ganha de', itens[pc],"Você ganhou 😑")
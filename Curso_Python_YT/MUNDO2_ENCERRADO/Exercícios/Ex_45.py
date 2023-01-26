from emoji import emojize
from random import randint
from time import sleep
import pygame
pygame.mixer.init()
pygame.init()

print('-='*20)
print('BEM VINDO AO PEDRA, PAPEL, TESOURA')
print('-='*20)
print('')
print('Você está preparado ? \n')
print(emojize('Suas opções: \n[ 0 ] PEDRA \U0001faa8\n[ 1 ] PAPEL \U0001f5de\uFE0F  \n[ 2 ] TESOURA \U0001f52a'))
itens = ('Pedra','Papel','Tesoura')
itens_emoji =('\U0001faa8','\U0001f5de','\U0001f52a')
escolha = int(input('\nQual é a sua jogada? \n~ '))
computador = randint(0, 2)

print('\n')
print('-='*20)
print(' '*10 + ' !!! JO KEN PO!!!')
print('-='*20)
print('\n')
pygame.mixer.music.load('JOKENPO.mp3')
pygame.mixer.music.play()
pygame.event.wait()
# 0 pedra perde para papel
# 1 papel perde para tesoura
# 2 tesoura perde para pedra

if computador == 0: #PEDRA
    if escolha == 0:
        print(f'Você jogou {itens[escolha]} vs computador {itens[computador]}\n')
        sleep(1)
        print(f'     {itens_emoji[escolha]}  vs {itens_emoji[computador]}\n')
        sleep(1)
        print('EMPATE')
    elif escolha == 1:
        print(f'Você jogou {itens[escolha]} vs computador {itens[computador]}\n')
        sleep(1)
        print(f'     {itens_emoji[escolha]}  vs {itens_emoji[computador]}\n')
        sleep(1)
        print('VOCÊ GANHOU')
    elif escolha ==2:
        print(f'Você jogou {itens[escolha]} vs computador {itens[computador]}\n')
        sleep(1)
        print(f'     {itens_emoji[escolha]}  vs {itens_emoji[computador]}\n')
        sleep(1)
        print('VOCÊ PERDEU')
    else:
        print('INVALIDO')
elif computador == 1: #PAPEL
    if escolha == 0:
        print(f'Você jogou {itens[escolha]} vs computador {itens[computador]}\n')
        sleep(1)
        print(f'     {itens_emoji[escolha]}  vs {itens_emoji[computador]}\n')
        sleep(1)
        print('VOCÊ PERDEU')
    elif escolha == 1:
        print(f'Você jogou {itens[escolha]} vs computador {itens[computador]}\n')
        sleep(1)
        print(f'     {itens_emoji[escolha]}  vs {itens_emoji[computador]}\n')
        sleep(1)
        print('EMPATE')
    elif escolha ==2:
        print(f'Você jogou {itens[escolha]} vs computador {itens[computador]}\n')
        sleep(1)
        print(f'     {itens_emoji[escolha]}  vs {itens_emoji[computador]}\n')
        sleep(1)
        print('VOCẼ GANHOU')
    else:
        print('INVALIDO')
elif computador == 2: #TESOURA
    if escolha == 0:
        print(f'Você jogou {itens[escolha]} vs computador {itens[computador]}\n')
        sleep(1)
        print(f'     {itens_emoji[escolha]}  vs {itens_emoji[computador]}\n')
        sleep(1)
        print('VOCÊ GANHOU')
    elif escolha == 1:
        print(f'Você jogou {itens[escolha]} vs computador {itens[computador]}\n')
        sleep(1)
        print(f'     {itens_emoji[escolha]}  vs {itens_emoji[computador]}\n')
        sleep(1)
        print('VOCÊ PERDEU')
    elif escolha ==2:
        print(f'Você jogou {itens[escolha]} vs computador {itens[computador]}\n')
        sleep(1)
        print(f'     {itens_emoji[escolha]}  vs {itens_emoji[computador]}\n')
        sleep(1)
        print('EMPATE')
    else:
        print('INVALIDO')
else:
    print('INVALIDO')
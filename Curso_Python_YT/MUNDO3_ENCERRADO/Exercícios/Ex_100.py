from random import randint
from time import sleep
numeros = list()

def sorteia():
    print('Sorteando 5 valores da lista:',end=' ')
    for i in range(0,5):
        numeros.append(randint(0,10))
        print(numeros[i],end=' ',flush=True)
        sleep(0.25)
    print('PRONTO!')


def somaPar():
    cont = 0
    for i in numeros:
        if i % 2 ==0:
            cont += i
    print(f'A somas dos numeros pares em {numeros} é {cont}')

sorteia()
somaPar()
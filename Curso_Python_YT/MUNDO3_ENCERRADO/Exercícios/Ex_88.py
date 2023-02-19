from random import randint
a = int(input('Quantos jogos você quer que eu sorteie? '))
lista = []
base = []
q1 = 0
for j in range(0,a):
    for jogo in range(0,6):
        base.append(randint(0,60))
    lista.append(base[:])
    base.clear()
for q in lista:
    print(f'Jogo {q1+1}: {q}')
    q1 +=1

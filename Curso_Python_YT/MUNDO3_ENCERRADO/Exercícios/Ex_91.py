from random import randint
jogadores = dict()
from operator import itemgetter
i = 1

for d in range (0,4):
    jogadores[f'jogador{d+1}'] = randint(1,6)
    
print('Valores sorteados: \n')
for k,v in jogadores.items():
    print(f'{k} tirou {v} no dado')

print('-='*20)
print(f'{"==":>5} RANKING DOS JOGADORES {"==":<5}')

for j,d in sorted(jogadores.items(), key=itemgetter(1), reverse=True):
    print(f'Em {i}º lugar: {j} jogou {d}')
    i += 1

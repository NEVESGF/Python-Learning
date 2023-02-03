jogador = dict()
jogos = list()
qtd = cont = soma = 0

jogador['nome'] = str(input('Nome do Jogador: ')).strip()
qtd = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for i in range(0,qtd):
    jogos.append(int(input(f'Quantos jogos na partida {cont}? ')))
    cont += 1
    soma = jogos[-1] + soma 
jogador['gols'] = jogos[:]
jogador['total'] = soma
print('-='*20)
print(jogador)
print('-='*20)
for j,v in jogador.items():
    print(f'O campo {j} tem o valor {v}')
print('-='*20)
print(f'O jogador {jogador["nome"]} jogou {cont} partidas.')
cont = 0
for i in jogador['gols']:
    print(f'   => Na partida {cont}, fez {i} gols.')
    cont +=1
jogador = dict()
jogos = list()
jogadores = list()
qtd = cont = soma = 0

while True:
    jogador['nome'] = str(input('Nome do Jogador: ')).strip()
    qtd = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    
    for i in range(0,qtd):
        jogos.append(int(input(f'Quantos gols na partida {cont}? ')))
        cont += 1
        soma = jogos[-1] + soma 
    jogador['gols'] = jogos[:]
    jogador['total_gols'] = soma
    jogador['partidas'] = qtd
    qtd = cont = soma = 0
    jogos.clear()
    jogadores.append(jogador.copy())
    
    a = str(input('Quer continuar? [S/N ]')).strip().upper()[0]
    if a in 'Nn':
        break
print('-='*25)
print(f'cód {"nome":<16} {"gols":<16} total_gols partidas')
print('-'*50)

for c,n in enumerate(jogadores):
    #print(f'{c} {n["nome"]:<16} {n["gols"]:<16} {n["total_gols"]:<10} {n["partidas"]}')
    print(f'{c:>3} {n["nome"]:<16} {str(n["gols"]):<16} {n["total_gols"]:<10} {n["partidas"]}')
print('-'*50)
while True:
    a = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if a == 999:
        break
    elif a != 999 and a <= len(jogadores)-1:
        print('-'*50)
        print('-- LEVANTAMENTO DO JOGADOR')

        print(jogadores[a]["gols"])

    elif a > len(jogadores)-1:
        print(f'ERRO! Não existe jogador com o código {a}!')
    
'''print('-='*20)
    print(f'O jogador {jogador["nome"]} jogou {cont} partidas.')
    cont = 0
    for i in jogador['gols']:
        print(f'   => Na partida {cont}, fez {i} gols.')
        cont +=1'''
#print(jogadores)

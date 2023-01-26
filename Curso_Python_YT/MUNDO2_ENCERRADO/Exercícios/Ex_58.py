from random import randint
num_escolhido = int(input('Escolha um número entre 0 e 10: \n~ '))
num_computador = randint(0,10)
num_tentativas = 0

print('-='*20)
print('JOGO DA ADVINHAÇÃO')
print('-='*20)
print('\n')

while num_computador != num_escolhido:
    print(f'O número {num_escolhido} não é o mesmo escolhido pela máquina, tente novamente.')
    num_escolhido = int(input('Digite um novo número entre 0 e 10 \n~ '))
    num_tentativas += 1
print('\n')
print(f'Você acertou, o número escolhido foi o {num_computador} você precisou de {num_tentativas} chances até acertar')

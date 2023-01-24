from random import randint

print('-='*20)
print(f"{'PAR OU IMPAR':^40}")
print('-='*20)

j = c = cont = s = 0
esc = comput = ''

while True:
    j = int(input('Diga um valor: '))
    esc = str(input('Par ou Ímpar [P/I] ')).strip().upper()[0]
    print('-'*20)
    c = randint(0,10)
    s = c + j

    if (c + j) % 2 == 0:
        comput = 'P'
    elif (c + j) % 2 != 0:
        comput = 'I'
    else:
        print('ERRO')

    if comput == esc:
        print('Você VENCEU!\nVamos jogar novamente...')
        print('-'*20)
    else:
        print('Você PERDEU!')    
        break
    cont += 1
print(f'FIM DE JOGO! Você venceu {cont} vezes seguidas.')
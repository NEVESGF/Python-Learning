lista = []
a = 0
e = ''
while True:
    if e != 'N':
        a = int(input('Digite um valor: '))
        if a in lista:
            print('Valor duplicado! Não vou adicionar...')
        else:
            lista.append(a)
            print('valor adicionado com sucesso...')
        e = str(input('Quer continuar? [S/N] ')).strip().upper()
    else:
        break
lista.sort()
print('-='*20)
print(f'Você digitou os valores {lista}')
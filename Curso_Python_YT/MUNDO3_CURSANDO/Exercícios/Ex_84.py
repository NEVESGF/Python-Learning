lista = []
base = []
qtd = maiorpes = menorpes = pes = 0

b = ''
while True:
    base.append(str(input('Nome: ').strip()))
    base.append(int(input('Peso: ')))
    pes = int(base[1])
    lista.append(base[:])
    base.clear()
    qtd +=1
    while True:
        b = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if b == 'S' or b == 'N':
            break
    if b in 'N':
        break

    if maiorpes == 0:
        maiorpes = pes
    elif pes < maiorpes:
        if menorpes > pes or menorpes == 0:
            menorpes = pes

print('-='*20)
print(f'Ao todo, você cadastrou {qtd} pessoas.')
print(f'O maior peso foi de {maiorpes}. Peso de ',end='')
for c in lista:
    if c[1] == maiorpes:
        print(c[0],end=' ')
print(f'\nO menor peso foi de {menorpes}. Peso de ',end='')
for d in lista:
    if d[1] == menorpes:
        print(d[0],end=' ')

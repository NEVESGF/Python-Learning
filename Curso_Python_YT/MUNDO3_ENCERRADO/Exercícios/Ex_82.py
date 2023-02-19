lista = []
pares = []
impares = []

while True:
    valor = int(input('Digite um valor: '))
    lista.append(valor)
    while True:
        b = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if b in 'SN':
            break
    if valor % 2 == 0:
        pares.append(valor)
    else:
        impares.append(valor)
    if b in 'Nn':
        break
    
print(f'A lista completa é {lista}')
print(f'A lista de pares é {pares}')
print(f'A lista de impares é {impares}')
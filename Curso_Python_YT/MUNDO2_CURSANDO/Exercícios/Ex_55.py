lista = []
for p in range(1,7):
    peso = float(input(f'Peso da {p}º pessoa: '))
    lista.append(peso)
    lista.sort()
print(f'O maior peso lido foi de {lista[0]}Kg')
print(f'O menor peso lido foi de {lista[-1]}Kg')
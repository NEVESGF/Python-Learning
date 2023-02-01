lista = [[0,0,0],[0,0,0],[0,0,0]]
soma = soma3 = maior = 0

for l in range(0,3):
    for i in range(0,3):
        lista[l][i] = int(input(f'Digite um valor para [{l},{i}]: '))
print('-='*20)
for a in range(0,3):
    for b in range(0,3):
        print(f'[{lista[a][b]:^5}]',end='')
    print()
print('-='*20)
for p in lista:
    for par in p:
        if par % 2 == 0:
            soma += par
print(f'A soma dos valores pares é {soma}')
for j in lista:
    soma3 += j[2]
print(f'A soma dos valores da terceira coluna é {soma3}')
for q in lista[1]:
    if maior == 0 or q > maior:
        maior = q
print(f'O maior valor da segunda linha é {maior}')
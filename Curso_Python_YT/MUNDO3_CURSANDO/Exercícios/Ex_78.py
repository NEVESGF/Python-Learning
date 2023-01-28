valores = up = down = list()
maior = menor = 0
for cont in range(0,5):
    valores.append(int(input('Digite um valor: ')))
 
    if cont == 0:
        maior = menor = valores[cont]
    else:
        if valores[cont] > maior:
            maior = valores[cont]
        if valores[cont] < menor:
            menor = valores[cont]

print(f'o maior foi {maior} nas posições ',end='')
for i,v in enumerate(valores):
    if v == maior:
        print(f'{i}...',end='')
print()
print(f'O menor valor foi o {menor} nas posições ',end='')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i}...',end='')
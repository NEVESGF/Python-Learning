galeura = list()
dado = list()
totmai = totmen = 0
for c in range (0,3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galeura.append(dado[:])
    dado.clear()
print(galeura)

for p in galeura:
    if p[1] >=21:
        print(f'{p[0]} é maior de idade.')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade')
        totmen +=1

print(f'Temos {totmai} maiores de idade e {totmen} menores de idade.')
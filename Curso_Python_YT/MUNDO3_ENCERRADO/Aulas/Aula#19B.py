'''brasil = list()
estado1 = {'uf':'Rio de Janeiro','sigla': 'RJ'}
estado2 = {'uf': 'São Paulo','sigla':'SP'}
brasil.append(estado1)
brasil.append(estado2)

print(brasil[0]['sigla'])'''

estado = dict()
brasil = list()

for c in range(0,2):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    #brasil.append(estado[:]) NO LUGAR DE [:] utiliza-se o comando copy
    brasil.append(estado.copy())
for e in brasil:
    for v in e.values():
        print(v)
print(brasil)
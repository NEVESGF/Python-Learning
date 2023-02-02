#Dicionarios são identificados como { }

dados=dict()
dados={'nome':'Pedro','idade':25}
print(dados['nome'])
print(dados['idade'])

# para adicionar

dados['sexo'] = 'M'

#para eliminar

del dados['idade']

####

print(dados.values()) #mostra o que esta na lista
print(dados.keys())   #mostra o nome de cada numeração
print(dados.items())  #mostra os dados e os nomes

####

for k,v in dados.items():
    print(f'O {k} é {v}')
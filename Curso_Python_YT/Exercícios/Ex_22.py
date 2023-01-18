nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print(f'Seu nome em maiúsculas é {nome.upper()}')
print(f'Seu nome em minúsculas é {nome.lower()}')

print(f'Seu nome tem ao todo {len(nome.replace(" ",""))} letras')
#para remover o espaço poderia ser também len(nome)-nome.count(' ')

print(f'Seu primeiro nome é {nome.split()[0]} e ele tem {len(nome.split()[0])} letras')
#poderia ser nome.find(' ') ele localiza onde é o primeiro espaço e fala quantos caracteres tem o primeior nome

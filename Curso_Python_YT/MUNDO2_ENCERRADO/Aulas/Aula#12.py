#Alinhado é uma estrutura condicional dentro de uma condicional

'''if:
    elif:
    elif:
    .
    .
    .
    else:'''

nome = str(input('Qual é o seu nome? '))

if nome == 'Guilherme':
    print('Que nome bonito')
elif nome == 'Maria' or nome == 'Pedro' or nome == 'João':
    print('Seu nome é bem popular no Brasil')
else:
    print('Seu nome é bem normal.')
print(f'Tenha um bom dia {nome}')
a = str(input('Digite a sua expressão: '))

b = int(a.count('('))
c = int(a.count(')'))

if b == c:
    print('Sua expressão é válida')
else:
    print('Sua expressão é inválida')
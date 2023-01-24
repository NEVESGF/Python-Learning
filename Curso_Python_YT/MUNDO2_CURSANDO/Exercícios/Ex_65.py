digite = cont = soma = 0
escolha = ''
lista = []
while escolha != 'N':
    digite = int(input('Digite um número: '))
    soma += digite
    cont += 1
    escolha = input('Quer continuar? [S/N] ').strip().upper()
    lista.append(digite)
    lista.sort()
print(f'Você digitou {cont} valores e a média foi {soma/cont:.2f}')
print(f'O maior valor foi {lista[-1]} e o menor foi {lista[0]}')

n1 = float(input('Digite o primeiro valor: '))
n2 = float(input('Digite o segundo valor: '))
n3 = float(input('Digite o terceiro valor: '))
lista = [n1,n2,n3]
lista.sort()
print(lista)
print(f'O menor valor digitado foi {lista[0]}')
print(f'O maior valor digitado foi {lista[2]}')
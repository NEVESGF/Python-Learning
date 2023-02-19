
a = int(input('Digite um número: '))
b = int(input('Digite outro número: '))
c = int(input('Digite mais um número: '))
d = int(input('Digite o último número: '))
lista = (a,b,c,d)

print(f"Você digitou os valores {lista}")
print(f"O valor 9 apareceu {lista.count(9)}")
if 3 in lista:
    print(f"O valor 3 apareceu na {lista.index(3)}º posição")
else:
    print('O valor 3 não foi digitado.')
print('Os valores pares digitados foram: ', end='')
for par in lista:
    if par % 2 == 0:
        print(lista[par], end='')

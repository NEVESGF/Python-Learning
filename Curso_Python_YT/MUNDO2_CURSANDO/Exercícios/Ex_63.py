i = int(input('Escolha a quantidade de números: '))
lista=[1]
lista.append(lista[0])
j = 0
while j < i:
    lista.append(lista[-1]+lista[-2])
    j+=1
print(lista)
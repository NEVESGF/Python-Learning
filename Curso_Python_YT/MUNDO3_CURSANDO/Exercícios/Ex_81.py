lista = []
b = ''
contador = 0
while True:
    if b != 'N':
        a = int(input('Digite um valor: '))
        lista.append(a)
        while True:
            b= str(input('Quer continuar? [S/N]')).strip().upper()[0]
            if b == 'S' or b =='N':
                break
        contador +=1
    if b == 'N':
        break
lista.sort(reverse=True)
print('-='*20)
print(f'Você digitou {contador} elementos')
print(f'Os valores em ordem decrescente são {lista}')
print(f"O valor 5 {'faz' if (5 in lista) else 'não faz' } parte da lista")
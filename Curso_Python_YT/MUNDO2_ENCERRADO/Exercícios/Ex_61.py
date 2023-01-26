n1 =int(input('Digite o primeiro termo: '))
n2 =int(input('Digite a razão da PA: '))
j=1
print(f'{n1}',end=' -> ')
while j <= 10:
    print(f'{n1+n2}', end=' -> ')
    n1 += n2
    j += 1
print('FIM')
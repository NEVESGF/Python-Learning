n1 =int(input('Digite o primeiro termo: '))
n2 =int(input('Digite a razão da PA: '))
j=1
print(f'{n1}',end=' -> ')
while j <= 9:
    print(f'{n1+n2}', end=' -> ')
    n1 += n2
    j += 1
print('PAUSA')
n = 0
i = 1
while i!=0:
    i = int(input('Quantos termos você quer mostrar a mais? '))
    while n <= i-1:
        print(f'{n1+n2}', end=' -> ')
        n1 += n2
        n += 1
        j += 1
    n = 0
    print('PAUSA')
print(f'Progressão finalziada com {j} termos')
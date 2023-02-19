def area(l1,l2):
    ar = l1*l2
    print(f'A área de um terreno {a}x{n} é de {ar}m²')

print(f'{"Controle de Terrenos":^30}')
print('-'*30)

a = float(input('LARGURA (m): '))
n = float(input('COMPRIMENTO (n): '))

area(a,n)
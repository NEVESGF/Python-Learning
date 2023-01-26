print('='*20)
print(''*5+'10 TERMOS DE UMA PA')
print('='*20)
print('\n')
n1 = int(input('Primeiro termo: '))
n2 = int(input('Razão: '))
for c in range(n1,n1+20,n2):
    print(c, end='->')
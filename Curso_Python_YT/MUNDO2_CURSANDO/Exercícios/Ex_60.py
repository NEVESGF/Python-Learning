import math
i = int(input('Digite o número que deseja saber o fatorial: '))
print(f'{i}!=',end='')
for j in range (i,0,-1):
    print(f'{j}',end='')
    if j != 1:
        print('',end='x')
    else:
        print('',end='')
print(f'={math.factorial(i)}')

i_w = i_i = int(input('Digite o número que deseja saber o fatorial: '))
print(f'{i_w}!=',end='')
while i_w != 0:
    print(f'{i_w}',end='')
    i_w = i_w - 1
    if i_w != 0:
        print('',end='x')
    else:
        print('',end='')
print(f'={math.factorial(i_i)}')

num = int(input('Digite um número: '))
qt_div = 0
for primo in range(1,num+1):
    if num % primo == 0:
        qt_div += 1
        print(f'\033[33m{primo}\033[m', end=' ')
    else:
        print(f'\033[31m{primo}\033[m', end=' ')
print('')
print(f'O número {num} foi divisivel {qt_div} vezes.')
print('E por isso ele', 'NÃO É PRIMO' if qt_div>2 else 'É PRIMO', '!')
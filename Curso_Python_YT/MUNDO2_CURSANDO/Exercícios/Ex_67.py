n = 0
print('-='*20)
print(f"{'TABUADA 3.0':^20}")
print('-='*20)

print('\n\n')

while True:
    n = int(input('Digite o valor que deseja a tabuada (negativo para parar): '))
    if n < 0:
        break
    print(f' 1 X {n} = {1*n:2}\n 2 X {n} = {2*n:2}\n 3 X {n} = {3*n:2}\n 4 X {n} = {4*n:2}\n 5 X {n} = {5*n:2}\n 6 X {n} = {6*n:2}\n 7 X {n} = {7*n:2}\n 8 X {n} = {8*n:2}\n 9 X {n} = {9*n:2}\n10 X {n} = {10*n:2}\n')
    

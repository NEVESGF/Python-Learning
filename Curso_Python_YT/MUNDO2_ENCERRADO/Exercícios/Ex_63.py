n1 = 0
n2 = 0
n3 =1
j = t = 0
i = int(input('Digite a quantidade: '))
while j < 3:
    j +=1
    if n2 <2:
        print(f'{n2+n1}',end=' -> ')
        n2 +=1
    else:
        while j <= i:
           # j = 3
            n2 = n3
            print(f' {n2+n1}', end=' -> ')
            n3 = n2 + n1
            n1 = n2
            j += 1
print('FIM')

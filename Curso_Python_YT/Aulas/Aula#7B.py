n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1+n2
m = n1*n2
d = n1/n2
d1 = n1//n2
e = n1**n2

print('A soma é {}, o produto é {} e a divisão é {:.3f}'.format(s,m,d), end=' ')
print('Divisão inteira é {} e potência {}'.format(d1,e))

# se digitar no final do print end='' ele concatena com o print da linha de baixo
# se digitar no meio do print \n ele quebra a linha no meio


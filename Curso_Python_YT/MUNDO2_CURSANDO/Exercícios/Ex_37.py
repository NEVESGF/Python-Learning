num = int(input('Digite um número inteiro: '))
print('Escolha uma das bases para conversão:')
print('[ 1 ] converter para BINÁRIO')
print('[ 2 ] converter para OCTAL')
print('[ 3 ] converter para HEXADECIMAL')
esc = float(input('Sua opção: '))

if esc == 1:
    print(f'{num} convertido para BINARIO é igual a {bin(num)[2:]}')
elif esc == 2:
    print(f'{num} convertido para OCTAL é igual a {oct(num)[2:]}')
elif esc == 3:
    print(f'{num} convertio para HEXADECIMAL é igual a {hex(num)[2:]}')
else:
    print('Essa escolha não é válida!')
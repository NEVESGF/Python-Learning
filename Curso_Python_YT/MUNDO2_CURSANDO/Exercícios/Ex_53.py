frase = input('Digite uma frase: ').upper().strip().replace(' ','')
frase_inv = frase[::-1]
print(f'O inverso de {frase} é {frase_inv}')
if frase == frase_inv:
    print('A frase digitada é um palíndromo')
else:
    print('A frase digitada não é um palíndromo')

#todo método tem parenteses no final ()
#Aula de estruturas condicionais
# if ...() : else:

tempo=int(input('Quantos anos tem seu carro? '))
if tempo <=3:
    print('Carro novo')
else:
    print('Carro velho')
print('--FIM--')

#condição simplificada

tempo=int(input('Quantos anos tem seu carro? '))
print('carro novo'if tempo <=3 else'carro velho')
print('--FIM--')
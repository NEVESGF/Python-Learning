#laço de repetição ou iteração
#laço de variável de controle

'''
for c in range(1,10):
    passo
pega
'''

for c in range(0,6):
    print('Oi')
print('fim')

#se quiser que ele conte de trás para frente precisa colocar a iteração no final

for c in range(6,0,-1):
    print(c)
print('fim')

#Exemplo

s = 0
for c in range(0,4):
    n = int(input('Digite um valor: '))
    s += n # mesma coisa que digitar s = s+n
print(f'O somatório de todos os valores é {s}')
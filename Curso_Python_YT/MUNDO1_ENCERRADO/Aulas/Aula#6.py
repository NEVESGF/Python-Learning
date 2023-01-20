#Resolvendo desafio da aula 4

#int = números inteiros, sem virgula
#float = números com virgulas (pontos)
#bool = True or False
#str = string, palavras entre aspas
#.format = é um método que substitui {}

num1 = int(input('Primeiro número '))
num2 = int(input('Segundo número '))
s = num1 + num2
#print ('A soma entre', num1, 'e', num2, 'vale' s)
print('A soma entre {} e {} vale {}'.format(num1,num2,s))


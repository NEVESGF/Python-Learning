
'No python existem três tipos de números'
'      int'
'      float'
'      complex'


'Os números do tipo int, são os números inteiros, + ou - que não possuem casa decimal.'

num1 = 300
num2 = -80 
print(type(num1))
print(type(num2))

'Os números do tipo float, são os números racionais e irracionais, ou seja, são números positivos e negativos que possuem casa decimal.'

num3 = 300.5 #número positivo com uma casa decimal
num4 = -433.6776 #número negativo com quatro casas decimais
print(type(num3))
print(type(num4))

'Os números do tipo complex, são compostos por uma parte real e outra imaginária.'

num5 = 2 + 4j
num6 = 4j
num7 = -10j
print(type(num5))
print(type(num6))
print(type(num7))

"O python, possui um módulo que gera um número aleatório."

import random
#Gera um número inteiro aleatório entre 0 e 10
z = random.randint(0,10)
print(z)
# Nesta aula aprenderemos a importar bibliotecas em python.
# para incluir alguma coisa tem que utilizar o comando import
# é possivel importar apenas uma coisa da biblioteca completa

# Para verificar quais biliotecas estão disponiveis basta acessar o Python.org

#import math
#from math import sqrt,ceil

import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print(f'A raiz de {num:.1f} é igual a {math.ceil(raiz)}')

#Quando se importa apenas o que precisa da biblioteca não é necessário digitar o .math
from math import sqrt
print(sqrt(25))

import random
num = random.randint(1,10)
print(num)

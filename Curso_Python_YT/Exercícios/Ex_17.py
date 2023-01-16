import math
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
print(f'A hipotenusa vai medir {math.hypot(co,ca):.2f}')

#como utilizou apenas o hypot poderia ter feito from math import hypot

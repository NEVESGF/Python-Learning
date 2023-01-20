import math
ang = float(input('Digite o ângulo que você deseja: '))
print(f'O ângulo de {ang:.2f} tem o SENO de {math.sin(math.radians(ang)):.2f} \nO ângulo de {ang:.2f} tem o COSSENO de {math.cos(math.radians(ang)):.2f} \nO ângulo de {ang:.2f} tem a TANGENTE de {math.tan(math.radians(ang)):.2f}')

#poderia ser from math import radians, sin, cos, tan

print("Ola, você quer par ou impar?")
x=(input())
import random
from sqlite3 import paramstyle
z = random.randint(0,1)
print(z)
if z == 0:
    zr = "par"
else:
    zr = "impar"
if x == zr :
    print("você ganhou")
else:
    print("se fudeu")
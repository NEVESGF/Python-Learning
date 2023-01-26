from random import randint

lista = (randint(0,5),randint(0,5),randint(0,5),randint(0,5),randint(0,5))

print(lista)
print(f"O menor valor é {sorted(lista)[0]}")
print(f"O maior valor é {sorted(lista)[len(lista)-1]}")

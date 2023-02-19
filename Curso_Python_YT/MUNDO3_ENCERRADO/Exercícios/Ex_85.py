base = []
pares = []
impares = []
a=0

for i in range(0,8):
	a = int(input(f'Digite o {i}o. valor:'))
	base.append(a)
	
	if a % 2 ==0:
		pares.append(a)
	else:
		impares.append(a)

print('-='*20)
print(f'Os valores pares digitados foram: {pares}')
print(f'Os valores impares digitados foram: {impares}')
print(f'A lista de valores digitados foi {base}')
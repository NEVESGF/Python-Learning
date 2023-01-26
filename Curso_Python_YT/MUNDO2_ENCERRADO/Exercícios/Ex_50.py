s = 0
for c in range (1,7):
    n = int(input(f'{c:2} - Digite um número: '))
    if n % 2 == 0:
        s += n
print(f'A soma entre os números pares foi de {s:2}')
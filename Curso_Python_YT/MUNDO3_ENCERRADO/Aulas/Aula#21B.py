def fatorial(num = 1):
    f = 1
    for c in range (num, 0, -1):
        f *= c
    return f

n = int(input('digite um número: '))
print(f'O factorial de {n} é {fatorial(n)}')
n = s = c = 0
while True:
    n = int(input('Digite um valor (999 para parar): '))
    c += 1
    if n == 999:
        break
    s += n
print(f'A soma dos {c} valores foi {s}!')
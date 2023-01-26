s = 0
c = 0
for n in range(0,500,3):
    if n % 3 == 0 and n % 2 ==1:
        c += 1
        s += n
print(f'A soma de todos {c} os valores é {s}.')
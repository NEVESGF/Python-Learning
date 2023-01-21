s = [0]
for c in range(1,51):
    if c % 2 == 0:
        s.append(c)
s.append('fim')
print(s)

##outra maneira ocupando menos do processador

for c in range(0,51, 2):
    print(c, end=' ')
print('Acabou')
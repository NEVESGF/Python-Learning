lista = list()
base = list()
d=0
for l in range(0,3):
    for i in range(0,3):
        base.insert(i,int(input(f"Digite um valor para [{l}, {i}]: ")))
    lista.insert(l,base[:])
    base.clear()
print('-='*20)
for d in range(0,3):
    for c in range(0,3):
        print(f"[{lista[d][c]:^5}]",end='')
    print('')

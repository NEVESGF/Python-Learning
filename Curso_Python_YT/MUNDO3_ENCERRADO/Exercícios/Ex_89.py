lista = list()
base =list()
i=0
while True:
    base.append(str(input('Nome: ').strip()))
    base.append(float(input('Nota 1: ')))
    base.append(float(input('Nota 2: ')))
    lista.append(base[:])
    base.clear()
    while True:
        a = str(input('Quer Continuar ? [S/N]: ')).strip().upper()
        if a in 'SnNn':
            break
    if a in 'Nn':
        break
print('-='*20)
print(f"{'No.':<4} {'NOME':<15} {'MÉDIA':<5}")
print('-'*30)
for j in range(0,len(lista)):
    print(f"{j:<4} {lista[j][0]:<15} ",end='')
    print(f"{(lista[j][1]+lista[j][2])/2:<5.1f}")
print('-'*30)
while True:
    b = int(input('Mostrar nota de qual aluno ? [999 interrompe]: '))
    if b == 999:
        break
    else:
        print(f'As notas de {lista[b][0]} foram {lista[b][1:3]}')
        print('-'*30)

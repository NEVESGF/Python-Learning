valores = []
b = 0
for cont in range(0,5):
    a = int(input('Digite um valor: '))
    valores.append(a)
    for a in valores[0:cont]:
        b = valores.index(a)
        print(b)
        '''if valores[0] < a:
            valores.insert(1,a)
            print(valores)
            #valores.pop()
        else:
            valores.insert(0,a)
            print(valores)
            #valores.pop()'''
    valores.pop()
print(valores)
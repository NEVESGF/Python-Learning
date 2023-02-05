def soma(a,b):
    soma = a + b
    print(soma)

soma(8,5)

#empacotador (*algumacoisa)
#permite colocar quantos valores quiser
def contador(*num):
    print(num)

def suma(*valores):
    s = 0
    for num in valores:
        s += num
    print(f'A soma dos valoes {valores} é {s}')
    
suma(2,3,5,7,5,1,2,3,4)
n=1
par =0
impar =0
while n!=0:
    n = int(input('Digite um valor: '))
    if n!=0:
        if n % 2 ==0:
            par +=1
        else:
            impar +=1
print(f'Foram digitados {par} valores par e {impar} impares de um total de {par + impar} inserções')
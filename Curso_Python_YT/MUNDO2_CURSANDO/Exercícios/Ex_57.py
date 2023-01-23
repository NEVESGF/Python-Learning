sexo = 'inicio'
cont_M = cont_F = 0
while sexo != 'FIM':
    sexo = str(input('Digite o sexo [M/F]: ').strip().upper()[0])
    if sexo != 'FIM':
        if sexo == 'M':
            cont_M +=1
        elif sexo == 'F':
            cont_F +=1
        elif sexo != 'M' or sexo != 'F':
            print('Digite novamente o sexo')
print(f'A quantidade de mulheres é de {cont_F} e de homens de {cont_M}')
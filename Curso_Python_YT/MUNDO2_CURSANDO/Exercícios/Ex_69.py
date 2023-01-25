print('-'*20)
print(f"{'CADASTRE UMA PESSOA':20}")
print('-'*20)
i = c = maior_idade = qtd_homens = mulher_menor = 0
sexo = continuar = ' '
while True:
    i = int(input('Idade: '))
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if i >= 18:
        maior_idade += 1
    if sexo == 'M':
        qtd_homens += 1
    if sexo == 'F' and i <20:
        mulher_menor +=1
    print('-'*20)
    c += 1
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        print('-'*20)
    if continuar == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {maior_idade}')
print(f'Ao todo temos {qtd_homens} homens cadastrados.')
print(f'E temos {mulher_menor} mulheres com meno de 20 anos.')

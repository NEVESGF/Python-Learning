nome_l = []
idade_l = []
idade_lM = []
sexo_l = []
nome_lM = []
idade_lF = []
qtd_F = 0
j=3

for p in range(1,j+1):
    print('-'*5,f'{p}º PESSOA','-'*5)
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ')

    nome_l.append(nome)
    idade_l.append(idade)
    sexo_l.append(sexo)

    if sexo == 'F':
        qtd_F += 1
    if sexo == 'F' and idade < 20:
        idade_lF.append(idade)
    elif sexo =='M':
        idade_lM.append(idade)
        nome_lM.append(nome)

print(f'A média de idade do grupo é de {sum(idade_l)/j:.1f}')
print(f'O homem mais velho tem {max(idade_lM)} anos e se chama {nome_lM[idade_lM.index(max(idade_lM))]}.')
print(f'Ao todo são {len(idade_lF)} com menos de 20 anos')
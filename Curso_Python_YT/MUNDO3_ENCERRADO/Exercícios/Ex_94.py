pessoas = dict()
todas_pessoas = list()

while True:
    pessoas['nome'] = str(input('Nome: ')).strip()
    while True:
        pessoas['sexo'] = str(input('Sexo [M/F] ')).strip().upper()[0]
        if pessoas['sexo'] in 'FM':
            break
        else:
            print('Erro! Por favor, digite apenas M ou F.')
    pessoas['idade'] = int(input('Idade: '))
    todas_pessoas.append(pessoas.copy())
    pessoas.clear()
    while True:
        a = str(input('Quer continuar? [S/N]')).strip().upper()[0]
        if a in 'SN':
            break
        else:
            print('ERRO! Responda apenas S ou N.')
    if a == 'N':
        break
print('-='*20)
print(f'A) Ao todos temos {len(todas_pessoas)} cadastradas.')
soma = 0
for a in todas_pessoas:
    soma = soma + a['idade']
print(f'B) A média de idade é de { soma / len(todas_pessoas):.2f} anos.')
print(f'C) As mulheres cadastradas foram: ',end='')
for b in todas_pessoas:
    if b['sexo'] == 'F':
        print(b['nome'],end=' ')
print('')
print('D) Lista das pessoas que estão acima da média:')
for c in todas_pessoas:
    if c['idade'] >= soma/len(todas_pessoas):
        print(f'    nome = {c["nome"]}; sexo = {c["sexo"]}; idade = {c["idade"]};',end='\n')
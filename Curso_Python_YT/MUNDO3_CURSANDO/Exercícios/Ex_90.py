aluno = dict()

aluno['Nome'] = str(input('Nome: ').strip())
aluno['Média'] = float(input(f'Média de {aluno["Nome"]}: '))
aluno['Resultado'] = 'Aprovado' if aluno['Média'] > 7 else 'Reprovado'

for p,s in aluno.items():
    print(f'{p} é igual a {s}')
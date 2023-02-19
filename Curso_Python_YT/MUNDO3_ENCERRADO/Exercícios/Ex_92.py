from datetime import datetime as dt

trabalhador = dict()

trabalhador['nome'] = str(input('Nome: ')).strip()
trabalhador['ano_nasc'] = int(input('Ano de Nascimento: '))
trabalhador['idade'] = dt.today().year - trabalhador['ano_nasc']
trabalhador['carteira'] = int(input('Carteira de trabalho (0 não tem): '))
if trabalhador['carteira'] == 0:
    print('-='*20)
else:
    trabalhador['contratacao'] = int(input('Ano de Contratação: '))
    trabalhador['salario'] = float(input('Salário: R$'))
    trabalhador['aposentadoria'] = 65
    print('-='*20)

for d,v in trabalhador.items():
    print(f' - {d} tem o valor {v}')
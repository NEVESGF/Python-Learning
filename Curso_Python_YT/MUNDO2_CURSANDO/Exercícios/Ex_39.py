import datetime as dt
ano = int(input('Digite o ano do seu nascimento: '))
idade = dt.datetime.today().year-ano
print(f'Quem nasceu em {ano} tem {idade} anos em {dt.datetime.today().year}')

if idade>18:
    print(f'Você já deveria ter se alistado há {idade-18} anos')
    print(f'Seu alistamento foi em {dt.datetime.today().year - (idade-18)}.')
elif idade<18:
    print(f'Ainda faltam {18-idade} anos para o seu alistamento.')
    print(f'Seu alistamento será em {dt.datetime.today().year + (18-idade)}.')
else: 
    print(f'Você deve se alistar IMEDIATAMENTE!')

#print(dt.date.today().year)


tabela = ('Palmeiras','Internacional','Fluminense','Corinthians','Flamengo','Athletico-PR','Atlético-MG','Fortaleza','São Paulo','América-MG','Botafogo','Santos','Goiás','Bragantino','Coritiba','Cuiabá','Ceará','Atlético-GO','Avaí','Juventude')

print('Os primeiros 5 colocados foram:')
for pos, colocados in enumerate(tabela[0:6]):
        print(f'{pos+1} - {colocados}')
print('\n')
print('Os quatro últimos colocados foram')
for pos, colocados in enumerate(tabela[15:20]):
    print(f'{pos+16} - {colocados}')
print('\n')
print(sorted(tabela))
print('\n')
print(f"O São Paulo terminou na posição {tabela.index('São Paulo')+1}")
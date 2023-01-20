
n1 = float(input('Primeira Nota: '))
n2 = float(input('Segunda Nota: '))
media = (n1+n2)/2
print(f'Tirando {n1} e {n2}, a média do aluno é {media:.1f}')
if media >= 6:
    print('O aluno passou de ano.')
else:
    print('O aluno está de recuperação')
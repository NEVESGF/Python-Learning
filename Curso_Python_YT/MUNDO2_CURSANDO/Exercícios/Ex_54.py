from datetime import date
menor = 0
maior = 0
for p in range(1,8):
    ano = int(input(f'Em que ano a {p}º pessoa nasceu? '))
    if date.today().year - ano < 21:
        menor += 1
    else:
        maior += 1
print(f'Ao todo tivemos {maior} pessoas maiores de idade')
print(f'E também tivemos {menor} pessoas menores de idade')

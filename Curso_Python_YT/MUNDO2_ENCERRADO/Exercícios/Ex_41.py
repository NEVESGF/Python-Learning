import datetime
import emoji
idade1 = int(input('Digite em que ano você nasceu: '))
idade2 = datetime.datetime.today().year - idade1
print(f'O atleta tem {idade2} anos.')

if idade2 <= 9:
    print(emoji.emojize('A classificação do Atleta é MIRIM \U0001f476'))
elif idade2 <=14:
    print(emoji.emojize('A classificação o Atleta é INFANTIL \U0001f9d2'))
elif idade2 <=19:
    print(emoji.emojize('A classificação do Atleta é JUNIOR \U0001f466'))
elif idade2 <=25:
    print(emoji.emojize('A classificação do Atleta é SÊNIOR \U0001f9d4'))
elif idade2 >25:
    print(emoji.emojize('A classificação do Atleta é MASTER \U0001f474'))
else:
    print('Entrada de dados incorreta')
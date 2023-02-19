from datetime import date
def voto(i):
    global a, b
    idade = date.today().year - a
    print(f'Com {idade} anos:',end=' ')
    if idade >=65:
        print('VOTO OPCIONAL')
    elif idade >= 18:
        print('VOTO OBRIGATÓRIO')
    elif idade >= 16:
        print('VOTO OPCIONAL')
    else:
        print('NÃO VOTA')

a = 0
a = int(input('Em que ano você nasceu? '))
voto(a)
  
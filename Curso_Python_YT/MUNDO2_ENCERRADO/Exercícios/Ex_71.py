print('='*20)
print(f"{'BANCO CEV':^20}")
print('='*20)
valor = c50 = c20 = c10 = c5 = 0

valor = int(input('Qual valor você quer sacar? R$'))
while True:

    if valor % 50 != 0 and valor % 50 > 0:
        c50 = (valor / 50)
        valor = valor % 50
    elif valor % 50 == 0:
        c50 = valor/50

    if c50 - int(c50) > 0:
        if valor % 20 != 0 and valor % 20 > 0:
            c20 = (valor / 20)
            valor = valor % 20    
        elif valor % 20 == 0:
            c20 = valor / 20
            
    if c20 - int(c20) > 0:
        if valor % 10 != 0 and valor % 10 > 0:
            c10 = (valor / 10)
            valor = valor % 10
        elif valor % 10 == 0:
            c10 = valor / 10

    if c10 - int(c10) > 0:
            if valor % 5 != 0 and valor % 5 > 0:
                c5= (valor / 5)
                valor = valor % 5
            elif valor % 5 == 0:
                c5= valor / 5
    '''else:
        print('ERRO')'''

    print(f'Total de {int(c50)} cédulas de R$50') if c50 >= 1 else ''
    print(f'Total de {int(c20):.0f} cédulas de R$20') if c20 >= 1 else ''
    print(f'Total de {int(c10):.0f} cédulas de R$10') if c10 >= 1 else ''
    print(f'Total de {int(c5):.0f} cédulas de R$5') if c5 >= 1 else ''

    break
print('='*20)
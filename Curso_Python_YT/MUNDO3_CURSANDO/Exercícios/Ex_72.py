numero = ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')

while True:
    esc = int(input('Qual número deseja saber? [0:20] '))
    if esc > 0 and esc <20:
        break
    else:
        print('Tente Novamente. ', end='')
print(f'o número escolhido foi {esc} que em extenso é {numero[esc]}')


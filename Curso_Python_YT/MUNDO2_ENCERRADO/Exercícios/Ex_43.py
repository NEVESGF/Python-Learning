import math
print('')
print('Cálculo de IMC')
print('')

nome = input('Digite o seu nome: ').strip().capitalize()
peso = float(input('Qual é o seu peso? (Kg) '))
altura = float(input('Qual é a sua altura? (m) '))

IMC = peso / (altura**altura)
print(f'Olá {nome}, o seu IMC é de {IMC:.2f} você está na faixa ', end='')

if IMC <18.5:
    print('ABAIXO DO PESO')
elif IMC < 25:
    print('PESO IDEAL')
elif IMC < 30:
    print('SOBREPESO')
elif IMC <40:
    print('OBESIDADE')
else:
    print('OBESIDADE MÓRBIDA')
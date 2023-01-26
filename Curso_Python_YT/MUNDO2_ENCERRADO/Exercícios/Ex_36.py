import time
import emoji

print('-='*20)
print('Cálculo de Empréstimo')
print('-='*20)
print(' ')
nome = str(input('Qual é o seu nome ? ').strip())
print(f'Bom dia {nome}, vamos começar!')
time.sleep(1)
print(' ')
valor = float(input(emoji.emojize(':money_with_wings: Qual o valor do imóvel que você deseja adquirir? R$')))
sal = float(input(emoji.emojize(':money_with_wings: Qual o valor do seu salário mensal? R$')))
anos = float(input(emoji.emojize(':books: Em quantos anos deseja efetuar o pagamento? ')))
print('')
time.sleep(0.5)
print('Calculando...')
time.sleep(2)
print('')

prestacao = valor/(anos*12) #prestação mensal

if prestacao > sal*0.3:
    print(emoji.emojize('Infelizmente o seu empréstimo foi \033[0;41mNEGADO!\33[m'))
    print(f'Visto que as parcelas de R${prestacao:.2f} excedem os 30% do seu salário.')
    print(f'O salário mínimo necessário nas condições indicadas deveria ser de {sal*0.3}')
else:
    print('O seu empréstimo foi \033[0;42mAPROVADO!\033[m')
    print(f'As prestações mensáis serão de R${prestacao:.2f} durante {anos} anos')
print('Obrigado por fechar negócio com o nosso banco.')
